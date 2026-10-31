import duckdb
import pandas as pd

# 1. SQL - Cria o WMS simulado (o que o sistema diz)
con = duckdb.connect("loss.db")
con.execute("""
CREATE TABLE IF NOT EXISTS estoque_wms (
  sku VARCHAR, local_cd VARCHAR, saldo_wms INT, valor_unit DECIMAL
);
DELETE FROM estoque_wms;
INSERT INTO estoque_wms VALUES 
('SKU12345','A3-12-4', 10, 150.00),
('SKU12346','A3-12-5', 5, 89.90),
('SKU12347','A3-12-6', 20, 45.50);
""")

# 2. SQL + Spark (DuckDB faz o papel do Spark) - Detecta perda
df = con.execute("""
SELECT 
  c.sku,
  c.local_cd,
  c.qtd_coletada,
  w.saldo_wms,
  (w.saldo_wms - c.qtd_coletada) as divergencia_qtd,
  (w.saldo_wms - c.qtd_coletada) * w.valor_unit as divergencia_rs,
  CASE WHEN w.saldo_wms > c.qtd_coletada THEN 'FALTA_FISICA' ELSE 'OK' END as tipo_perda
FROM read_csv('data/raw_coletor/*.csv') c
JOIN estoque_wms w ON c.sku = w.sku
""").df()

print("--- GOLD PERDA DIARIA - ITUPEVA ---")
print(df)

# 3. Salva Gold
df.to_parquet("data/gold_perda_diaria.parquet")
print(f"\nPerda total: R$ {df['divergencia_rs'].sum():.2f}")

# 4. Alerta pro Telegram (seu multi-agente)
if df['divergencia_rs'].sum() > 0:
    print(f"\n🚨 ALERTA: Enviar pro Telegram: Perda de R$ {df['divergencia_rs'].sum()} no corredor A3")

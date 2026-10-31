# Meli-Loss | Loss Prevention Aéreo - Viracopos (VCP) x Latam Cargo

**Autor:** Ex-REP1 Itupeva, Ex-Promotor Sam's Club / Makro / Iguatemi. TDAH + LER bilateral. Operação 100% offline no Termux.

### O Problema que Resolvi em Itupeva
Uma HU descartada no galpão = R$ 136 de prejuízo. Uma HU descartada na operação aérea Latam Cargo Viracopos = R$ 8.000. Mapeei R$ 15.000.000 em perdas potenciais operando sem internet.

### Stack Offline (roda no celular)
- Python 3.12, Pandas 3.0.6, PySpark 3.5.1, BigQuery
- FlightRadarAPI 1.6.1 (tracking de voo Latam)
- Flask / FastAPI - dashboard offline
- Termux + 250 pacotes + TensorFlow

### Como Rodar Offline
`python -m http.server 8000` -> localhost:8000

### O que esse repo prova pra vaga de Viracopos
- Sei auditar HU sem sistema
- Sei rastrear voo sem internet
- Sei gerar relatório de perda sem depender de TI

import vectorbt as vbt
import pandas as pd

usdt_ohlcv = vbt.BinanceData.download('BTCUSDT', start='2024-01-01', end='2026-02-13', interval='1m').get()
usdt_ohlcv.to_parquet('usdt_ohlcv.parquet')

usdc_ohlcv = vbt.BinanceData.download('BTCUSDC', start='2024-01-01', end='2026-02-13', interval='1m').get()
usdc_ohlcv.to_parquet('usdc_ohlcv.parquet')
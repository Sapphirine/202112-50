import pandas as pd
import numpy as np
from numpy import concatenate
import yfinance as yf

def get_stock_prices(ticker,period):
	stock_prices = yf.download(tickers=ticker, period = period, interval = '1d')

	return stock_prices
# Daily Stock Price and Volume in TWSE (fill datestring in %s)
TAIWAN_URL = "https://www.twse.com.tw/en/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALL"

# The interval (Unit: days) of the history record of stocks in Taiwan
TW_STOCK_INTERVAL = 5 * 365

# The database name for the stocks in Taiwan
TW_STOCK_DB = "tw_stock.db"
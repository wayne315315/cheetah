# Database
DB = "securities.db"

# URL for Daily Stock Price and Volume in TWSE
TAIWAN_URL = "https://www.twse.com.tw/en/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALL"

# The interval of the history record of stocks in Taiwan (Unit: day)
TW_STOCK_INTERVAL = 15 * 365

# Crawling-related configuration (Unit: second)
CRAWL_INTERVAL = 10
PENALTY_TIME = 3600
PENALTY_FACTOR = 1.1
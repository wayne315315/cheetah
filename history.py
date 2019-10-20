import time
from datetime import date, timedelta
import sqlite3

from crawl import crawl_tw_stock
from config import TW_STOCK_INTERVAL, TW_STOCK_DB


oneday = timedelta(days=1)
today = date.today()

def update_tw_stock():
	conn = sqlite3.connect(TW_STOCK_DB)
	conn.row_factory = sqlite3.Row
	c = conn.cursor()

	curr = today
	table = curr.isoformat().replace("-", "")
	for _ in range(TW_STOCK_INTERVAL):
		df = crawl_tw_stock(table)
		if df is not None:
			df.to_sql(table, conn)
			print("update %s" % curr.isoformat())
		curr -= oneday
		table = curr.isoformat().replace("-", "")
		c.execute("SELECT * FROM sqlite_master WHERE type='table'")
		res = c.fetchall()
		if table in map(lambda row: row["name"], res):
			break
		time.sleep(0.5)
	conn.commit()
	conn.close()
	print("Finished...")

if __name__ == "__main__":
	update_tw_stock()
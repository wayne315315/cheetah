import random
import time
from datetime import date, timedelta
import sqlite3

from crawl import crawl_tw_stock
from config import TW_STOCK_INTERVAL
from config import DB, CRAWL_INTERVAL, PENALTY_TIME, PENALTY_FACTOR


oneday = timedelta(days=1)
today = date.today()

def update():
	with sqlite3.connect(DB) as conn:
		update_tw_stock(conn)

def update_tw_stock(conn):
	"""Crawling stocks starting from yesterday to 'TW_STOCK_INTERVAL' days ago"""
	c = conn.cursor()
	curr = today
	penalty = PENALTY_TIME
	schema = (
		'\"Date\" TEXT',
		'\"Security Code\" TEXT',
		'\"Trade Volume\" INTEGER', 
		'\"Transaction\" INTEGER', 
		'\"Trade Value\" INTEGER', 
		'\"Opening Price\" REAL',
		'\"Highest Price\" REAL', 
		'\"Lowest Price\" REAL', 
		'\"Closing Price\" REAL', 
		'\"Change\" REAL',
		'\"Last Best Bid Price\" REAL', 
		'\"Last Best Bid Volume\" REAL', 
		'\"Last Best Ask Price\" REAL',
		'\"Last Best Ask Volume\" REAL',
		'\"Price-Earning ratio\" REAL',
		'primary key (\"Date\", \"Security Code\")'
		)

	# create table
	c.execute('CREATE TABLE IF NOT EXISTS tw_stock (%s, %s, \
		%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' % schema)

	for _ in range(TW_STOCK_INTERVAL):
		curr -= oneday
		datestring = curr.isoformat()

		while True:
			try:
				df = crawl_tw_stock(datestring)
			except OSError:
				print("Connection Error...")
				print("penalty time: %.2f hour" % (penalty / 3600))
				time.sleep(penalty)
				penalty *= PENALTY_FACTOR
			else:
				penalty = PENALTY_TIME
				break

		if df is not None:
			df["Date"] = datestring
			try:
				df.to_sql("tw_stock", conn, if_exists="append")
			except sqlite3.IntegrityError:
				break
			print("'tw_stock': update %s" % datestring)

		time.sleep(random.random() * CRAWL_INTERVAL)

	print("Finished updating 'tw_stock'")

if __name__ == "__main__":
	update()
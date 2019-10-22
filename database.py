import sqlite3

import pandas as pd

from config import DB


def load_tw_stock():
	"""
	load all data in to memory
	vulnerable to out of memory error
	"""
	with sqlite3.connect(DB) as conn:
		df = pd.read_sql_query(
			"SELECT * FROM tw_stock",
			conn,
			index_col=["Security Code", "Date"],
			parse_dates=["Date"])
	return df

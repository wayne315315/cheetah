from io import StringIO

import requests
import pandas as pd

from config import TAIWAN_URL, TIMEOUT


def crawl_tw_stock(datestring):
	"""datestring needs to be isoformat"""
	datestring = datestring.replace("-", "")
	url = TAIWAN_URL % datestring

	rawdata = requests.get(url, timeout=TIMEOUT).text
	if not rawdata:
		return None

	header, footer = [], []
	for i, line in enumerate(rawdata.split("\n")):
	    if "Security Code" in line:
	        header.append(i)
	    if "Remarks:" in line:
	        footer.append(i)
	header, footer = header[0], footer[-1]
	rawdata = "\n".join(rawdata.replace("=", "").split("\n")[header:footer])

	usecols = ['Security Code',
	           'Trade Volume', 
	           'Transaction', 
	           'Trade Value', 
	           'Opening Price',
	           'Highest Price', 
	           'Lowest Price', 
	           'Closing Price', 
	           'Dir(+/-)', 
	           'Change',
	           'Last Best Bid Price', 
	           'Last Best Bid Volume', 
	           'Last Best Ask Price',
	           'Last Best Ask Volume', 
	           'Price-Earning ratio']

	df = pd.read_csv(StringIO(rawdata), usecols = usecols, index_col="Security Code")
	df = df.apply(lambda s: pd.to_numeric(s.astype(str).str.replace(",", "").replace("+", "1").replace("-", "-1"), errors='coerce'))
	df = df.fillna(value={"Dir(+/-)":0})
	df["Change"] *= df["Dir(+/-)"]
	df = df.drop(columns="Dir(+/-)")

	return df
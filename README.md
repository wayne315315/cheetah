# cheetah
A software tool for downloading all stock information in Taiwan (extendable)

# Installation guide
Step 1 : Type the following command to download the source code to your current directory:<br/>
```
git clone https://github.com/wayne315315/cheetah.git
```

Step 2 : Switch the directory to the "cheetah" folder with the following command:<br/>
```
cd cheetah
(or) 
cd /path/to/cheetah/folder
```

Step 3 : (Optional) Open the 'config.py' file to modify the tracking interval (default: 15 years) :<br/>
```
TW_STOCK_INTERVAL = INTERVAL_LENGTH_IN_DAYS # only positive integer is valid
```

Step 4 : Download all the prerequisites :<br/>
```
pip3 install -r requirements.txt
```

Step 5 : Download all history data with the command (first round may take several days) :<br/>
```
python3 history.py
```

Step 6 : (Optional) Rerun 'history.py' whenever you want to get the most updated information<br/>
```
python3 history.py
```

Step 7 : (Optional) Open jupyter notebook with the following command and run 'demo.ipynb' to learn how to use<br/>
```
jupyter notebook
```

# Footnote
For more information about dataframe manipulation, please check pandas documentation:
https://pandas.pydata.org/pandas-docs/stable/

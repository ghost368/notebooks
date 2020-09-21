#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup


#%%
url = 'https://fxtop.com/en/countries-currencies.php'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


#%%
av_url = 'https://www.alphavantage.co/query'
response = requests.get(av_url, params={'function': 'TIME_SERIES_DAILY', 'symbol': 'IBM', 'apikey': 'ZHI8TJ46LRUXGC50'})

#%%



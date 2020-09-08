#%%
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

#%%

response = requests.get('https://www.tradinghours.com/markets-by-capitalization')
soup = BeautifulSoup(response.content, 'html.parser')

exchanges_table = soup.find('table', id='capTable')
exchanges_table = pd.read_html(str(exchanges_table))[0]

# %%
def parse_market_cap(mkt_cap_str):
    unit_dict = {'Million': 1e6, 'Billion': 1e9, 'Trillion': 1e12}
    unit_pat = '|'.join(unit_dict.keys())
    pattern = rf'\$([.0-9]*)\s*({unit_pat})'
    match = re.match(pattern, mkt_cap_str)
    amount, unit = match.groups()
    amount = float(amount) * unit_dict[unit]
    return amount

def normalize_exchanges_table(exchanges_table):
    

#%%

#%%
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

#%%


def load_cac_table():
    cac_url = 'https://www.bnains.org/archives/histocac/histocac.php'
    response = requests.get(cac_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    cac_table = soup.find('table', class_='table table-bordered table-super-condensed')
    return pd.read_html(str(cac_table))[0]


def normalize_cac_table(cac_table):
    cac_table = (
        cac_table.loc[1:, ['Date', 'Sens', 'Sicovam ou ISIN', 'Valeur']]
        .rename({'Sens': 'Action', 'Sicovam ou ISIN': 'ISIN', 'Valeur': 'Name'}, axis=1)
        .set_index('Date')
    )
    cac_table = cac_table[cac_table['Action'].isin(['Admission', 'Retrait'])]
    cac_table.loc[:, 'Action'] = cac_table['Action'].map(
        {'Admission': 'In', 'Retrait': 'Out'}
    )
    cac_table.index = pd.to_datetime(cac_table.index, format='%d/%m/%Y')
    return cac_table


#%%

cac_table = load_cac_table().pipe(normalize_cac_table)

# %%

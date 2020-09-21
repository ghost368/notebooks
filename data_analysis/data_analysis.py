#%%
import numpy as np
import pandas as pd

from marketdata.daily import get_fx_daily_data
import qplot.activate
from qplot import get_axes


#%%
fx_data = get_fx_daily_data()
close = fx_data['close'].to_pandas().T

fx_rets = close / close.shift().ffill() - 1.0
fx_rets = fx_rets.fillna(0)

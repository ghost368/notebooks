#%%
import numpy as np
import pandas as pd
import scipy as sp

#%%


def f(x):
    for i in x:
        if i == 3:
            raise ValueError
        print(i)

#%%

print('I was here')

#f([1, 2, 3, 4, 5])



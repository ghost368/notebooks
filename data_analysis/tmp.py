#%%
import pandas as pd
import re
from pathlib import Path
import numpy as np
import pandas as pd


#%%

arr = np.zeros((5, 4), dtype=float, order='C')
arr[0, -1] = -1
arr

arr.flatten(order='F')

np.zeros_like(arr)

arr.byteswap().dtype.byteorder
arr.dtype.byteorder

arr.byteswap()

#%%
strarr = np.array(['a', 'bc', 'cd'])
strarr.dtype.byteorder, strarr.byteswap().dtype

strarr.byteswap()

#%%

arr[2, 3] = -4
arr.reshape((2, 10), order='F').T


arr.compress([True, False, True, True, False], axis=0)
arr


np.repeat(arr, 3)
xx = arr.ravel()
xx[3] = 19
arr


yy = np.vstack([arr] * 4)
arr[0, 0] = 12

yy
arr

#%%
arr.dtype


xx = arr.view(dtype=int)

xx.dtype
xx[0, 0] = -123


#%%

dtp = np.dtype([('abc', np.int64), ('xyz', bool)])
dtp

dtp['abc']


recarr = np.array([(1, True), (2, False), (4, True), (-5, False)], dtype=dtp)
recarr['xyz']


#%%
arr[0, 0] = -3

np.asfortranarray(arr).flatten()
#%%

arr = pd.DataFrame([[True, 1], [False, 4]]).to_numpy()
arr = arr.T

recarr = np.core.records.fromarrays(arr, names=['a', 'b'], formats=[bool, int])
recarr['a']


xx = np.recarray(names=['a', 'b'], formats=['bool', 'i8'], shape=(2,))
xx['a']

xx[:]

xx[:] = [(False, 4), (True, 2)]
xx['a']


#%%

arr.dtype

arr2 = arr.astype(float)


arr2[0, 0] = -1
arr

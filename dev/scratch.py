#%%
class Tmp:
    version: 2

    def __init__(self, x):
        self.x = x


#%%

t = Tmp(4)
t.x

Tmp.version

#%%

from dataclasses import dataclass
import numpy as np

class SetItemMixin(object):
    def __setitem__(self, key, value):
        super().__setattr__(key, value)

#%% 

@dataclass
class Group(SetItemMixin):
    x : int
    y : int


#%%
g = Group(4, 5)

#%%
import pandas as pd
import re
from pathlib import Path
import numpy as np
import pandas as pd


#%%

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

#%%

class Point(Singleton):

    dim: int = 2

    def __init__(self, x, y=None):
        if isinstance(x, Point):
            self.x = x.x
            self.y = x.y
        else:   
            self.x=x
            y = y or x
            self.y=y
    
    @classmethod 
    def change_dim(cls):
        cls.dim = 3

    @staticmethod 
    def print():
        print('hello')


#%%
bp = Point(4, 5)
bp2 = Point(10, 15)

bp.x



bp.change_dim()
bp.dim
bp.print()
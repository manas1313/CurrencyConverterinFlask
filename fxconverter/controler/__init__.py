# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:17:15 2020

@author: routm1
"""

import pandas as pd
#import numpy as np


def get_data():
    data = pd.read_csv('currency_map.csv', index_col ="/")
    return data
    
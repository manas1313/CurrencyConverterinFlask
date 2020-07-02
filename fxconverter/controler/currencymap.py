# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:56:39 2020

@author: routm1
"""


import pandas as pd
from fxconverter.logger import logger

data = pd.read_csv('currency_map.csv', index_col ="/")

class CrossCurrency:    
    def get_crosscurrency(base_currency, terms_currency):
        logger.loggerr.debug("get_crosscurrency called with base currency {} and term currency {}".format(base_currency,terms_currency))
#        val = data.loc[base_currency, terms_currency]       
        return data.loc[base_currency, terms_currency]
    
    def get_currencyname():        
#        col= list(data.columns)
        return list(data.columns)



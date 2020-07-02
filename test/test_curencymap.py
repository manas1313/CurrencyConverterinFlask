# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:45:47 2020

@author: routm1
"""

import unittest
import fxconverter.controler.currencymap as cm
import fxconverter.controler.currencypairs as cp

class CurrPair(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.curr = ['AUD', 'CAD', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'JPY', 'NOK', 'NZD', 'USD']
        self.currmap  = {'AUDUSD': '0.8371', 'CADUSD': '0.8711', 'USDCNY': '6.1715', 'EURUSD': '1.2315', 'GBPUSD': '1.5683','NZDUSD': '0.7750','USDJPY': '119.95','EURCZK': '27.6028','EURDKK': '7.4405','EURNOK': '8.6651'}
        
        pass
#        self.func = currencyPair()
#        self.app = app
    @classmethod 
    def tearDownClass(self):
        pass

 
    
    def test_exchange_name(self): 
        self.assertEqual(cm.CrossCurrency.get_crosscurrency('AUD','AUD'),'1')
        self.assertEqual(cm.CrossCurrency.get_crosscurrency('AUD','USD'),'D')
        self.assertEqual(cm.CrossCurrency.get_crosscurrency('JPY','USD'),'INV')
        self.assertEqual(cm.CrossCurrency.get_crosscurrency('GBP','CNY'),'USD')
        self.assertEqual(cm.CrossCurrency.get_crosscurrency('NOK','CZK'),'EUR')
        self.assertEqual(cm.CrossCurrency.get_currencyname(),self.curr)

    
    def test_exrate(self):
        self.assertEqual(cp.CurrencyPairs.ex_rates(),self.currmap)

        
if __name__ == '__main__':
    unittest.main()
    
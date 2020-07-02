# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 04:16:21 2020

@author: routm1
"""

import unittest
import fxconverter.model.currencyconvertr as cc

class ConvertCurrency(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.curr = ['AUD', 'CAD', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'JPY', 'NOK', 'NZD', 'USD']
        self.currmap  = [1]
        
        pass
#        self.func = currencyPair()
#        self.app = app
    @classmethod 
    def tearDownClass(self):
        pass
    
    
    def test_getrate(self):
        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','JPY'),'100.410')
        self.assertEqual(cc.CurrencyConvert.get_rate('DKK','GBP'),'0.106')
        self.assertEqual(cc.CurrencyConvert.get_rate('GBP','CNY'),'0.000')        
        self.assertEqual(cc.CurrencyConvert.get_rate('NOK','USD'),'0.142')
        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','DKK'),'5.058')
        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','CNY'),'0.000') 
        
#        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','CAD'),'0.961')
#        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','CNY'),'0.000')
#        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','CZK'),'18.763')
#        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','DKK'),'5.058')
#        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','EUR'),'0.680')
#        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','GBP'),'0.534')
#        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','JPY'),'100.410')
#        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','NOK'),'5.890')
#        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','NZD'),'1.080')
#        self.assertEqual(cc.CurrencyConvert.get_rate('AUD','USD'),'0.837')
        
#        self.assertEqual(cc.CurrencyConvert.get_rate('CAD','AUD'),'100.410145')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CAD','CNY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CAD','CZK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CAD','DKK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CAD','EUR'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CAD','GBP'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CAD','JPY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CAD','NOK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CAD','NZD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CAD','USD'),'5.057607')
#        
#        self.assertEqual(cc.CurrencyConvert.get_rate('CNY','AUD'),'100.410145')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CNY','CAD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CNY','CZK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CNY','DKK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CNY','EUR'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CNY','GBP'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CNY','JPY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CNY','NOK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CNY','NZD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CNY','USD'),'5.057607')
#
#        self.assertEqual(cc.CurrencyConvert.get_rate('CZK','AUD'),'100.410145')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CZK','CAD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CZK','CNY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CZK','DKK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CZK','EUR'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CZK','GBP'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CZK','JPY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CZK','NOK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CZK','NZD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('CZK','USD'),'5.057607')        
#        
#        self.assertEqual(cc.CurrencyConvert.get_rate('DKK','AUD'),'100.410145')
#        self.assertEqual(cc.CurrencyConvert.get_rate('DKK','CAD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('DKK','CNY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('DKK','CZK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('DKK','EUR'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('DKK','GBP'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('DKK','JPY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('DKK','NOK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('DKK','NZD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('DKK','USD'),'5.057607')
#        
#        self.assertEqual(cc.CurrencyConvert.get_rate('EUR','AUD'),'100.410145')
#        self.assertEqual(cc.CurrencyConvert.get_rate('EUR','CAD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('EUR','CNY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('EUR','CZK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('EUR','DKK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('EUR','GBP'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('EUR','JPY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('EUR','NOK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('EUR','NZD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('EUR','USD'),'5.057607')
#        
#        self.assertEqual(cc.CurrencyConvert.get_rate('GBP','AUD'),'100.410145')
#        self.assertEqual(cc.CurrencyConvert.get_rate('GBP','CAD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('GBP','CNY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('GBP','CZK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('GBP','DKK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('GBP','EUR'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('GBP','JPY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('GBP','NOK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('GBP','NZD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('GBP','USD'),'5.057607')
#        
#        self.assertEqual(cc.CurrencyConvert.get_rate('JPY','AUD'),'100.410145')
#        self.assertEqual(cc.CurrencyConvert.get_rate('JPY','CAD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('JPY','CNY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('JPY','CZK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('JPY','DKK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('JPY','EUR'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('JPY','JPY'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('JPY','NOK'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('JPY','NZD'),'5.057607')
#        self.assertEqual(cc.CurrencyConvert.get_rate('JPY','USD'),'5.057607')
        
        


        
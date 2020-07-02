# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 23:14:48 2020

@author: routm1
"""

from fxconverter.controler.currencypairs import CurrencyPairs
from fxconverter.controler.currencymap import CrossCurrency
import decimal
from flask import current_app



class CurrencyConvert:
    
    
    def convert_currency(from_currency, to_currency):
        base_currency = CrossCurrency.get_crosscurrency(from_currency,to_currency)
        return base_currency   
    
    
    def get_rate1(fcurrency,tcurrency):
        
        list_curr = []
        list_rate = []
        list_curr.append (fcurrency)
        list_curr.append (tcurrency)
        
        for i in range(11):            
            base = CrossCurrency.get_crosscurrency(fcurrency,tcurrency)
            
            
            if (base !='D' and base !='INV'):
                list_curr.append(base)
                tcurrency = base
                
            elif(base =='D'):
                list_rate.append(CurrencyPairs.exchange_rate(fcurrency+tcurrency))
                break
                
            elif(base =='INV'):
                list_rate.append(CurrencyPairs.inv_exchange_rate(fcurrency+tcurrency))
                break
            
        k = len(list_curr)
           
        for j in range(k-2):
            
            k =k-1
            
            fcurrency = list_curr[k]
            tcurrency = list_curr[k-1]
            
            base = CrossCurrency.get_crosscurrency(fcurrency,tcurrency)
            
            if(base =='D'):
                list_rate.append(CurrencyPairs.exchange_rate(fcurrency+tcurrency))                
            elif(base =='INV'):
                list_rate.append(CurrencyPairs.inv_exchange_rate(fcurrency+tcurrency))
                

#        length = len(list_rate)-1
        index = 0
        final_rate = 1
        for m in range(len(list_rate)):
            
#            length = length - 1
#            print(float(list_rate[item]))
            
            if(list_rate[index] != None):
                final_rate = final_rate * float(list_rate[index])
            else:
                final_rate = 0
            
#            if not type() is float:
#                raise TypeError("Only float is allowed")
            
#            final_rate = final_rate * float(list_rate[item])
            index = index + 1

#        print(final_rate)
            
#        final_rate = round(final_rate,4)
        final_rate = decimal.Decimal(final_rate)
        return final_rate
        
    def get_rate(fcurrency, tcurrency):      
        list_curr = []
        list_rate = []        
#        fcurrency = 'AUD'
#        tcurrency = 'DKK'        
        list_curr.append (fcurrency)
        list_curr.append (tcurrency)
        while len(list_curr) >= 2:
#            try
            base = CrossCurrency.get_crosscurrency(fcurrency,tcurrency)
            if(base =='D'):
                list_rate.append(CurrencyPairs.exchange_rate(fcurrency+tcurrency))
                list_curr.remove(fcurrency)
                if len(list_curr) >= 2:
                    fcurrency = list_curr[-1]
                    tcurrency = list_curr[-2]
            elif(base =='INV'):
                list_rate.append(CurrencyPairs.inv_exchange_rate(fcurrency+tcurrency))
                list_curr.remove(fcurrency)
                if len(list_curr) >= 2:
                    fcurrency = list_curr[-1]
                    tcurrency = list_curr[-2]
            else:
                if len(list_curr) >= 2:
                    tcurrency = base
            if base not in {'D','INV','1'}:                
                list_curr.append(base)
        final_rate = 1
#        current_app.logger.info(list_curr)
        for indx, list_rate in enumerate(list_rate):
            if(list_rate != None):
                final_rate = final_rate * decimal.Decimal(list_rate)
            else:
                final_rate = 0
        final_rate = '%.3f'% decimal.Decimal(final_rate)
        return final_rate
 
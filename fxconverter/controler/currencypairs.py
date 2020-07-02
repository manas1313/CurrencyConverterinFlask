# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:14:31 2020

@author: routm1
"""
#import json


class CurrencyPairs:
    
    def __init__(self):
         with open('Currencypairs.txt') as f:
            self.lines = f.readlines()
            
    def chunks(s):        
        f= s[:3]
        l= s[3:]        
        return l+f
    
    def ex_rates():
        with open('Currencypairs.txt') as f:
            lines = f.readlines()         

        rateDict = {}        
        for line in lines:
            parsed = line.split("=")            
            rateDict[parsed[0]] = parsed[1].rstrip("\n")            
        return rateDict
    
    def inv_ex_rates():
        with open('Currencypairs.txt') as f:
            lines = f.readlines()
        
        invrateDict ={}
                
        for line in lines:
#            line = 'USDJPY=119.95\n'
            parsed = line.split("=")
            f= parsed[0][:3]
            l= parsed[0][3:]
            val = parsed[1].rstrip("\n")
#            invrateDict[l+f] = round(1/float(parsed[1].rstrip("\n")),len(val))
            invrateDict[l+f] = str(round(1/float(val),len(val)))
        return invrateDict
    
    def exchange_rate(currencypair):
        rateDict = CurrencyPairs.ex_rates()
#        if(rateDict == None):
#            raise Exception("Rate not found")
        return rateDict.get(currencypair)
    
    def inv_exchange_rate(currencypair):
        invrateDict = CurrencyPairs.inv_ex_rates()
#        print(invrateDict.get(currencypair))
#        if(invrateDict == None):
#            raise Exception("Rate not found")
        
        return invrateDict.get(currencypair)
    


    
        
    

        
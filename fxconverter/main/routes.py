# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 02:00:45 2020

@author: routm1
"""

from flask import Blueprint, render_template, flash
from fxconverter.model.forms import InputDataForms
from fxconverter.model.currencyconvertr import CurrencyConvert
import decimal
#from fxconverter.logger import logger

main = Blueprint("main", __name__, template_folder="templates")

@main.route('/', methods=['GET', 'POST'])
def home():
    forms = InputDataForms()
    if forms.validate_on_submit():
        base = forms.base.data
        currency = forms.currency.data
        quantity = forms.quantity.data
#        print('You entered from currency {} to currency {} and amount {}'.format(base,currency,quantity))       
        if (base != currency):              
            total= decimal.Decimal(quantity) * decimal.Decimal(CurrencyConvert.get_rate(base,currency))           
            
            if(total == 0):
                flash("Unable to find rate for {}/{}".format(base, currency))
        else:
            total = quantity
            
        if(currency != 'JPY'):
            flash("{} {} = {:.2f} {}".format(quantity, base, total, currency))
        else:
            flash("{} {} = {:.0f} {}".format(quantity, base, total, currency))
            
    return render_template('home.html', form=forms)

#@cache.cached(300)

        
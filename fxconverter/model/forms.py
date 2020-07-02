# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 01:34:29 2020

@author: routm1
"""

from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from fxconverter.controler.currencymap import CrossCurrency

def length_validate(form,field):
    if len(str(field.data)) > 10:
        raise ValidationError('Amount field must be less than 10 characters')

class InputDataForms(FlaskForm):
    
#    curr = CrossCurrency.get_currencyname()
    curr = list(CrossCurrency.get_currencyname())
    
    choice = []
    
    for i in curr:
        tpl =(i,i)
        choice.append(tpl)
    base = SelectField('base', choices=choice, validators=[DataRequired()])
    currency = SelectField('currency', choices=choice, validators=[DataRequired()])
    quantity = FloatField(f'Enter amount to convert', validators=[DataRequired(),length_validate])
#    quantity = FloatField(f'Enter amount to convert', validators=[Length(max=10)])
    
    submit = SubmitField('Calculate')


    
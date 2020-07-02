# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 16:54:51 2020

@author: routm1
"""

import os
from flask import Flask
#from healthcheck import HealthCheck, EnvironmentDump
from fxconverter.config import config



app = Flask(__name__)
config_name = os.getenv("FLASK_CONFIGURATION", "default")
app.config.from_object(config[config_name])
app.config.from_pyfile("config.cfg", silent=True)


if __name__ == "__main__":
    print("in check")
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)))
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:30:45 2020

@author: routm1
"""
import os
import logging, sys
from flask_compress import Compress



class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "1d94e52c-1c89-4515-b87a-f48cf3cb7f0b"
    LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOGGING_LOCATION = "converter.log"
    LOGGING_LEVEL = logging.INFO
    CACHE_TYPE = "simple"
    PORT = "5002"
    COMPRESS_MIMETYPES = [
        "text/html",
        "text/css",
        "text/xml",
        "application/json",
        "application/javascript",
    ]
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500


#class Config(object):
#    PORT = '5000'
#    LOG_LEVEL = 'CRITICAL'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = "development"
    SECRET_KEY = "a9eec0e0-23b7-4788-9a92-318347b9a39f"

class ProductionConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = "prodduction"
    SECRET_KEY = "8c0caeb1-6bb2-4d2d-b057-596b2dcab18e"
    
    
config = {
    "dev": "fxconverter.config.DevelopmentConfig",
    "prod": "fxconverter.config.ProductionConfig",
    "default": "fxconverter.config.DevelopmentConfig",
}

def configure_app(app):
    config_name = os.getenv("FLASK_CONFIGURATION", "default")
    app.config.from_object(config[config_name])
    app.config.from_pyfile("config.cfg", silent=True)
    # Configure logging
    handler = logging.FileHandler(app.config["LOGGING_LOCATION"])
    handler.setLevel(app.config["LOGGING_LEVEL"])
    formatter = logging.Formatter(app.config["LOGGING_FORMAT"])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    # Configure Compressing
    Compress(app)
    
def configure_consol_app(app):
    config_name = os.getenv("FLASK_CONFIGURATION", "default")
    app.config.from_object(config[config_name])
    app.config.from_pyfile("config.cfg", silent=True)
    # Configure logging
    chandler = logging.StreamHandler(sys.stdout)
    chandler.setLevel(app.config["LOGGING_LEVEL"])
    cformatter = logging.Formatter(app.config["LOGGING_FORMAT"])
    chandler.setFormatter(cformatter)
    app.logger.addHandler(chandler)
    # Configure Compressing
    Compress(app)
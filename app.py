# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:59:27 2020

@author: routm1
"""

from fxconverter import app
from gevent.pywsgi import WSGIServer

app.config["DEBUG"]= True
app.config["SECRET_KEY"] = 'asfet51354235'

if __name__ == "__main__":
#    print('enviroment')
#    
#    if app.config["ENV"] == "development":
#        app.config.from_object("config.ProductionConfig")
#        http_server = WSGIServer(('', 8080), app)
#        http_server.serve_forever()
#    else:
#        app.config.from_object("config.DevelopmentConfig")

    print(f'ENV is set to: {app.config["ENV"]}')
    app.run()
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:57:37 2020

@author: routm1
"""

from flask import Flask
from fxconverter.main.routes import main
from fxconverter.utills import get_instance_folder_path
from fxconverter.config import configure_app, configure_consol_app

#app = Flask(
#    __name__,
#    instance_path=get_instance_folder_path(),
#    instance_relative_config=True,
##    template_folder="templates",
#)
#
#configure_app(app)


app = Flask(__name__, instance_relative_config=True)
app.config.from_object("fxconverter.config.DevelopmentConfig")
port = app.config["PORT"]
app.config["DEBUG"] = True

server_name = "127.0.0.1:" + port
app.config["SERVER_NAME"] = server_name



#configure_consol_app(app)
#
#@app.errorhandler(404)
#def page_not_found(error):
#    current_app.logger.error("Page not found: %s", (request.path, error))
#    return render_template("404.htm"), 404
#
#@app.errorhandler(Exception)
#def unhandled_exception(error):
#    current_app.logger.error("Unhandled Exception: %s", (error))
#    return render_template("500.htm"), 500

#@app.context_processor
#def inject_data():
#    return dict(user=current_user, lang_code=g.get("lang_code", None))

app.register_blueprint(main)
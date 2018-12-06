# -*- coding: utf-8 -*-
"""
Created on Thu Dec 06 07:31:11 2018

@author: 006258
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ =="__main__":
    app.route(host="172.31.1.102")
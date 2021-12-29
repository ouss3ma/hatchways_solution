# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 12:23:22 2021

@author: ouss3ma
"""

from flask import Flask


from endpoints.posts import posts_api 
from endpoints.ping import ping_api



app = Flask(__name__)




app.register_blueprint(ping_api) 
app.register_blueprint(posts_api) 



if __name__ == '__main__':
    app.run(debug=False)
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:29:11 2021

@author: ouss3ma
"""

from flask import Blueprint, Flask, request, jsonify

ping_api = Blueprint('ping_api', __name__) 


@ping_api.route("/api/ping")
def ping():
    resp = jsonify({"success": "true"})
    resp.status_code = 200
    return resp
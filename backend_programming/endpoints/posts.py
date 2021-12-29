# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:30:11 2021

@author: ouss3ema
"""
import flask
from flask import Blueprint, jsonify
import requests
import sys


class sortBy_not_valid(Exception):
    pass

class direction_not_valid(Exception):
    pass

class tag_not_valid(Exception):
    pass

posts_api = Blueprint('posts_api', __name__) 




def get_data(tags):
    data ={'posts':[]}
    for tag in tags:  
        res = requests.get("https://api.hatchways.io/assessment/blog/posts?tag="+tag)
        try:
            if not res.json()['posts']:
                raise tag_not_valid
        except tag_not_valid:
            resp = jsonify({'error':"tags parameter is invalid"})
            resp.status_code = 400
            return resp
        data['posts'] += res.json()['posts']
    #remove duplication
    data['posts']=[k for j, k in enumerate(data['posts']) if k not in data['posts'][j + 1:]]
    return data

@posts_api.route("/api/posts")
def posts():
    
    acceptable_sortBy = ['id', 'reads', 'likes', 'popularity']
    acceptable_direction = ['desc', 'asc']
    
    tags = flask.request.args.get('tag', default=None, type = str)
    try:
        if  tags is None:
            raise tag_not_valid
    except tag_not_valid:
        resp = jsonify({'error':"Tags parameter is required"})
        resp.status_code = 400
        return resp
        
    tags = tags.split(',')
    sortBy = flask.request.args.get('sortBy', default='id', type = str)
    direction = flask.request.args.get('direction', default='asc', type = str)
    try:
        if sortBy not in acceptable_sortBy:
            raise sortBy_not_valid
        elif direction not in acceptable_direction:
            raise direction_not_valid
    except sortBy_not_valid:
        resp = jsonify({'error':"sortBy parameter is invalid"})
        resp.status_code = 400
        return resp
    except direction_not_valid:
        resp = jsonify({'error':"direction parameter is invalid"})
        resp.status_code = 400
        return resp    
    #print(tags, file=sys.stderr)
    
    data= get_data(tags)  
    
    #sort json object
    if direction == 'asc':
        data['posts'].sort(key=lambda x: x[sortBy])
    else:
        data['posts'].sort(key=lambda x: x[sortBy], reverse=True)
    resp = jsonify(data)
    resp.status_code = 200
    return resp

    
    
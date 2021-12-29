# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:58:22 2021

@author: ouss3ma
"""
import unittest
import json

import os, sys

p = os.path.abspath('.')
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app import app

class ApiTest(unittest.TestCase):
    
        
    #check for reponse 200 /posts
    def test_posts_status(self):
        tester = app.test_client(self)
        response = tester.get('/api/posts?tag=tech')
        print(response)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        
    #checkif the content return is application/json /posts    
    def test_posts_type(self):
        tester = app.test_client(self)
        response = tester.get('/api/posts?tag=tech')
        self.assertEqual(response.content_type, "application/json")
        
    #checkif the content return when tag is missing /posts    
    def test_posts_content(self):
        tester = app.test_client(self)
        response = tester.get('/api/posts')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['error'], "Tags parameter is required")
        
if __name__ == "__main__":
    unittest.main()
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:05:53 2021

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
    
    #check for reponse 200 /ping
    def test_ping(self):
        tester = app.test_client(self)
        response = tester.get('/api/ping')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        
if __name__ == "__main__":
    unittest.main()
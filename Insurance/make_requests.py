# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 07:51:29 2021

@author: rajat
"""

import requests 

# url
# URL = 'http://127.0.0.1:5000/predict'
URL = 'http://localhost:3000/predict'
# headers
headers = {"Content-Type": "application/json"}

# data input
data_in = [49, 'male', 21, 'yes',  'northwest', 2]

# make post request and print response
r = requests.post(URL, json={'input': data_in})

print("Charges: $ {:.2f}".format(r.json()))
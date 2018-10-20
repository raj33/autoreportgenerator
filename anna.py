# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:58:18 2018

@author: Admin
"""

from bs4 import BeautifulSoup
#import numpy as np

import requests
url = "http://45.114.246.190/admin/all_Location_details.aspx"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

table = soup.find( "table" )
data = []
rows=list()
for row in table.findAll("tr"):
   cols = row.find_all('td')
   cols = [ele.text.strip() for ele in cols]
   data.append([ele for ele in cols if ele])
   
print(data[2]) 
print(data[5])   
  
   
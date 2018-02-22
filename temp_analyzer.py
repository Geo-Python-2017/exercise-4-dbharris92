# -*- coding: utf-8 -*-
"""
A script using fahrToCelsius function and tempClassifier function
to convert Fahrenheit values to Celsius, and classify Celsius temperatures
into four (0:3) categories

2.21.18

db harris
"""

###import temperature values from data.py

from data import tempData as tD

###import functions from functions

from functions import fahrToCelsius as fTC
from functions import tempClassifier as tC 

###create an empty list for temp class numbers

tempClasses = []

###iterate through tempData
for t in tD:
###convert to Celsius and classify
    tempCelsius = fTC(t)
    tempClass = tC(tempCelsius)
    
###add classified temperatures to tempClasses list    
    tempClasses.append(tempClass)

###count and print zeroes, ones, twos, threes in tempClasses list
print("There are", tempClasses.count(0), "zeros.")
print("There are", tempClasses.count(1), "ones.")
print("There are", tempClasses.count(2), "twos.")
print("There are", tempClasses.count(3), "threes.")

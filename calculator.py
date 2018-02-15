# -*- coding: utf-8 -*-
"""
A script with a single function to convert
between Kelvins to Celsius and Fahrenheit

For Geo-Python Lesson 4

Drew Harris
2.15.18
"""

from tempConverter import celsiusToFahr
import tempConverter

def tempCalculator(tempK, convertTo):
    """
    Function for converting Kelvins to Celsius and Fahrenheit
    
    Parameters
    ----------
    tempK: <numerical>
        Temperature in Kelvins
    convertTo: <str>
        Temperature in Celsius (C) or Fahrenheit (F)
    
    Returns
    ----------
    <float>
        Converted temperature
    """    
    
   #check if convering to Celsius 
    if convertTo == "C":
        #convert to Celsius using tempConverter function
        convertedTemp = kelvinsToCelsius(tempKelvins = tempK)
    elif convertTo == "F":
        #convert to Fahrenheit
        convertedTemp = kelvinsToFahr(tempKelvins = tempK)
    return convertedTemp
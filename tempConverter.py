# -*- coding: utf-8 -*-
"""
This script contains functions to convert temperatures
from C, F, and Kelvins

Drew Harris 2.15.18
"""
###define functions###
def celsiusToFahr(tempCelsius):
    return 9/5 * tempCelsius + 32

def kelvinsToCelsius(tempKelvins):
    return tempKelvins - 273.15

def kelvinsToFahr(tempKelv):
    tempCelsius = kelvinsToCelsius(tempKelv)
    tempFahr = celsiusToFahr(tempCelsius)
    return tempFahr

###end functions###
    
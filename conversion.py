# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:20:14 2020

@author: Anthony Sánchez
"""


def l100kmtompg(liters):
    return (100*3.785411784*1000/liters*1609.344)
def mpgtol100km(miles):
    return (100/(miles*1.609344/3.785411784))
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
    
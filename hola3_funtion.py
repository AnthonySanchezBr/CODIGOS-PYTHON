# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:53:14 2020

@author: Anthony Sánchez
"""


def hola3(mylist):
    for a in mylist:
        print("Hola !",a)
        return mylist
    hola3(["Juan","Carlos","Pedro"])
    print(hola3("Juan","Carlos","Pedro","Sandra","monica"))
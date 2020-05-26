# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:10:24 2020

@author: Anthony Sánchez
"""

while True:
    x=input("Ingrese q o quit: ")
    
    if x=='q' or x=='quit':
        break
        x=int(x)
        y=1
        while True:
            print(y)
            y=y+1
            if y>x:
                break


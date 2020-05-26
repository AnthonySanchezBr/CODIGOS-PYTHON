# -*- coding: utf-8 -*-
"""
Created on Thu May  7 07:52:09 2020

@author: Anthony Sánchez
"""

switches=[]
devices=["R1","R2","R3","S1","S2"]

for item in devices:
    if "S" in item:
        switches.append(item)
        print(switches)
        
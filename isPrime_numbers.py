# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:16:50 2020

@author: Anthony Sánchez
"""
def isPrime(num):

     for i in range (2,num+1):
        if (num%i==0):
            if i==num:
               	return True 
            else:
                return False
                break

for i in range(1, 20):

                if isPrime(i + 1):

                   print(i + 1, end=" ")

print()



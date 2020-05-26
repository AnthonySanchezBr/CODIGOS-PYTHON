# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:13:27 2020

@author: Anthony Sánchez
"""
def isPrime(n):

     for i in range (2,n+1):
        if (n%i==0):
            if i==n:
               	return True 
            else:
                return False
                break

for i in range(1, 20):

                if isPrime(i + 1):

                   print(i + 1, end=" ")

print()


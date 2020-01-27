#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 21:40:22 2020

@author: davidfauzi
"""
#example : January 11, 2020 at 07:33PM 
timeinput=input()
print(timeinput)
_,_,_,_,time=timeinput.split()
print(time)
time=time[:-2]+":00 "+time[-2:]
print(time)
# Python program to convert time 
# from 12 hour to 24 hour format 
  
# Function to convert the date format 
def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 
  
# Driver Code         
out=convert24(time)
print(out)  

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:18:42 2018

@author: Cindy
"""

print ("Home is where the heart is. Do you agree?")
user_input = input("Type yes or no: ")
finished = "yes" or "no"

while finished:

  if user_input =="no":
    print ("You are a cold fish. Go find some love.")
    break
    
  elif user_input == "yes":
    user_input2 = input("Who do you love? ")
    print ("Your home is with " + str(user_input2 +"."))
    break
   
  else:
    user_input = input("I do not understand. Type yes or no. ")


    
print ("This is the meaning of life.") 

'''
author ag abhijith
date oct 19 2024
description :a Python program that performs the following tasks:
Create, concatenate, and print a string and access a sub-string from a given string.
'''
first_name = input("Enter your first name")
last_name  = input("enter your last name")
name=first_name+" "+last_name
print(name)
first_name_length = len(first_name)
print(first_name_length)
last_string=name[:first_name_length]
print(last_string)

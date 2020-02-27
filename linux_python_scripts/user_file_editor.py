#!/usr/bin/env python3.6
"""
Description: Pythos script that calls the user to provide a path and filename and Keeps adding text into seperate lines until an empty string is provided 
Author: Mateusz Maly
Email: mateuszfmaly@gmail.com
github: matmaly

"""

with open(input("Enter an absoulte path to file and a new filename "), "w") as f:
    user_input = input()
    while user_input != "":
        f.write(user_input)
        f.write("\n")
        user_input = input()


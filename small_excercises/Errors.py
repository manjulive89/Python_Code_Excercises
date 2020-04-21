#!/usr/bin/env python3

def problem1():
    try:
        for i in ["a","b","c"]:
            print(i**2)
    except TypeError:
        print("Strings instead of Ints")

def problem2():
    x = 5
    y = 0
    try:
        z = x / y
    except ZeroDivisionError:
        print("Can't divide by 0")
    finally:
        print("All done")

def problem3():
    while True:
        try:
            user_input = int(input("Enter a number: "))
        except:
            print("Please provide ints only")
        else:
            result = user_input **2
            print(f"{user_input} squared is: {result}")
            break
problem1()
problem2()
problem3()

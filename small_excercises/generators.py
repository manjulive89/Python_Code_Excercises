#!/usr/bin/env python3
'''
yield is used instead of a return
that way you don't have to save into memory and occupy it
Use it if you want to generate something once for example and it's big
'''
def gen(n):

    for x in range(n):
        yield x * 2

# Followin for loop prints the numbers that were yielded by the function, otherwise print points to the object in memory
#for number in gen(10):
#    print(number)

#g = gen(5)

# Next keyword is used to iterate through the yielded values, it's not holding everythin in memory. It remembers which one it called before.
# ints only

#print(next(g))
#print(next(g))

#s = "hello"

# iter() fun allows for strings to be iterated with the next()
#s_iter = iter(s)

# following will print h and e 
#print(next(s_iter))
#print(next(s_iter))

# Print squares of numbers up to N using a generator
def problem1(n):
    for x in range(n):
        yield x ** 2

for number in problem1(10):
    print(number)
print("\n")

# generator which takes in low and high values and then assigns a random number between 1 and 10 to n, then yields 'n' random numbers between low and high
def problem2(low, high):
    import random

    n = random.randint(1,10)

    for x in range(n):
        yield random.randint(low,high)

for number in problem2(5,8):
    print(number)

print("\n")

# Following shows iter() fun which converts the string into an iterator
s = "hello"
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

print("\n")
'''
Generator Comprehension:
(<expression> for <var> in <iterable> if <condition>)

'''
even_gen = (i for i in range(11) if i % 2 ==0)

for number in even_gen:
    print(number)





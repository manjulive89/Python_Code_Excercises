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
for number in gen(10):
    print(number)

g = gen(5)

# Next keyword is used to iterate through the yielded values, it's not holding everythin in memory. It remembers which one it called before.
# ints only

print(next(g))
print(next(g))

s = "hello"

# iter() fun allows for strings to be iterated with the next()
s_iter = iter(s)

# following will print h and e 
print(next(s_iter))
print(next(s_iter))


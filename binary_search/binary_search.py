#!/usr/bin/env python3.6

'''
My Attempt at a binary search algorithm using oo
'''

import random

class Binary_Search:
    def __init__(self):	    
        self.list_to_search = []

    def generate_list(self):
        self.list_to_search = random.sample(range(101), 50)
        self.list_to_search.sort()
        print(self.list_to_search)
		
    def search_list(self,to_find):
        element = False
        while not element:
            half_point = len(self.list_to_search) // 2
            if len(self.list_to_search) == 1:
                if to_find == self.list_to_search[0]:
                    print(self.list_to_search)
                    element = True
                else:
                    print("Element not in the List")
                    element = True
            elif to_find >= self.list_to_search[half_point]:
                del self.list_to_search[:half_point]
            elif to_find < self.list_to_search[half_point]:
                del self.list_to_search[half_point:]

search = Binary_Search()
search.generate_list()
search.search_list(20)	

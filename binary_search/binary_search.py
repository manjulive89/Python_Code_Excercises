#!/usr/bin/env python3.6

'''
My Attempt at a binary search algorithm using oo
'''

import random

class Binary_Search:
	def __init__(self):
		self.list_to_search = []

	def generate_list(self):
		self.list_to_search = random.sample(range(101), 101)

	def search_list(self):
		print(self.list_to_search)



search = Binary_Search()
search.generate_list()
search.search_list()	

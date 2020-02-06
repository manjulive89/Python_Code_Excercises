#!/usr/bin/env python3.6

'''
My Attempt at a binary search algorithm using oo
'''

import random

class Binary_Search:
	def __init__(self):
		self.list_to_search = []

	def generate_list(self):
		self.list_to_search = random.sorted(sample(range(101), 101))
		print(self.list_to_search)
		
	def search_list(self,to_find):
		element = False
		while not element:
			half_point = len(self.list_to_search) // 2
			if to_find == self.list_to_search[half_point]:
				print(f"Found at position: {self.list_to_search.index(half_point)}")
				break
			elif to_find > self.list_to_search[half_point]:
				print("More")
			elif to_find < self.list_to_search[half_point]:
				print("Less"
			else:
				break 	
		print(half_point)


search = Binary_Search()
search.generate_list()
search.search_list()	

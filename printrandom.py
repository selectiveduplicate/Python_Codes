#this program imports the random module 

import random

print('These are random integers-')

for i in range(5):
	print(random.randint(1, 5))	#print random integers between 1 and 10

print('These are random floating point numbers-')

for i in range(5):
	print(random.uniform(1, 5))	#print random floating point numbers between 1 and 5
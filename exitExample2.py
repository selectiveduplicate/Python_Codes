#this program uses the sys module to exit out of an infinite loop

import sys

while True:
	print('Type your name')
	response = input()

	if response == 'exit':
		sys.exit()

	print('You typed ' + response + '.')
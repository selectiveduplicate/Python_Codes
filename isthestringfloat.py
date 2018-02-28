take = input()

try:
    float(take)
except ValueError:
	print('Not a float!')
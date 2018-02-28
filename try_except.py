a = input()

try:
	int(a)
except ValueError:
	print("Not an integer, got to be a float, see for yourself-", a)
print("It's an integer-", a)
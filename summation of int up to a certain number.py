#this program sums up integers up to a certain given number

print("Enter the number you want to sum up to-")
givenint = input()
start = 1
result = 0

while start <= int(givenint):
	result = result + start
	start = start + 1

print('The summation up to ' + str(givenint) + ' is' + ' result')
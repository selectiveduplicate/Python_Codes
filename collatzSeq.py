# explores the Collatz sequence, as per on page 77 of Automate the Boring Stuff

# defining the function


def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 != 0:
        return 3*number + 1

# input only takes place once


print("Enter number")
numb = int(input())

param = True


# our function will be called continuously until it returns 1

while param:
    res = collatz(numb)
    print(res)
    if res == 1:
        param = False
    numb = res


def number(a, b):
    print(a + b)


print(" ")

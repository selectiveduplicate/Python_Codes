# this program sums up integers up to a certain given number

negative = True  # these two controls the main loop of taking input and summing up
floating = True

while negative and floating:  # assume inputs r negative, need to keep coming back here unless an integer
    print("Enter the number you want to sum up to-")
    givenint = input()

    b = float(givenint)
    a = int(b)  # int can't convert to integer and decode it from string at the same time

    start = 1
    result = 0

    if a == b:
        if a < 0:  # a equals b means it's an integer
            print("That's a negative number, please enter an integer number...")
            negative = False  # neg so don't sum

        while (negative and start <= int(givenint)):
            result = result + start
            start = start + 1

    if b > a:
        floating = False  # b > a means it's a floating number, so we gotta do something so that it's not summed
        print('That is a floating number, enter an integer...')

    if negative and floating:  # if all tests r passed, these two var should remain true, so summing is legit
        print('The summation up to ' + str(givenint) + ' is ' + str(result))
        negative = False
        floating = False
        continue

    negative = True  # if not all tests are passed, we need to start all over again
    floating = True

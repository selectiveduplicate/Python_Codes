# this program shows exception handling- how to handle errors so that a program doesn't crash


def spam(divideBy):

    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')


print(spam(2))
print(spam(3))
print(spam(0))
# print(spam(43))
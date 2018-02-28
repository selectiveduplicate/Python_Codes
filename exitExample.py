import sys

while True:
    print('Type "I want to get out of this" to exit...')
    response = input()
    if response == 'I want to get out of this':
        sys.exit()
        print("Voila! You're out!")
    else: print('You wanna get out? Then tell me so!')
    print('You typed ' + response + ' which is nothing that matters!')

import sys, os
from users import run_user_menu
from mongoengine import *

connect('posts_test')


def get_user_op():
    print('\n>>> What would you like to do ?')
    print('')
    print('1. Add/search/remove users')
    print('2. Add/search/remove posts')
    print('3. Quit')
    print('')
    return input('Enter number: ')

os.system('clear')

while True:
    op = get_user_op()

    if op == '1':
        run_user_menu()
    elif op == '2':
        os.system('clear')
        print('Coming soon...')
    elif op == '3':
        os.system('clear')
        print('Bye 👋🏻')
        sys.exit(0)
    else:
        os.system('clear')
        print('Unknown code')

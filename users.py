import sys
import os
from mongoengine import *
from schemas import User


def get_user_op():
    print('\n>>> Select one')
    print('')
    print('1. Add new user')
    print('2. List users')
    print('3. Search users')
    print('4. Remove users')
    print('5. Back')
    print('6. Quit')
    print('')
    return input('Enter number: ')


def add_user():
    os.system('clear')
    email = input('Enter email: ')
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    new_user = User(email=email, first_name=first_name,
                    last_name=last_name).save()
    print('\nSaved...')


def list_users(user_array=None):
    os.system('clear')
    print('---------------')
    for user in (user_array or User.objects):
        print(f"{user.id} | {user.first_name} {user.last_name} | {user.email}")
    print('---------------')


def search_users():
    os.system('clear')
    query = input('Enter search query: ')
    results = User.objects(
        Q(email__icontains=query) |
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query)
    )
    list_users(results)


def remove_user():
    os.system('clear')
    delId = input('Enter id: ')
    try:
        item = User(id=delId)
        item.delete()
        print('Deleted.')
    except:
        print('User cannot be deleted.')


def run_user_menu():
    os.system('clear')
    while True:
        op = get_user_op()
        if op == '1':
            add_user()
        elif op == '2':
            list_users()
        elif op == '3':
            search_users()
        elif op == '4':
            remove_user()
        elif op == '5':
            os.system('clear')
            break
        elif op == '6':
            os.system('clear')
            print('Bye 👋🏻')
            sys.exit(0)
        else:
            os.system('clear')
            print('Unknown code')

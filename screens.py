import os
import sys


def display_intro_screen(filename):
    new_file = open(filename)
    intro_screen = new_file.read()
    os.system('clear')
    print(intro_screen)
    decide_which_action()


def decide_which_action():

    try:
        user_choice = int(input('Press key: '))
    except ValueError:
        print('Enter only a number')
    else:
        if user_choice in (1, 2, 3, 4):       
            if user_choice == 1:
                return True
            elif user_choice == 2:
                os.system('clear')
                display_how_to_play()
            elif user_choice == 3:
                os.system('clear')
                display_about_authors()
            elif user_choice == 4:
                os.system('clear')
                display_story()
        else:
            print('Wrong number')


def go_back_to_menu():
    input('Press button: ')
    os.system('clear')
    display_intro_screen('introduction.txt')


def display_how_to_play():
    new_file = open('how_to_play.txt')
    how_to_play_screen = new_file.read()
    print(how_to_play_screen)
    go_back_to_menu()


def display_about_authors():
    new_file = open('about_authors.txt')
    how_to_play_screen = new_file.read()
    print(how_to_play_screen)
    go_back_to_menu()


def display_story():
    new_file = open('story.txt')
    story_screen = new_file.read()
    print(story_screen)
    go_back_to_menu()


def display_win_screen(inventory):
    new_file = open('win.txt')
    win_screen = new_file.read()
    os.system('clear')
    print(win_screen)
    inventory_items = ""
    for k, v in inventory.items():
        inventory = ("".join(' {}:{} '.format(k, v)))
        inventory_items += str(inventory)
    print("You win this game with inventory:  ", inventory_items, '\n\n')
    sys.exit()
    
    
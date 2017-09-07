import sys
import os
import random

import boss_game
import screens


def get_board_from_file(file_name):
    with open(file_name) as f:
        read_data = f.read()
    read_data = read_data.strip()
    board = read_data.split("\n")
    for i in range(len(board)):
        board[i] = list(board[i])
    return board


def print_board(board):
    for line in board:
        line.append('\n')
    for i in range(len(board)):
        board[i] = ''.join(board[i])
        board[i] = board[i]
    board = ''.join(board)
    print(board)


def change_hero_position(x, y, ch, board):
    new_x = x
    new_y = y
    if ch == 'w':
        new_x -= 1
    if ch == 's':
        new_x += 1
    if ch == 'a':
        new_y -= 1
    if ch == 'd':
        new_y += 1
    if ch == 'z':
        sys.exit()

    if board[new_x][new_y] in ('#', '~', '1'):
        new_x = x
        new_y = y

    return new_x, new_y


def fight_mode(board, x, y, user_health):

    print('you will fight with enemy in the dice game!!!')
    enemy_health = 30
    fight_counter = 0
    while user_health > 0 and enemy_health > 0:
        user_dice_number = random.randint(1, 6)
        enemy_dice_number = random.randint(1, 6)
        if user_dice_number > enemy_dice_number:
            enemy_health -= 10
            fight_counter += 1
        if user_dice_number < enemy_dice_number:
            user_health -= 5
            fight_counter += 1

    if enemy_health == 0:
        print('You win with enemy in', fight_counter, 'rounds')
        return user_health


def add_character_to_board(sign, board, x, y):
    board[x][y] = sign
    return board


def add_items_to_board(board, hero_health, inventory, hugs):
    add_character_to_board('e', board, 4, 10)
    add_character_to_board('e', board, 10, 40)
    add_character_to_board('e', board, 16, 50)
    add_character_to_board('e', board, 10, 8)
    #add_character_to_board('hp = ' + str(hero_health), board, 20, 1)
    #add_character_to_board('Inventory: ' + inventory, board, 20, 10)
    if hugs > 30:
        for i in range(5, 10):
            for j in range(60, 65):
                add_character_to_board('R', board, i, j)
    return board


def print_inventory(inventory):
    inventory_items = ""
    for k, v in inventory.items():
        inventory = ("".join(' {}:{} '.format(k, v)))
        inventory_items += str(inventory)
    return inventory_items


def check_lose_game(hero_health):
    if not hero_health:
        os.system('clear')
        print_lose_board()


def print_lose_board():
    new_file = open('lose.txt')
    lose_screen = new_file.read()
    print(lose_screen)
    sys.exit()


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def hot_cold_warm():
    print("fight with Great Rydz")


def main():
    screens.display_intro_screen('introduction.txt')

    hero_health = 100
    inventory = {'Vacuum': 0, 'Tubbies Cream': 0, 'Hugs': 0}
    hugs = inventory['Hugs']
    if hugs < 14:
        file_name = 'lev1.txt'
        x = 1
        y = 30
    else:
        file_name = 'lev2.txt'
        x = 30
        y = 1

    inventory_items = print_inventory(inventory)
    board = get_board_from_file(file_name)

    board_with_enemies = add_items_to_board(board, hero_health, inventory_items, hugs)
    board_with_characters = add_character_to_board('\033[1;32m@\033[1;m', board, x, y)
    os.system('clear')
    print_board(board_with_characters)
    print('{}{}'.format("hp = ", hero_health))
    print('{}{}'.format("inventory", print_inventory(inventory)))
    print('_' * 72)

    while True:
        ch = getch()

        hugs = inventory['Hugs']
        if hugs < 14:
            file_name = 'lev1.txt'
        else:
            file_name = 'lev2.txt'

        board = get_board_from_file(file_name)
        x, y = change_hero_position(x, y, ch, board)


        if board_with_characters[x][y] == 'e':
            hero_health = fight_mode(board, x, y, hero_health)
            check_lose_game(hero_health)
            inventory['Hugs'] += 3
            inventory['Tubbies Cream'] += random.randint(0,2)
            inventory_items = print_inventory(inventory)
        elif board_with_characters[x][y] == 'R':
            if boss_game.main():
                screens.display_win_screen(inventory)
            else:
                print_lose_board()

        else:
            board_with_characters = add_character_to_board('\033[1;32m@\033[1;m', board, x, y)
            board_with_all_characters = add_items_to_board(board_with_characters, hero_health, inventory_items, hugs)

            os.system('clear')
            print_board(board)
            print('{}{}'.format("hp = ", hero_health))
            print('{}{}'.format("inventory", print_inventory(inventory)))
            print("_" * 72)

        if inventory['Tubbies Cream'] > 4:
            hero_health = 100
            inventory['Tubbies Cream'] = 0
            print('***Tubbies Cream restore your life***')


if __name__ == '__main__':
    main()

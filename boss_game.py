import random
import os


def get_random_digits():
    correct_answer = []
    while len(correct_answer) < 3:
        digit = random.randint(0, 9)
        if digit not in correct_answer:
            correct_answer.append(digit)
    return correct_answer


def get_user_input():
    while True:
        user_guess = input("Enter number: ")
        if user_guess.isalpha():
            print("Enter only digits")
        elif len(user_guess) != 3:
            print("You have to enter exactly 3 digits!")
        else:
            return list(user_guess)


def compare_user_input_with_answer(user_guess, correct_answer):
    index = 0
    hint_list = []
    for a in correct_answer:
        if str(a) == user_guess[index]:
            hint_list.insert(0, 'HOT')
        elif str(a) in user_guess:
            hint_list.append("WARM")
        index += 1
    if not hint_list:
        hint_list.append("COLD")

    return hint_list


def check_result(hint_list):
    if hint_list == ["HOT"] * 3:
        return True


def main():
    os.system('clear')
    print("Fight with Great Rydz in Hot Cold Warm game")
    print("guess three digits number Great Rydz is thinking of")
    correct_answer = get_random_digits()
    tries_left = 10

    while tries_left > 0:

        user_guess = get_user_input()
        result = compare_user_input_with_answer(user_guess, correct_answer)
        print(result)
        if check_result(result):
            return True
        tries_left -= 1
    if tries_left == 0:
        return False


if __name__ == '__main__':
    main()

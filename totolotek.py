import random

def lotto():
    random_numbers = [random.randint(1, 50) for number in range(6)]

    user_choice = input("Enter your 6 numbers:")
    choice_list = list(user_choice)

    print (random_numbers, choice_list)
"""
    numbers_range = range(1,50)
    range_list = list(numbers_range)
    random_numbers = shuffle(range_list)
"""
lotto()
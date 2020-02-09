from random import shuffle

def lotto():
    user_choices = input("Enter your 6 numbers:").split()
    #user_choices = ['1','4','3','17','49', '12']
    #print(user_choices)
    correct_choices = []

    if len(user_choices) != 6:
        print("6 numbers should be given")
        return

    for i in range(len(user_choices)):
        try:
            choice = int(user_choices[i])
        except ValueError:
            print(user_choices[i],' is not a number')
            return
        #print(choice)

        if not choice in range(1,50):
            print(choice,'Is outside the range')
            return

        if choice in correct_choices:
            print(choice, ' is dubled value')
            return

        correct_choices.append(choice)


    correct_choices.sort()
    print (f'Your numbers: {correct_choices}')

    number_range = range(1, 50)
    numbers_list = list(number_range)
    random_numbers = shuffle(numbers_list)
    result = numbers_list[:6]
    result.sort()
    print (f'Random numbers: {result}')

    hit_count = 0
    hit_numbers = []
    for i in range(len(correct_choices)):
        if correct_choices[i] in result:
            hit_count += 1
            hit_numbers.append(correct_choices[i])
    print('You have ',hit_count,' hits:',hit_numbers)
lotto()


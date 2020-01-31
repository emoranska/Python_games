import random

def guess_number():
    guessed = False
    random_number = random.randint(1,100)

    while not guessed:
        user_number = input("Zgadnij liczbę: ")

        if user_number.isdigit(): #sprawdza, czy user_number można rzutować na liczbę
            user_number = int(user_number)
       # return your_number
            if user_number < random_number:
                print("Za mało!")
            elif user_number > random_number:
                print("Za dużo!")
            elif user_number == random_number:
                print("Zgadłeś!")
                guessed = True
        else:
            print("To nie jest liczba!")

guess_number()
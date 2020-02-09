
def guess_number_2(user_number):
    print('Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach')

    min = 0
    max = 1000
    guess = 500

    while guess != user_number:
        guess = int((max - min) / 2) + min
        print(f'Zgaduję: {guess}')

        if guess > user_number:
            max = guess
            print("Za dużo!")
        elif guess < user_number:
            min = guess
            print('Za mało!')

    print(f'Zgadłeś! {guess} było poprawną liczbą.')

guess_number_2(839)

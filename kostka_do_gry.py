import re

def dice(pattern):
    regex = r"^(\d*)([D])(3|4|6|8|10|12|20|100)([+|-]?)(\d*)"
    checking = re.search(regex, pattern)
    list_to_check = checking.groups()
    print (list_to_check)

    if checking != None:
        number_of_rolls = list_to_check[0]

        if number_of_rolls == '':
            number_of_rolls = 1

        dice_type = int(list_to_check[2])
        modifier = list_to_check[3]
        modifier_number = list_to_check[4]

        allowedTypes = (3, 4, 6, 8, 10, 12, 20, 100)

        if dice_type in allowedTypes:
            if modifier is '+':
                roll = int(number_of_rolls) * dice_type + int(modifier_number)
                return roll
            elif modifier is '-':
                roll = number_of_rolls * dice_type - int(modifier_number)
                return roll
            elif modifier is '':
                roll = number_of_rolls * dice_type
                return roll
    else:
        print("Bad dice pattern")

print(dice("D8"))
print(dice("D12-1"))
print(dice("2D10+10"))

import random

def __parse_roll(message):
    space_index = message.find(' ')
    d_index = message.find('d')
    plus_index = message.find('+')
    add_mod_to_all = False

    if plus_index == -1:
        plus_index = message.find('a')
        add_mod_to_all = True

    roll_list = []
    dice_count = int(message[space_index:d_index].strip())
    if plus_index != -1:
        dice_sides = int(message[d_index + 1:plus_index].strip())
    else:
        dice_sides = int(message[d_index + 1:].strip())
    total = 0

    for i in range (0, dice_count):
        curr_val = random.randint(1, dice_sides)
        total += curr_val
        roll_list.append(curr_val)

    plus_value = 0
    if plus_index != -1:
        plus_value = int(message[plus_index + 1:].strip())
        if add_mod_to_all:
            total = total + (plus_value * len(roll_list))
        else:
            total += plus_value

    return roll_list, plus_value, total, add_mod_to_all

def __get_roll_results(roll_list, plus_value, total, add_mod_to_all):
    if len(roll_list) == 0:
        return ", you didn't roll any dice, or you rolled literally air!"

    ret_string = '['
    for number in roll_list:
        ret_string = ret_string + str(number) + ' '

    ret_string = ret_string[:-1] + "]"

    if add_mod_to_all:
        ret_string = ret_string + " and with the mod applied to all rolls: "

        ret_string = ret_string + '['
        for number in roll_list:
            ret_string = ret_string + str(number + plus_value) + ' '

        ret_string = ret_string[:-1] + "]"
    else:
        if plus_value != 0:
            ret_string = ret_string + " + " + str(plus_value)

    ret_string = ret_string + ", for a total of " + str(total) + "."

    return ", you rolled " + ret_string

def get_roll_message(message, author):
    roll_list, plus_value, total, add_mod_to_all = __parse_roll(message)
    results = __get_roll_results(roll_list, plus_value, total, add_mod_to_all)
    return "<@" + str(author) + ">" + results

#TODO: Write Unit Tests
'''For Testing'''
if __name__ == '__main__':
    print(__parse_roll("!roll 3d2a7"))
    print(__get_roll_results([3, 3, 4, 1], 2, 3, True))
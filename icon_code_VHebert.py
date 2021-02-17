"""
Virginia Hebert
DAT129 - Python 2
Icon Creation Program
"""

import itertools
import os
import sys


def make_list():
    """create blank list"""
    user_numbers = []
    return user_numbers

def get_file(value_list):
    """get user's file of numbers or send to in-program input"""
    file_name = input("If you have a file with the list of numbers, please type in the name (including file type). \nIf there is no file, type 'none'. ")
    exists = os.path.isfile(file_name)
    str_values = ""
    if exists == True: # pull from file, if file is present
        with open(file_name, "r") as values:
            file_values = values.readlines()
            clean_list = []
            for line_end in file_values:
                clean_list.append(line_end.strip()) # strip newline character
            clean_list[:] = [''.join(clean_list[:])] # make one big list
            for values in clean_list: # convert to string
                str_values += values
            return str_values
    elif exists == False or file_name == "none": # break loop if no file or exit
        print() #aesthetic line
        print("We'll get the files in the program them.")
        return str_values

def user_input(values):
    """get user's list of numbers with a flag for not enough/too many values"""
    if len(values) == 0:
        user_numbers = input("Please give me one hundred 1s or 0s with no spaces, commas, or other characters: ")
        while len(user_numbers) != 100:
            if len(user_numbers) < 100:
                print("You haven't given me enough values.")
                more_needed = 100 - len(user_numbers) # determine how many more numbers are needed
                more_numbers = input("Please give me " + str(more_needed) + " more numbers: ")
                user_numbers = user_numbers + more_numbers # determine if there are enough
            elif len(user_numbers) > 100:
                print() #aesthetic line
                print("You've given me more than 100 values, so I'll just use the first 100.")
                return user_numbers
        else:
            print() #aesthetic line
            print("Just the right amount!")
            return user_numbers
    elif len(values) == 100:
        print() #aesthetic line
        print("Looks like the file has all we need!")
        return values
    elif len(values) < 100 and len(values) > 0:
        print() #aesthetic line
        print("The file doesn't have enough values in it. Please check and make sure there are 100 1s and/or 0s.")
        return sys.exit() # exit the program to fix the input file of numbers

def assign_characters(user_list, fill, empty):
    """assign a value to represent the 1 """
    swap_dict = {"1": fill, "0": empty}
    swap_values = user_list.maketrans(swap_dict)
    new_list = user_list.translate(swap_values)
    return new_list

def dbl_characters(user_list, fillfill, emptyempty):
    """assign 2x the characters per value assigned to 1"""
    swap_dict = {"1": fillfill, "0": emptyempty}
    swap_values = user_list.maketrans(swap_dict)
    new_list = user_list.translate(swap_values)
    return new_list

def list_of_lists(new_values):
    """break the full list down into a series of 10 value long lists"""
    listy_list = [new_values[i:i + 10] for i in range(0, len(new_values), 10)]
    return listy_list

def copy_list(user_list):
    """make a copy of the user list for wallpaper"""
    copied_list = []
    for x in range(len(user_list)):
        temp = []
        for sub_list in user_list[x]:
            temp.append(sub_list)
        copied_list.append(temp)
    return copied_list

def wallpaper_lists(original_list, copied_list):
    """create a zipped list of lists to print a wallpaper sytle design"""
    zip_list = [list(itertools.chain(*i))
       for i in zip(original_list, copied_list, original_list, copied_list, original_list, copied_list)]
    added_list = (3 * zip_list)
    return added_list

def print_pattern(many_lists):
    """print the list of lists into a pattern"""
    for a_list in many_lists:
        for character in a_list:
            print(character, end = "")
        print("", sep = "\n")
    
def supersize(fancy_values):
    """print out a 2x2 for each value pattern for the icon"""
    a = 0
    b = 20
    while b < 200:
        print(fancy_values[a:b])
        print(fancy_values[a:b])
        a = a + 20
        b = b + 20
        if b > 200:
            break

def pause():
    """insert a pause/break in the program"""
    program_pause = input("press the <ENTER> key")
    return program_pause

def main():
    """pull it all together with the appropriate verbage"""
    new_list = make_list()
    print() #aesthetic line
    print("Welcome to the icon creation extravaganza!")
    print() #aesthetic line
    print("If you can give me 100 1s or 0s, I can create a pattern on the screen using the values.")
    print("The 0s will be blank and the 1s will be 'filled'.")
    file_values = get_file(new_list)
    user_choice = user_input(file_values)
    print() #aesthetic line
    print("These are the values I'm going to use for the pattern: ")
    print(user_choice[:100])
    print() #aesthetic line
    icon1 = input("What character would you like to use for 1 (shaded)? ")
    icon0 = input("What character would you like to use for 0 (not shaded)? ")
    assigned_values = assign_characters(user_choice, icon1, icon0)
    print() #aesthetic line
    print() #aesthetic line
    print("Now to see the magic..."), pause()
    print() #aesthetic line
    all_the_lists = list_of_lists(assigned_values)
    print_pattern(all_the_lists)
    print() #aesthetic line
    print("And a little fancier...supersized"), pause()
    print() #aesthetic line
    double_1 = icon1 + icon1
    double_0 = icon0 + icon0
    assigned_values = dbl_characters(user_choice, double_1, double_0)
    supersize(assigned_values)
    print() #aesthetic line
    print("And fancier still...wallpaper"), pause()
    print() #aesthetic line
    second_list = copy_list(all_the_lists)
    repeat_lists1 = wallpaper_lists(all_the_lists, second_list)
    print_pattern(repeat_lists1)


if __name__ == "__main__":
    main()

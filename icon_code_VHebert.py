# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:39:51 2021
Virginia Hebert
DAT129 - Python 2
Icon Creation Program
"""

import itertools


def make_list():
    """create blank list"""
    user_numbers = []
    return user_numbers

def user_input():
    """get user's list of numbers with a flag for not enough/too many values"""
    user_numbers = input("Please give me one hundred 1s or 0s with no spaces, commas, or other characters: ")
    while len(user_numbers) != 100:
        if len(user_numbers) < 100:
            print("You haven't given me enough numbers.")
            values_needed = 100 - len(user_numbers)
            more_numbers = input("Please give me " + str(values_needed) + " more numbers: ")
            user_numbers = user_numbers + more_numbers
        elif len(user_numbers) > 100:
            print() #aesthetic line
            print("You've given me more than 100 values, so I'll just use the first 100.")
            return user_numbers
    else:
        print() #aesthetic line
        print("Just the right amount!")
        return user_numbers

def assign_characters(user_list, x):
    """assign a value to represent the 1 
    https://www.w3schools.com/python/ref_string_translate.asp
    https://www.w3schools.com/python/ref_string_maketrans.asp"""
    swap_dict = {"1": x, "0": " "}
    swap_values = user_list.maketrans(swap_dict)
    new_list = user_list.translate(swap_values)
    return new_list

def dbl_characters(user_list, xx):
    """assign 2x the characters per value assigned to 1"""
    swap_dict = {"1": xx, "0": "  "}
    swap_values = user_list.maketrans(swap_dict)
    new_list = user_list.translate(swap_values)
    return new_list

def list_of_lists(new_values):
    """break the full list down into a series of 10 value long lists
    https://www.geeksforgeeks.org/break-list-chunks-size-n-python/"""
    listy_list = [new_values[i:i + 10] for i in range(0, len(new_values), 10)]
    return listy_list

def copy_list(user_list):
    """make a copy of the user list for wallpaper
    https://www.geeksforgeeks.org/python-how-to-copy-a-nested-list/"""
    copied_list = []
    for x in range(len(user_list)):
        temp = []
        for sub_list in user_list[x]:
            temp.append(sub_list)
        copied_list.append(temp)
    return copied_list

def wallpaper_lists(original_list, copied_list):
    """create a zipped list of lists to print a wallpaper sytle design
    https://www.geeksforgeeks.org/python-zipping-two-lists-of-lists/"""
    zip_list = [list(itertools.chain(*i))
       for i in zip(original_list, copied_list, original_list, copied_list, original_list)] 
    added_list = zip_list + zip_list + zip_list
    return added_list

def print_pattern(many_lists):
    """print the list of lists into a pattern
    https://stackoverflow.com/questions/38872341/print-list-of-lists-in-separate-lines"""
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
    make_list()
    print() #aesthetic line
    print("Welcome to the icon creation extravaganza!")
    print() #aesthetic line
    print("If you can give me 100 1s or 0s, I can create a pattern on the screen using the values.")
    print("The 0s will be blank and the 1s will be 'filled'.")
    user_choice = user_input()
    print() #aesthetic line
    print("These are the values I'm going to use for the patern: ")
    print(user_choice[:100])
    print() #aesthetic line
    icon = input("What character would you like to use for 1? ")
    print() #aesthetic line
    print() #aesthetic line
    print("Now to see the magic..."), pause()
    print() #aesthetic line
    assigned_values = assign_characters(user_choice, icon)
    all_the_lists = list_of_lists(assigned_values)
    print_pattern(all_the_lists)
    print() #aesthetic line
    print("And a little fancier...supersized"), pause()
    print() #aesthetic line
    xx = icon+icon
    assigned_values = dbl_characters(user_choice, xx)
    supersize(assigned_values)
    print() #aesthetic line
    print("And fancier still...wallpaper"), pause()
    print() #aesthetic line
    second_list = copy_list(all_the_lists)
    repeat_lists1 = wallpaper_lists(all_the_lists, second_list)
    print_pattern(repeat_lists1)


if __name__ == "__main__":
    main()

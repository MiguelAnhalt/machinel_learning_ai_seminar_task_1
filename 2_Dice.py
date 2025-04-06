######################################################################
#                                                                    #
# Task 1.2: Introduction to Python: Running Make Dice on VS code     #
# Instructions:                                                      #
# Your task is to print the ‘Dice Function’ in the VS Code Terminal  # 
#  • A directory named home/username/Desktop/ML/Task1 needs to be    #
# created and inside that the                                        #
# 2_Dice.py python file needs to be created                          #
#  • Some hints: in addition to previous commands read on the        #
# ‘import’, ‘random’ and ’randint’                                   #
#                                                                    #
#                                                                    #
# Author: Miguel Angel Lopez Mejia                                   #
######################################################################

# region Libraries
import random
from collections import Counter

# endregion

# region Functions

def get_dice_number():
    """
    Prompts the user for the number of dice and returns it as an integer.

    Returns:
        int: The number of dice entered by the user, or 0 if input is invalid.

    Raises:
        None explicitly, but handles all exceptions internally by returning 0.

    Examples:
        >>> get_dice_number()  # User enters "3"
        3
        >>> get_dice_number()  # User enters "abc"
        The value must be integer
        0
    """
    try:
        dice_number = int(input("How many dices? "))
        return dice_number  
    except Exception as e:
        print("The value must be integer")
        return 0
        

def generate_random(dices):
    """
    Generates random values (1-6) for a specified number of dice.

    Args:
        dices (int): The number of dice to generate values for.

    Returns:
        dict: A dictionary where keys are dice numbers (as strings) and values are random integers
              between 1 and 6 (inclusive).

    Examples:
        >>> generate_random(2)
        {'1': 4, '2': 6}  # Random values will vary
        >>> generate_random(0)
        {}
    """    

    dice_values = {}
    for dice in range(0,dices):
        dice_values[f'{1 + dice}'] = (random.randint(1,6))
        
    return dice_values

def count_values(dice_values):
    """
    Prints the value of each die from a dictionary of dice results.

    Args:
        dice_values (dict): A dictionary where keys are dice identifiers (e.g., '1', '2')
                            and values are the rolled numbers.

    Returns:
        None: This function only prints output and does not return a value.

    Examples:
        >>> count_values({'1': 3, '2': 5})
        The dice number 1 shows: 3
        The dice number 2 shows: 5
        >>> count_values({})
        # Prints nothing
    """    
    for dice, value in dice_values.items():
        print("---------------------------------------------------------------------")
        print(f"The dice number {dice} shows: {value}")
        print("---------------------------------------------------------------------")

# endregion

#region Implementation
dices = get_dice_number()
dice_values = generate_random(dices)

count_values = count_values(dice_values)

#endregion
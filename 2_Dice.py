######################################################################
#                                                                    #
# Task 1.2: Introduction to Python: Running Make Dice on VS code     #
# Instructions:                                                      #
# Your task is to print the ‘Dice Function’ in the VS Code Terminal  # 
#  • A directory named home/username/Desktop/ML/Task1 needs to be    #
# created and inside that the 2_Dice.py python file needs to be      #
# created                                                            #
#  • Some hints: in addition to previous commands read on the        #
# ‘import’, ‘random’ and ’randint’                                   #
#                                                                    #
#                                                                    #
# Author: Miguel Angel Lopez Mejia                                   #
######################################################################

# region Libraries
import random
import sys

# endregion

# region Class
class DiceGenerator:
    def __init__(self):
        pass

    def get_dice_number(self):
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
            self.dice_number = int(input("How many dice? "))
            
        except ValueError as e:
            print("The value must be integer")
            sys.exit(1) # Exit with a non-zero status code to indicate an error
            

    def generate_random(self):
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

        self.dice_values = {}
        for dice in range(0,self.dice_number):
            self.dice_values[f'{1 + dice}'] = (random.randint(1,6))
            
        
    def count_values(self):
        """
        Prints the value of each dice from a dictionary of dice results.

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
        for dice, value in self.dice_values.items():
            print("---------------------------------------------------------------------")
            print(f"The dice number {dice} shows: {value}")
            print("---------------------------------------------------------------------")

# endregion

#region Implementation
def main():
    """
    Orchestrates the process of simulating dice rolls and counting the occurrences of each value.

    This function creates an instance of the `DiceGenerator` class, prompts the user
    to specify the number of dice to roll, generates the random dice rolls, and then
    counts the frequency of each outcome.

    It calls the following methods of the `DiceGenerator` instance in sequence:
    - `get_dice_number()`: Obtains the desired number of dice to roll from the user.
    - `generate_random()`: Simulates the rolling of the specified number of dice,
      generating a list of random integer values between 1 and 6 (inclusive).
    - `count_values()`: Analyzes the generated dice rolls and counts the occurrences
      of each possible dice value (1 through 6), storing the results in an internal
      data structure.
    """    
    dice_generator_instance = DiceGenerator()
    dice_generator_instance.get_dice_number()
    dice_generator_instance.generate_random()
    dice_generator_instance.count_values()

if __name__ == "__main__":
    main()
#endregion
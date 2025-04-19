######################################################################
#                                                                    #
# Task 1.2: Introduction to Python: proving dice function randomly   #
# Instructions:                                                      #
#  • Your task is to prove your ‘Dice Function’ is working in the    #
# VS Code                                                            #
#  • A directory named home/username/Desktop/ML/Task1 needs to be    #
# created and inside that the                                        #
# 3_Dice_Ext.py python file needs to be created                      #
#  • Some hints: in addition to previous commands read on the        #
# ‘for loop’, ‘while loop’, ‘matplotlib’ and ’numpy’                 #
# • What can you do to prove randomness? Think about statistics      #
#                                                                    #
#                                                                    #
# Author: Miguel Angel Lopez Mejia                                   #
######################################################################

# region Libraries
import random
import matplotlib.pyplot as plt
import logging
import numpy as np
import sys
from collections import Counter
from statistics import mean
# endregion

# Basic configuration
logging.basicConfig(level=logging.INFO)  # Sets the level to INFO and above

# Create a logger
logger = logging.getLogger(__name__)  # __name__ gives the module name

# region Class
class DiceGenerator:
    def __init():
        pass
    
    def get_roll_number(self):
        """
        Prompts the user for the number of die rolls and stores it in `self.num_rolls`.

            This method requests an integer input for how many times to roll a die. If the input
            is valid, it assigns the value to `self.num_rolls`. If the input is invalid (e.g., non-integer),
            it prints an error message and terminates the program.

            Notes:
                - Stores the result in `self.num_rolls` as an integer.
                - Uses `input()` for user interaction, expecting an integer.
                - On invalid input, the program exits with status code 1 via `sys.exit(1)`.
                - Assumes a single die, as the prompt refers to rolling "the dice" (singular context).

            Example:
                >>> dice_gen = DiceGenerator()
                >>> dice_gen.get_roll_number()  # User enters "5"
                # Sets dice_gen.num_rolls = 5
                >>> dice_gen.get_roll_number()  # User enters "abc"
                The value must be integer
                # Program exits with status code 1

            Raises:
                SystemExit: If the input cannot be converted to an integer, with an error message.
            """
        try:
            self.num_rolls = int(input("How many times you want to roll the dice? "))
            
        except Exception as e:
            print("The value must be integer")
            sys.exit(1)

    # Function to simulate die rolls
    def roll_die(self):
        """
        Simulates rolling a six-sided die multiple times and stores the results.

        This method generates a list of random integers between 1 and 6 (inclusive),
        representing the outcomes of rolling a die `self.num_rolls` times. The results
        are stored in the instance variable `self.results`.

        Attributes:
            self.results (list): A list of integers representing the die roll outcomes.
            self.num_rolls (int): The number of times the die is rolled, defined elsewhere
                                in the class.

        """        
        self.results = [random.randint(1, 6) for roll in range(self.num_rolls)]

    def count_ocurrences_per_face(self):
        """
        Counts the occurrences of each die face in the results and logs the statistics.

        This method uses the Counter class to tally the frequency of each result (1 to 6)
        from the die rolls stored in `self.results`. It then logs the count and percentage
        of occurrences for each face using a logger.

        Attributes:
            self.counts (Counter): A Counter object storing the frequency of each die face.
            self.results (list): A list of integers (1-6) representing prior die roll outcomes.
            self.num_rolls (int): The total number of die rolls, defined elsewhere in the class.

        Notes:
            - Requires the `collections` module for Counter (`from collections import Counter`).
            - Requires a `logger` object (e.g., from the `logging` module) to be configured.

        """
        logger.info("-----------------------------------------------------------------------------------------------")
        self.counts = Counter(self.results) # Counter({4: 23, 5: 20, 1: 17, 2: 16, 3: 15, 6: 9})
        for i in range(1, 7):
            logger.info(f" Face {i}: Appears {self.counts[i]} times - ({round(self.counts[i]/self.num_rolls*100,2)} %) ")
        
        logger.info("-----------------------------------------------------------------------------------------------")
        
        
    def test_randomness(self):
        """
        The Chi-Square method is used to determine if there is a significant difference between the expected 
        frequencies and the observed frequencies, the function assumes that each face of the die the 
        same probability of 1/6.

        The method is represented by the following formula:
            χ2=∑ (Oi-Ei)2/Ei

        Where 
        Oi is the observed frequency, in this case, the frequency of each face of the die
        Ei is the excpected frecuency of each face of the die

        E.G.
        Analysis:
        If the die is rolled 12 times, we expect that the frequency of the values to be like:
        Expected = 12/6 = 2 for each face
        Observed = [0,4,1,3,3,1] (sum is 12)

        χ2 = 6.0 (In this case, the formula will calculate the Chi-Square for [0,4,1,3,3,1] and [2,2,2,2,2,2])
        
        Now, we need to consider the following:

        1. Degrees of freedom = 6-5 = 1 (We know that there are 6 categories, if we roll the dice 12 times, 
        the sum of the frequencies of each face of the dice must be 12, if we know that the values of the 
        numbers 1-5 are 0,4,1,3,3 the value of the number 6 must be 1 so they sum 12, there is no freedom 
        to choose the last value, that is why we have 1 degree of freedom.)

        2. Critic Value = 11.07 (Considering a significance level (α) = 0.05 , It is the threshold defined to decide when a 
        difference between what is observed and what is expected is "too large" to be attributed 
        to chance, 0.05 is the standar - Check for reference Images/3_Dice_Chi_square_probability_table.png)

        Conclusion:
        - We defined the Null Hypothesis = The dice is fair, which means that the frequencies of each face of the dice are the same.
        - Null Hypothesis expects χ2 > Critic Value
        - As the value of χ2 < Critic Value (6.0 < 11.07) we can't reject the Null Hyphotesis (The dice is fair)
        - The expected mean is 2
        - The observed mean is 3.666
        """
         # Count frequencies
        observed = np.array([self.counts.get(i, 0) for i in range(1, 7)])
        
        # Expécted frequency
        expected = np.full(6, self.num_rolls / 6)
   
        # Calculate Chi-square
        chi_square_stat = np.sum((observed - expected) ** 2 / expected)

        logger.info("-----------------------------------------------------------------------------------------------")
        logger.info(f"-------------------------- Test of Randomness - Chi-square method -----------------------------")
        logger.info("-----------------------------------------------------------------------------------------------")

        if chi_square_stat > 11.07:
            logger.info(f" Degrees of freedom: 5 (6 faces - 1)")
            logger.info(" Compare with critical value (e.g., 11.07 for alpha=0.05, df=5)")
            logger.info(f" The value of Chi-square ({chi_square_stat}) > Critic Value (11.07).")
            logger.info(" The conclusion is that the Null hypothesis can be rejected.")
        else:
            logger.info(f" Degrees of freedom: 5 (6 faces - 1)")
            logger.info(" Compare with critical value (e.g., 11.07 for alpha=0.05, df=5)")            
            logger.info(f" The value of Chi-square ({chi_square_stat}) < Critic Value (11.07)")
            logger.info(" The conclusion is that there is no enough information to reject the Null hypothesis")
        
        logger.info("-----------------------------------------------------------------------------------------------")
        logger.info("-----------------------------------------------------------------------------------------------")

    def plot_results(self):
        """
        Generates a bar chart of dice roll results with a mean line.

            This method creates a visualization of the dice roll results stored in `self.results`.
            It plots each roll’s value as a bar, adds a horizontal line for the observed mean,
            and logs the expected mean (3.5 for a fair six-sided die) and observed mean.
            The plot includes labeled axes, a title, and a legend.

            Notes:
                - Requires `self.results` to be a list or array of dice roll outcomes (integers).
                - Uses `matplotlib.pyplot` for plotting and a `logger` for logging.
                - The expected mean is hardcoded as 3.5, assuming a fair six-sided die.
                - The plot is displayed immediately using `plt.show()`.

            Example:
                >>> dice_gen = DiceGenerator()
                >>> dice_gen.results = [4, 2, 6, 3, 1]
                >>> dice_gen.plot_results()
                # Logs expected and observed means, displays a bar chart with mean line.
            """        
        num_rolls = len(self.results)
        roll_numbers = list(range(1, num_rolls + 1)) # Roll numbers starting from 1

        logger.info(f" The Expected mean is 3.5")
        mean_dices = mean(self.results)
        logger.info(f" The Observed mean is {mean_dices}")
        logger.info("-----------------------------------------------------------------------------------------------")
        # Create bar chart
        plt.bar(x=roll_numbers, height=self.results, color='cyan', label='Values', align='center')
        # Add a horizontal line for the mean
        plt.axhline(y=mean_dices, color='firebrick', linestyle='--', label=f'Mean = {mean_dices:.2f}')

        # Customize the plot
        plt.xlabel('Roll Number')
        plt.ylabel('Value')
        plt.title('Die Rolls and Their Mean')
        plt.xticks(roll_numbers) # Set the x-axis ticks to the roll numbers
        plt.legend()

        # Show the plot
        plt.tight_layout() # Adjust layout to prevent labels from overlapping
        plt.show()

    def histogram_die(self):
        """
        Generates a histogram showing the frequency distribution of dice roll results.

        This method creates a histogram of the dice roll outcomes stored in `self.results`,
        with bins centered on the possible die values (1 to 6). The x-axis represents the
        dice values, and the y-axis shows the frequency of each value.

        Attributes:
            self.results (list): A list of integers (1-6) representing die roll outcomes.
            self.num_rolls (int): The total number of die rolls, defined elsewhere in the class.

        Notes:
            - Requires `matplotlib.pyplot` for plotting (`import matplotlib.pyplot as plt`).
            - The bins are set to [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5] to center bars on integer values.

        """     
        # Create histogram
        plt.hist(self.results, bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], 
                edgecolor='black', align='mid')
        plt.title(f'Distribution of {self.num_rolls} Die Rolls')

        plt.xlabel('Die Value')
        plt.ylabel('Frequency')
        plt.show()
# endregion


#region Implementation
def main():
    """
    Executes a sequence of die simulation and analysis steps.
    This function initializes a `DiceGenerator` object and orchestrates a workflow to:
            1. Prompt the user for the number of die rolls.
            2. Simulate rolling a die the specified number of times.
            3. Count and log occurrences of each die face.
            4. Perform a chi-square test to assess randomness.
            5. Generate a bar chart displaying results with the mean.
            6. Create a histogram of the roll results.
    """    
    die_generator = DiceGenerator()

    die_generator.get_roll_number()

    die_generator.roll_die()

    die_generator.count_ocurrences_per_face()
    
    die_generator.test_randomness()

    die_generator.plot_results()

    die_generator.histogram_die()


if __name__ == "__main__":
    main()
#endregion    
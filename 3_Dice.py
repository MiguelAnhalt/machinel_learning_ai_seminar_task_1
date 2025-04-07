import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import logging


from collections import Counter
from statistics import mean

# Basic configuration
logging.basicConfig(level=logging.INFO)  # Sets the level to INFO and above

# Create a logger
logger = logging.getLogger(__name__)  # __name__ gives the module name

class DiceGenerator:
    def __init():
        pass
    
    def get_roll_number(self):
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
            self.num_rolls = int(input("How many times you want to roll the dice? "))
            
        except Exception as e:
            print("The value must be integer")
            self.num_rolls = 0

    # Function to simulate dice rolls
    def roll_dice(self):
        self.results = [random.randint(1, 6) for roll in range(self.num_rolls)]


    def count_ocurrences_per_result(self):
        """
        Simulates rolling a six-sided die multiple times and returns the results.

            Args:
                num_rolls (int): The number of times to roll the die.

            Returns:
                list: A list of integers, each between 1 and 6, representing the dice roll outcomes.

            Example:
                >>> sim = DiceSimulator()
                >>> sim.roll_dice(3)
                [4, 1, 6]  # Example output, actual results will vary due to randomness.
            """        
        self.counts = Counter(self.results)
        for i in range(1, 7):
            logger.info(f"Face {i}: Appears {self.counts[i]} times - ({round(self.counts[i]/self.num_rolls*100,2)} %) ")
        
        

    def chi_square(self):
        # Chi-square test for uniformity
        expected = self.num_rolls / 6  # Expected frequency for each number
        observed = [self.counts[i] for i in range(1, 7)]
        chi_square_stat, p_value = stats.chisquare(observed, [expected] * 6)
        # print(f"\nChi-square statistic: {chi_square_stat:.2f}")
        logger.info(f"Chi-square statistic: {round(chi_square_stat,2)}")
        # print(f"P-value: {p_value:.4f}")
        logger.info(f"P-value: {round(p_value,4)}")
    
    def mean_graph(self):
        """
        Creates a bar chart of dice roll results with a line indicating their mean.

            Args:
                results (list): A list of integers representing dice roll outcomes.

            Notes:
                Logs the mean value using the logging module at the INFO level.
                Requires matplotlib.pyplot as plt, statistics.mean, and a configured logger.

            Example:
                >>> sim = DiceSimulator()
                >>> sim.mean_graph([1, 2, 3, 4, 5])
                # Displays a bar chart with bars at 1, 2, 3, 4, 5 and a red dashed line at mean 3.0
            """        
        indices = range(len(self.results)) # Obtain the indexes for the X-axis
        mean_dices = mean(self.results)
        logger.info(f"The mean is {mean_dices}")

        # Create bar chart
        plt.bar(indices, self.results, color = 'cyan', label = 'Values')
        # Add a horizontal line for the mean
        plt.axhline(y=mean_dices, color='red', linestyle='--', label=f'Mean = {mean_dices}')
        
        # Customize the plot
        plt.xlabel('Roll Number')
        plt.ylabel('Value')
        plt.title('Dice Rolls and Their Mean')
        plt.legend()

        # Show the plot
        plt.show()


    def histogram_dice(self):
        """
        Creates a histogram showing the frequency distribution of dice roll results.

            Args:
                results (list): A list of integers representing dice roll outcomes (1 to 6).

            Notes:
                Assumes num_rolls is available as a class attribute (self.num_rolls).
                Requires matplotlib.pyplot as plt.

            Example:
                >>> sim = DiceSimulator()
                >>> sim.num_rolls = 5
                >>> sim.histogram_dice([1, 2, 2, 3, 4])
                # Displays a histogram with bars for values 1, 2, 3, 4, and their frequencies.
            """        
        # Create histogram
        plt.hist(self.results, bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], 
                edgecolor='black', align='mid')
        plt.title(f'Distribution of {self.num_rolls} Dice Rolls')
        plt.xlabel('Dice Value')
        plt.ylabel('Frequency')
        plt.show()


dice_generator = DiceGenerator()

dice_generator.get_roll_number()

dice_generator.roll_dice()

counts = dice_generator.count_ocurrences_per_result()

dice_generator.chi_square()

dice_generator.mean_graph()

dice_generator.histogram_dice()

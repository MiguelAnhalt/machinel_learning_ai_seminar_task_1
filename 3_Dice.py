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

import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import logging
import numpy as np
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
        """
        Simulates rolling a six-sided die multiple times and stores the results.

        This method generates a list of random integers between 1 and 6 (inclusive),
        representing the outcomes of rolling a die `self.num_rolls` times. The results
        are stored in the instance variable `self.results`.

        Attributes:
            self.results (list): A list of integers representing the die roll outcomes.
            self.num_rolls (int): The number of times the die is rolled, defined elsewhere
                                in the class.

        Examples:
            >>> class DiceSimulator:
            ...     def __init__(self, num_rolls):
            ...         self.num_rolls = num_rolls
            ...     def roll_dice(self):
            ...         self.results = [random.randint(1, 6) for roll in range(self.num_rolls)]
            >>> sim = DiceSimulator(3)
            >>> sim.roll_dice()
            >>> print(sim.results)  # Possible output: [4, 1, 6]
        """        
        self.results = [random.randint(1, 6) for roll in range(self.num_rolls)]


    def count_ocurrences_per_result(self):
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

        Examples:
            >>> from collections import Counter
            >>> import logging
            >>> logging.basicConfig(level=logging.INFO)
            >>> logger = logging.getLogger(__name__)
            >>> class DiceSimulator:
            ...     def __init__(self, num_rolls):
            ...         self.num_rolls = num_rolls
            ...         self.results = []
            ...     def count_ocurrences_per_result(self):
            ...         self.counts = Counter(self.results)
            ...         for i in range(1, 7):
            ...             logger.info(f" Face {i}: Appears {self.counts[i]} times - ({round(self.counts[i]/self.num_rolls*100,2)} %) ")
            >>> sim = DiceSimulator(100)
            >>> sim.results = [4, 4, 5, 1, 2, 3, 6]  # Example results
            >>> sim.count_ocurrences_per_result()
            INFO:__main__: Face 1: Appears 1 times - (1.0 %)
        """
        self.counts = Counter(self.results) # Counter({4: 23, 5: 20, 1: 17, 2: 16, 3: 15, 6: 9})
        for i in range(1, 7):
            logger.info(f" Face {i}: Appears {self.counts[i]} times - ({round(self.counts[i]/self.num_rolls*100,2)} %) ")
        
        
    def test_randomness(self):
        """
        The Chi-Square method is used to determine if there is a significant difference between the expected 
        frequencies and the observed frequencies, the function assumes that each face of the dice the 
        same probability of 1/6.

        The method is represented by the following formula:
            χ2=∑ (Oi-Ei)2/Ei

        Where 
        Oi is the observed frequency, in this case, the frequency of each face of the dice
        Ei is the excpected frecuency of each face of the dice

        E.G.
        Analysis:
        If the dice is rolled 12 times, we expect that the frequency of the values to be like:
        Expected = 12/6 = 2 for each face
        Observed = [0,4,1,3,3,1] (sum is 12)

        χ2 = 6.0 (In this case, the formula will calculate the Chi-Square for [0,4,1,3,3,1] and [2,2,2,2,2,2])
        
        Now, we need to consider the following:

        1. Degrees of freedom = 6-5 = 1 (We know that there are 6 categories, if we roll the dice 12 times, 
        the sum of the frequencies of each face of the dice must be 12, if we know that the values of the 
        numbers 1-5 are 0,4,1,3,3 the value of the number 6 must be 1 so they sum 12, there is no freedom 
        to chosse the last value, that is why we have 1 degree of freedom.)

        2. Critic Value = 11.07 (Considering a significance level (α) = 0.05 , It is the threshold defined to decide when a 
        difference between what is observed and what is expected is "too large" to be attributed 
        to chance, 0.05 is the standar - Check for reference Images/3_Dice_Chi_square_probability_table.png)

        3. P-Value = 0.05 (We consider the value of P-Value to be 0.05, is an indicator that tells us what is the probability of 
        observing a test statistic as extreme or more extreme than the one calculated, under the Null hypothesis.)

        Conclusion:
        - We defined the Null Hypothesis = The dice is fair, which means that the frequencies of each face of the dice are the same.
        - Null Hypotesis expects χ2 > Critic Value
        - As the value of χ2 < Critic Value (6.0 < 11.07) we can't reject the Null Hyphotesis (The dice is fair)
        - We can also use the P-value where, is p < 0.05, we can reject the Null Hyphotesis, 
        - is p > 0.05 we can't reject the Null Hypothesis 
        - P-value will be 0.3062, which means 0.3062 > 0.05 (The dice is fair)
        - The expected mean is 2
        - The observed mean is 3.666
        """
        # Contar frecuencias observadas con NumPy
        observed = np.array([self.counts.get(i, 0) for i in range(1, 7)])
        
        # Frecuencia esperada (uniforme: num_rolls / 6)
        expected = np.full(6, self.num_rolls / 6)
   
        # Calcular chi-cuadrado manualmente
        chi_square_stat = np.sum((observed - expected) ** 2 / expected)
                
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


    def chi_square(self):
        """
        The Chi-Square method is used to determine if there is a significant difference between the expected 
        frequencies and the observed frequencies, the function assumes that each face of the dice the 
        same probability of 1/6.

        The method is represented by the following formula:
            χ2=∑ (Oi-Ei)2/Ei

        Where 
        Oi is the observed frequency, in this case, the frequency of each face of the dice
        Ei is the excpected frecuency of each face of the dice

        E.G.
        Analysis:
        If the dice is rolled 12 times, we expect that the frequency of the values to be like:
        Expected = 12/6 = 2 for each face
        Observed = [0,4,1,3,3,1] (sum is 12)

        χ2 = 6.0 (In this case, the formula will calculate the Chi-Square for [0,4,1,3,3,1] and [2,2,2,2,2,2])
        
        Now, we need to consider the following:

        1. Degrees of freedom = 6-5 = 1 (We know that there are 6 categories, if we roll the dice 12 times, 
        the sum of the frequencies of each face of the dice must be 12, if we know that the values of the 
        numbers 1-5 are 0,4,1,3,3 the value of the number 6 must be 1 so they sum 12, there is no freedom 
        to chosse the last value, that is why we have 1 degree of freedom.)

        2. Critic Value = 11.07 (Considering a significance level (α) = 0.05 , It is the threshold defined to decide when a 
        difference between what is observed and what is expected is "too large" to be attributed 
        to chance, 0.05 is the standar - Check for reference Images/3_Dice_Chi_square_probability_table.png)

        3. P-Value = 0.05 (We consider the value of P-Value to be 0.05, is an indicator that tells us what is the probability of 
        observing a test statistic as extreme or more extreme than the one calculated, under the Null hypothesis.)

        Conclusion:
        - We defined the Null Hypothesis = The dice is fair, which means that the frequencies of each face of the dice are the same.
        - Null Hypotesis expects χ2 > Critic Value
        - As the value of χ2 < Critic Value (6.0 < 11.07) we can't reject the Null Hyphotesis (The dice is fair)
        - We can also use the P-value where, is p < 0.05, we can reject the Null Hyphotesis, 
        - is p > 0.05 we can't reject the Null Hypothesis 
        - P-value will be 0.3062, which means 0.3062 > 0.05 (The dice is fair)
        - The expected mean is 2
        - The observed mean is 3.666
        """
        # Chi-square test for uniformity
        expected = self.num_rolls / 6  # Expected frequency for each number
        observed = [self.counts[i] for i in range(1, 7)] # Observed frequencies per face of the dice

        chi_square_stat, p_value = stats.chisquare(observed, [expected] * 6)
        

        logger.info(" The Null Hypothesis is that the dice is fair.")

        if chi_square_stat > 11.07 and p_value < 0.05:
            logger.info(f" The value of Chi-square ({chi_square_stat}) > Critic Value (11.07), and the P-value ({round(p_value,2)}) < 0.05.")
            logger.info(" The conclusion is that the Null hypothesis can be rejected.")
        else:
            logger.info(f" The value of Chi-square ({chi_square_stat}) < Critic Value (11.07), and the P-value ({round(p_value,2)}) > 0.05.")
            logger.info(" The conclusion is that there is no enough information to reject the Null hypothesis")

    
    def mean_graph(self):
        """
        Generates a bar chart of dice roll results and overlays the observed mean.

        Args:
            self: The instance of the class with results attribute.

        Attributes:
            self.results (list): List of die roll outcomes (integers 1-6).

        Notes:
            Requires `from statistics import mean`, `import matplotlib.pyplot as plt`,
            and a configured `logger`.

        """       
        indices = range(len(self.results)) # Obtain the indexes for the X-axis
        logger.info(f" The Expected mean is 3.5")
        mean_dices = mean(self.results)
        logger.info(f" The Observed mean is {mean_dices}")

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

        Examples:
            >>> import matplotlib.pyplot as plt
            >>> class DiceSimulator:
            ...     def __init__(self, num_rolls):
            ...         self.num_rolls = num_rolls
            ...         self.results = []
            ...     def histogram_dice(self):
            ...         plt.hist(self.results, bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], 
            ...                 edgecolor='black', align='mid')
            ...         plt.title(f'Distribution of {self.num_rolls} Dice Rolls')
            ...         plt.xlabel('Dice Value')
            ...         plt.ylabel('Frequency')
            ...         plt.show()
            >>> sim = DiceSimulator(10)
            >>> sim.results = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]  # Example results
            >>> sim.histogram_dice()
            # Displays a histogram with bars centered at 1, 2, 3, 4, 5, 6 showing frequencies
        """     
        # Create histogram
        plt.hist(self.results, bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], 
                edgecolor='black', align='mid')
        plt.title(f'Distribution of {self.num_rolls} Dice Rolls')
        plt.xlabel('Dice Value')
        plt.ylabel('Frequency')
        plt.show()

def main():
    """Executes a sequence of dice simulation and analysis steps.

        This function initializes a DiceGenerator object and runs a series of methods to:
        1. Prompt the user for the number of dice rolls,
        2. Simulate rolling a die that many times,
        3. Count and log the occurrences of each result,
        4. Generate a bar chart with the mean,
        5. Create a histogram of the results.
        6. Perform a chi-square test on the results,
    """    
    dice_generator = DiceGenerator()

    dice_generator.get_roll_number()

    dice_generator.roll_dice()

    dice_generator.count_ocurrences_per_result()
    
    # Extra analysis
    dice_generator.test_randomness()


    dice_generator.mean_graph()

    dice_generator.histogram_dice()


main()
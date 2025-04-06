import random
import matplotlib.pyplot as plt
import scipy.stats as stats

from collections import Counter
from statistics import mean

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
            dice_number = int(input("How many times you want to roll the dice? "))
            return dice_number  
        except Exception as e:
            print("The value must be integer")
            return 0

    # Function to simulate dice rolls
    def roll_dice(self, num_rolls):
        """
        """
        return [random.randint(1, 6) for _ in range(num_rolls)]

    def count_ocurrences_per_result(self, results):
        # Count occurrences of each number
        counts = Counter(results)
        for i in range(1, 7):
            print(f"Number {i}: Appears {counts[i]} times ({counts[i]/num_rolls*100:.1f}%)")
        
        return counts

    def chi_square(self, counts):
        # Chi-square test for uniformity
        expected = num_rolls / 6  # Expected frequency for each number
        observed = [counts[i] for i in range(1, 7)]
        chi_square_stat, p_value = stats.chisquare(observed, [expected] * 6)
        print(f"\nChi-square statistic: {chi_square_stat:.2f}")
        print(f"P-value: {p_value:.4f}")
    
    def mean_graph(self, results):
        indices = range(len(results)) # Obtain the indeces for the X-axis
        mean_dices = mean(results)

        print(f"The mean is {mean_dices}")

        # Create bar chart
        plt.bar(indices, results, color = 'skyblue', label = 'Values')
        # Add a horizontal line for the mean
        plt.axhline(y=mean_dices, color='red', linestyle='--', label=f'Mean = {mean_dices}')
        
        # Customize the plot
        plt.xlabel('Roll Number')
        plt.ylabel('Value')
        plt.title('Dice Rolls and Their Mean')
        plt.legend()

        # Show the plot
        plt.show()


    def histogram_dice(self, results):
        # Create histogram
        plt.hist(results, bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], 
                edgecolor='black', align='mid')
        plt.title(f'Distribution of {num_rolls} Dice Rolls')
        plt.xlabel('Dice Value')
        plt.ylabel('Frequency')
        plt.show()


dice_generator = DiceGenerator()

# Simulate 10000 dice rolls
# num_rolls = 100
num_rolls = dice_generator.get_roll_number()
results = dice_generator.roll_dice(num_rolls)

counts = dice_generator.count_ocurrences_per_result(results)

dice_generator.chi_square(counts)

dice_generator.mean_graph(results)

dice_generator.histogram_dice(results)

import random
import matplotlib.pyplot as plt
from collections import Counter
import scipy.stats as stats

# Function to simulate dice rolls
def roll_dice(num_rolls):
    return [random.randint(1, 6) for _ in range(num_rolls)]

# Simulate 10000 dice rolls
num_rolls = 10000
results = roll_dice(num_rolls)

# Count occurrences of each number
counts = Counter(results)
print(type(counts))
for i in range(1, 7):
    print(f"Number {i}: {counts[i]} times ({counts[i]/num_rolls*100:.1f}%)")

# Chi-square test for uniformity
expected = num_rolls / 6  # Expected frequency for each number
observed = [counts[i] for i in range(1, 7)]
chi_square_stat, p_value = stats.chisquare(observed, [expected] * 6)
print(f"\nChi-square statistic: {chi_square_stat:.2f}")
print(f"P-value: {p_value:.4f}")

# Create histogram
plt.hist(results, bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], 
         edgecolor='black', align='mid')
plt.title(f'Distribution of {num_rolls} Dice Rolls')
plt.xlabel('Dice Value')
plt.ylabel('Frequency')
plt.show()
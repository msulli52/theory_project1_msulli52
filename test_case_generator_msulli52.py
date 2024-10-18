import csv
import random

# function to generate a specific number of random test cases per knapsack size
def generate_test_cases(file_name, tests_per_size, min_size, max_size):
    # coin values in the currency list
    coins = [3, 11, 23]
    
    # open the csv file to write the test cases
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # header row
        writer.writerow(['Target (Cents)', 'Knapsack (Coin Counts)', 'Number of Coins in Knapsack'])
        
        for knapsack_size in range(min_size, max_size + 1):
            for _ in range(tests_per_size):
                # randomly choose a target value
                target_value = random.randint(20, 200)
                
                # create the knapsack with a random number of each coin (3, 11, 23)
                knapsack = [0, 0, 0]  # coin counts for 3, 11, and 23 cent coins
                
                # randomly distribute the number of coins in the knapsack across the 3 types
                remaining_coins = knapsack_size
                for i in range(2):  # first two coin types (3 and 11)
                    knapsack[i] = random.randint(0, remaining_coins)
                    remaining_coins -= knapsack[i]
                knapsack[2] = remaining_coins  # remaining coins go to 23

                # write test case to csv file
                writer.writerow([target_value, knapsack, knapsack_size])

    print(f"Generated {tests_per_size * (max_size - min_size + 1)} test cases and saved to {file_name}")

# parameters for test case generation
file_name = 'output_test_cases_msulli52.csv'
tests_per_size = 40     # number of test cases per knapsack size
min_size = 1            # minimum knapsack size
max_size = 15           # maximum knapsack size

# generate the test cases
generate_test_cases(file_name, tests_per_size, min_size, max_size)

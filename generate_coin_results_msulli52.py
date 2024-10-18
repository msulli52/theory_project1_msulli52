import time
import csv

# function to generate all possible combinations of coins
def generate_combos(coins):
    n = len(coins)
    combos = []
    
    # loop through all possible subsets (binary approach)
    # 2^n possible subsets, represented by binary numbers from 0 to 2^n - 1
    for i in range(1 << n):  # 1 << n is 2^n
        subset = []
        for j in range(n):
            if i & (1 << j):  # if the j-th bit in i is set, include coins[j]
                subset.append(coins[j])
        combos.append(subset)
    
    return combos

# function that iteratively finds a combination of coins that adds up to the target value
# generates all possible combinations, checks their sum, and stops early if a valid combo is found.
def find_coin_combo(target, coins):
    start = time.time()  # start the timer
    
    # generate all combinations of coins
    combinations = generate_combos(coins)
    
    # check each combination to see if it sums to the target value
    for combo in combinations:
        if sum(combo) == target:
            end = time.time()  # stop the timer if target found
            return combo, (end - start) * 1e6  # return the valid combo and time in microseconds
    
    # if no combo possible 
    end = time.time()  # stop timer
    return None, (end - start) * 1e6  # return None if no valid combo



# function to run test cases and save results to a CSV file
def run_test_cases(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        fieldnames = ['Target Value', 'Knapsack (3, 11, 23)', 'Total Coins', 'Execution Time (µs)', 'Combination', 'Satisfiability']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        # read each line of the input CSV file and process it
        reader = csv.reader(infile)
        next(reader)  # skip the header row
        
        for row in reader:
            target_value = int(row[0])  # target value
            knapsack = list(map(int, row[1].strip('[]').split(',')))  # convert coin counts from string to list
            total_coins = int(row[2])  # total number of coins (for reference)

            # create the coin list based on the knapsack values
            coin_distribution = [3] * knapsack[0] + [11] * knapsack[1] + [23] * knapsack[2]

            # run the coin combo function and record the results
            solution, time_taken = find_coin_combo(target_value, coin_distribution)
            satisfiability = 'Satisfiable' if solution else 'Unsatisfiable'

            # write the result to the output CSV
            writer.writerow({
                'Target Value': target_value,
                'Knapsack (3, 11, 23)': knapsack,
                'Total Coins': total_coins,
                'Execution Time (µs)': time_taken,
                'Combination': solution if solution else [],
                'Satisfiability': satisfiability
            })

# main function to process the CSV test cases and save the results
def main():
    input_file = 'output_test_cases_msulli52.csv'  # input CSV file with test cases
    output_file = 'output_results_msulli52.csv'  # output CSV file for results

    # run the test cases and save the results to the output CSV file
    run_test_cases(input_file, output_file)

if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.optimize import curve_fit

# function to represent y = b + a(2^x)
def boundary_curve(x, a, b):
    return b + a * (2**x)

# function to plot results from the csv file
def plot_results(input_file):
    # initialize lists to store data points
    total_coins = []
    execution_times = []
    colors = []
    satisfiable_points = []  # to count how many are satisfiable
    unsatisfiable_points = []  # to count how many are unsatisfiable

    # open the csv file and read data
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # get total number of coins and execution time
            total_coins.append(int(row['Total Coins']))
            execution_times.append(float(row['Execution Time (µs)']))
            
            # set the color based on satisfiability
            if row['Satisfiability'] == 'Satisfiable':
                colors.append('green')  # satisfiable = green
                satisfiable_points.append(1)  # add to satisfiable count
            else:
                colors.append('red')    # unsatisfiable = red
                unsatisfiable_points.append(1)  # add to unsatisfiable count

    # create the scatter plot with data
    plt.figure(figsize=(10, 6))
    plt.scatter(total_coins, execution_times, c=colors, s=50, edgecolors='black', alpha=0.7, label="Data Points")
    
    # create legend with labels for satisfiable and unsatisfiable
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Satisfiable'),
                       Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Unsatisfiable')]

    # add labels and title
    plt.xlabel('Total Number of Coins in Knapsack')
    plt.ylabel('Execution Time (µs)')
    plt.title('Execution Time vs Number of Coins')

    # fit a curve to the upper boundary points
    # find max execution time for each total_coin value to fit the boundary curve
    unique_coins = np.unique(total_coins)
    max_execution_times = []

    for coin in unique_coins:
        indices = [i for i, x in enumerate(total_coins) if x == coin]
        max_execution_times.append(np.max([execution_times[i] for i in indices]))

    # fit the boundary curve y = b + a * (2^x)
    popt, _ = curve_fit(boundary_curve, unique_coins, max_execution_times)
    a, b = popt

    # generate points to plot the boundary curve
    x_fit = np.linspace(min(total_coins), max(total_coins), 100)
    y_fit = boundary_curve(x_fit, a, b)

    # plot the fitted boundary curve as a dotted line
    plt.plot(x_fit, y_fit, color='blue', linestyle='--', label=f'Boundary Curve (y = {b:.2f} + {a:.2f} * 2^x)', linewidth=2)

    # add the custom legend
    plt.legend(handles=legend_elements + [Line2D([0], [0], color='blue', lw=2, linestyle='--', label='Boundary Curve')], loc='upper left')

    # show the plot
    plt.grid(True)
    plt.show()

# main function to call the plotting function
def main():
    input_file = 'output_results_msulli52.csv'  # the csv file generated from the previous task
    plot_results(input_file)

if __name__ == '__main__':
    main()

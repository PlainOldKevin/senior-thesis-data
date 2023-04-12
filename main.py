# Imports
import pandas as pd
from string import digits

# Read csv file in
data = pd.read_csv("sacbunt_data.csv")

# Make dataframe
data_df = pd.DataFrame(data)

# Remove digits in output
def remove_digits(string):
    str.maketrans('', '', digits)
    return string.translate(remove_digits)

# Function to print statistics from main data table
def bunting_data_overview():
    print("\n")
    # Initially, print size of data set
    print("Since 2012, there have been " + str(len(data)) + " situations in MLB (Regular season) that fit the given criteria:")
    print("Extra innings, home team batting, no outs, runner on second, game tied, and a sacrifice bunt is attempted.")
    print("This is some basic noting and analysis of the data.\n")

    # Batter involved in the most of these situations (laid down the bunt)
    print("The batter who sac bunted the most in this scenario is " + data_df["Batter"].mode().to_string(index=False) + ", 3 times\n")

    # WPA added avg
    wpa_avg = str(round(data_df["WPA"].mean(), 3))
    print("The average WPA (win probability added) from the bunt in this scenario is " + wpa_avg + " (negligible)\n")

    # LI avg
    li_avg =  str(round(data_df["LI"].mean(), 2))
    print("The average LI (leverage index, the pressure the pitcher or batter saw during this play) in this scenario is " + li_avg + " (very high)\n")

    # How many of these games did the home teamn wind up winning
    wins = 0
    for i in data["Rslt"].items():
        if 'W' in i:
            wins += 1
    print("The number of wins the home team accrued where at least one of these situations occurred is " + str(wins) + " wins\n") 

    print(data_df)

    



bunting_data_overview()
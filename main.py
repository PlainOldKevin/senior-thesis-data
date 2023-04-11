# Imports
import pandas as pd
from string import digits

# Read csv files in
data = pd.read_csv("sacbunt_data_since2012.csv") # All data
# Positional data
SSdata = pd.read_csv("SSdata.csv")
Cdata = pd.read_csv("Cdata.csv")
TwoBdata = pd.read_csv("TwoBdata.csv")
CFdata = pd.read_csv("CFdata.csv")


# Make dataframes
data_df = pd.DataFrame(data)

# Remove digits in output
def remove_digits(string):
    str.maketrans('', '', digits)
    return string.translate(remove_digits)

# Function to print statistics from main data table
def since2012_all():
    print("\n")
    # Initially, print size of data set
    print("Since 2012, there have been " + str(len(data)) + " situations in MLB (Regular season) that fit the given criteria:")
    print("Ninth inning or later, <2 outs, RISP, game tied or batting team down 1 run, and a sac bunt occurs.")
    print("This is some basic noting and analysis of the data.\n")

    # Batter involved in the most of these situations (laid down the bunt)
    print("The batter who sac bunted the most in this scenario is " + data_df["Batter"].mode().to_string(index=False) + ", " +  " times\n")

    # WPA added avg
    wpa_avg = str(round(data_df["WPA"].mean(), 2))
    print("The average WPA (win probability added) from the bunt in this scenario is " + wpa_avg + " (negligible)\n")

    # LI avg
    li_avg =  str(round(data_df["LI"].mean(), 2))
    print("The average LI (leverage index, the pressure the pitcher or batter saw during this play) in this scenario is " + li_avg + " (very high)\n")

since2012_all()
import os
import csv

# Path to collect data from the Resources folder
wrestlingCSV = os.path.join("WWE-Data-2016.csv")

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def my_function(wrestlerData):

    # Find the total number of matches wrestled
    total = int(wrestlerData[1]) + int(wrestlerData[2]) + int(wrestlerData[3])

    # Find the percentage of matches won
    percent_win = int(wrestlerData[1]) / total * 100

    # Find the percentage of matches lost
    percent_loss = int(wrestlerData[2]) / total * 100
    # Find the percentage of matches drawn
    percent_draw = int(wrestlerData[3]) / total * 100
    # Print out the wrestler's name and their percentage stats
    print(f"The wrestler name is{wrestlerData[0]}")
    print(f"The win percentage is {percent_win}")
    print(f"The win percentage is {percent_loss}")
    print(f"The win percentage is {percent_draw}")


# Read in the CSV file
with open(wrestlingCSV, "r") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Prompt the user for what wrestler they would like to search for
    nameToCheck = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        if nameToCheck == row[0]:
            my_function(row)

# Function Purpose: To sum up all of the money that has been spent this week
# Parameters: None
# Return: The sum of all money
# Algorithm: Use a sentinel-controlled loop to ask the user for a cost to add to the total.
# Return the total at the end of the function.
# Assume the user only gives values that are > 0, and are numbers.


def cost_function():
    total_cost = 0
    day_count = 0
    cost_str = input("Please enter the amount of money of spent on a day here, and enter -999 when finished:")
    cost = int(cost_str)
    while cost != -999:
        day_count += 1
        total_cost += cost
        cost_str = input("Please enter the amount of money of spent on a day here, and enter -999 when finished:")
        cost = int(cost_str)

    average = total_cost / day_count
    print"You have spent", total_cost, "dollars this week."
    print"You spent on average", average, "dollars per day this week."


# Function Purpose: Main
# Parameters:
# Return: None


def main():
    # Output the purpose
    print("This program determines how much money on average you spend in a week")
    # Find out how much money has been spent this 7-day week
    # Determine the average amount of money spent each day
    # Output the total money spent this week and the average per day
    cost_function()


main()

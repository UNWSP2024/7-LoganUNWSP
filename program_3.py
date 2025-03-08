# Logan H's US Population

# 1st, SET our data list.
data_list = []

# 2nd, ASK the year, this and step 4 will still happen as long as positive year is inputted.
while True:
    year = int(input("Enter the year (Enter a Negative to end): "))

# 3rd, BREAK LOOP if a negative is entered.
    if year <= -1:  # Exit condition for the loop
        break

# 4th, ASK the state and population.
    state = input("Enter the name of the state: ")
    population = int(input(f"Enter the population of {state}: "))

# 5th, STORE the data in the list of lists.
    data_list.append([year, state, population])

# 6th, WHEN LOOP IS BROKEN, ASK for the year they would like to search through.
year_to_search = int(input("Enter the year to search for: "))

# 7th, CALCULATE total population for given year.
total_population = 0
for data in data_list:
    if data[0] == year_to_search:
        total_population += data[2]

# 8th, FINALLY< PRINT the result.
print(f"Total population for the year {year_to_search}: {total_population}")

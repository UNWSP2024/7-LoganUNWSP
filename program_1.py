# Logan H's Rainfall Program

# 1st, CREATE an empty list to store rainfall data.
rainfall = []

# 2nd, LIST of month names.
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# 3rd, GET data
for month in months:
    amount = float(input(f"Enter inches of rainfall for {month}: "))
    rainfall.append(amount)

# 4th, CALCULATE total and average rainfall.
total_rainfall = sum(rainfall)
average_rainfall = total_rainfall / 12

# 5th, FIND highest/lowest rainfall amount.
max_rainfall = max(rainfall)
min_rainfall = min(rainfall)

# 6th, FIND highest/lowest rainfall months using highest/lowest rainfall amount.
max_month = months[rainfall.index(max_rainfall)]
min_month = months[rainfall.index(min_rainfall)]

# 7th, FINISH, PRINT answer.
print("\nTotal rainfall for the year:", total_rainfall, "inches")
print("Average monthly rainfall:", round(average_rainfall, 2), "inches")
print(f"Month with the highest rainfall: {max_month} ({max_rainfall} inches)")
print(f"Month with the lowest rainfall: {min_month} ({min_rainfall} inches)")

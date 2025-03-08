# Logan H's Larger than n

# 1st, DEFINE the function
def display_greater_numbers(numbers_list, n):
    for number in numbers_list:
        if number > n:
            print(number)


# 2nd, CREATE the list of numbers
numbers_list = [10, 25, 30, 5, 60, 15, 80, 72, 1, 6, 12, 19, 27, 32, 41, 48, 59, 92]

# 3rd, SET the n
n = 47

# 4th, FINALLY PRINT the numbers greater than n
display_greater_numbers(numbers_list, n)

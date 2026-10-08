# Task 2: Reads sales data using read(), readline(), and readlines().

# Read the entire file
with open("sales_data.txt", "r") as file:
    print("Entire file:")
    print(file.read())

# Read the first line
with open("sales_data.txt", "r") as file:
    print("First line:")
    print(file.readline())

# Read all values and convert them into integers
with open("sales_data.txt", "r") as file:
    content = file.readlines()
    sales = []

    for line in content:
        values = line.strip().split(",")
        for value in values:
            if value:
                sales.append(int(value))

    print("Sales as integers:", sales)
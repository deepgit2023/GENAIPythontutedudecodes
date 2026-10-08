
# Task 3: Appends each new sale on a separate line.

# new_sales = [5000, 2500, 1700]

# with open("sales_data.txt", "a") as file:
#     for sale in new_sales:
#         file.write(str(sale) + "\n")

# with open("sales_data.txt", "r") as file:
#     print("Updated sales data:")
#     print(file.read())
    
new_sales = [5000, 2500, 1700]

with open("sales_data.txt", "a") as file:
    for sale in new_sales:
        file.write(str(sale) + "\n")

with open("sales_data.txt", "r") as file:
    print("Updated sales data:")
    print(file.read())
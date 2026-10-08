
# sales = [1200, 450, 980, 1500, 3000]

# Open the file in write mode and save each sale on a new line
# with open("sales_data.txt", "w") as file:
#     for sale in sales:
#         file.write(str(sale) + "\n")

# Open the file in read mode and display its contents
# with open("sales_data.txt", "r") as file:
#     content = file.read()
#     print(content)

# optional comma separated version

# sales = [1200, 450, 980, 1500, 3000]

# with open("sales_data.txt", "w") as file:
#     file.write(",".join(map(str, sales)))

# with open("sales_data.txt", "r") as file:
#     content = file.read()
#     print(content)


# Task 1: Writes sales amounts on separate lines.

sales = [1200, 450, 980, 1500, 3000]

with open("sales_data.txt", "w") as file:
    for sale in sales:
        file.write(str(sale) + "\n")

print("Sales :" , sales)
print("Sales file reset successfully.")
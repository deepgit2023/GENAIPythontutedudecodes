
# Task 5: Takes three product names and prices, saves them to a file, and prints each line.

with open("products.txt", "w") as file:
    for i in range(3):
        name = input(f"Enter product {i + 1} name: ")
        price = input(f"Enter product {i + 1} price: ")
        file.write(f"{name} | {price}\n")

with open("products.txt", "r") as file:
    print("\nProduct Information:")
    for line in file:
        print(line.strip())

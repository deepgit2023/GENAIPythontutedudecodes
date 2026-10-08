
# Task 7: Calculates discounted product prices, exports a report, and prints the report.

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount_percent = float(input("Enter discount percentage: "))

with open("discount_report.txt", "w") as file:
    file.write("Product | Original Price | Discounted Price\n")

    total_discounted_price = 0

    for product, price in prices.items():
        discounted_price = price * (1 - discount_percent / 100)
        total_discounted_price += discounted_price

        file.write(
            f"{product} | {price:.2f} | {discounted_price:.2f}\n"
        )

    total_items = len(prices)
    average_discounted_price = total_discounted_price / total_items

    file.write(f"Total Items: {total_items}\n")
    file.write(f"Average Discounted Price: {average_discounted_price:.2f}\n")

with open("discount_report.txt", "r") as file:
    print("\nDiscount Report:")
    print(file.read())

# Task 4: Generates a summary report from sales data stored in a file.

sales = []

# Read sales data from the file
with open("sales_data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            sales.append(int(line))

# Calculate and display the summary
if sales:
    total_sales = sum(sales)
    highest_sale = max(sales)
    lowest_sale = min(sales)
    average_sale = total_sales / len(sales)

    print("Total Sales:", total_sales)
    print("Highest Sale:", highest_sale)
    print("Lowest Sale:", lowest_sale)
    print("Average Sale:", average_sale)
else:
    print("No sales data available.")

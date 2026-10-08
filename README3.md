# Assignment 4: Python File Handling

Name: Deepanshu Sharma

## Project Overview

This assignment demonstrates Python file handling operations, including reading, writing, appending, file modes, user input, basic data processing, and safe file access.

## Tasks Completed

### Task 1: Write Sales Records to a File
- Created a list of sales amounts.
- Wrote each sales amount on a separate line in `sales_data.txt`.
- Read and printed the saved file contents.
- Practiced write (`w`) and read (`r`) modes.

### Task 2: Read File in Different Ways
- Read the entire file using `read()`.
- Read the first line using `readline()`.
- Read all lines using `readlines()`.
- Converted sales values into a list of integers.
- Used `strip()` and `split()` to clean and process file data.

### Task 3: Append New Sales
- Appended new sales amounts: 5000, 2500, and 1700.
- Saved each new amount on a separate line.
- Read and displayed the updated file.
- Practiced append (`a`) mode.

### Task 4: Generate Summary Report
- Read sales values from `sales_data.txt`.
- Converted values into integers.
- Calculated and displayed:
  - Total sales
  - Highest sale
  - Lowest sale
  - Average sale

### Task 5: Create Product Information File
- Accepted three product names and prices from the user.
- Saved product information in `products.txt`.
- Used the format `ProductName | Price`.
- Read and displayed each line with proper formatting.

### Task 6: Read File Safely
- Asked the user for a filename.
- Checked file existence using `os.path.exists()`.
- Read and printed the file contents if it existed.
- Displayed an error message if the file was not found.

### Task 7: Export Discounted Prices
- Created a dictionary containing five products and their prices.
- Accepted a discount percentage from the user.
- Calculated discounted prices for all products.
- Exported the results to `discount_report.txt`.
- Displayed the report, including total items and average discounted price.

## Concepts Used

- `open()` function
- File modes: `r`, `w`, and `a`
- `read()`, `readline()`, and `readlines()`
- `write()` and `with open()`
- User input using `input()`
- Lists and dictionaries
- Loops and conditional statements
- Type conversion using `int()` and `float()`
- String methods: `strip()` and `split()`
- File existence checks using `os.path.exists()`
- Basic calculations using `sum()`, `max()`, and `min()`

## Requirements

- Python 3.x
- No external libraries required.
- The `os` module is used for checking file existence in Task 6.


## Learning Outcome

This assignment provides practical experience with Python file handling, text file processing, safe file access, user input, and generating simple reports from stored data.
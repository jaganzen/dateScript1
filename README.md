#Version 1 - Date Night Simulator

## Overview

The "Date Night Simulator" is a simple Python script that simulates a date night. It allows you to enter details about your date, set a budget for the evening, and make choices from a menu. The script calculates your remaining budget after each order and determines whether you have enough budget for a second date based on a predefined threshold.

## How to Use

1. **Run the Script:**
   - Make sure you have Python installed on your computer.
   - Clone or download this repository to your local machine.
   - Open a terminal or command prompt and navigate to the directory containing the script (`date_night.py`).
   - You can copy and paste the code into your Jupyter Notebooks as well!

2. **Start the Simulation:**
   - Execute the script by running the following command:
     ```python3 python Date Script.py```

3. **Simulate Your Date Night:**
   - You'll be greeted with a welcome message and prompted to enter the name of the person you're on a date with (used via the input function).

   - Next, you'll be asked to enter your budget for the date in dollars.

   - The script will display the initial budget and a menu of food and drink items with their respective prices.

   - You can choose items from the menu by entering the corresponding number (e.g., '1' for Burger).

   - After each order, the script will update and display your remaining budget.

   - To finish your date night simulation, enter '0'.

4. **Second Date Evaluation:**
   - After completing your date night simulation, the script will evaluate your budget.

   - If you have more than $20.0 remaining, the script will congratulate you and let you know that you have enough budget for a second date.

   - If your remaining budget is $20.0 or less, the script will inform you that your budget is too low for a second date.

## Menu Items

The script offers a menu of food and drink items, each with its respective price:

- Burger - $10.99
- Pizza - $12.99
- Salad - $8.49
- Soda - $2.49
- Wine - $15.99
- Dessert - $6.99

## Criticisms and takeaways

This project is too simplistic and will be updated and can use the inclusion of lists, tuples, or dictionaries along with loops to display options.

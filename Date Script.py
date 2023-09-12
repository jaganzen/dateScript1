def dateNight():
    print("Welcome to your Date Night!")
    partner_name = input("Enter the name of the person you're on a date with: ")
    initial_budget = float(input("Enter your budget for the date: $"))

    # Initialize remaining budget
    remaining_budget = initial_budget

    print(f"\nYou are on a date with {partner_name}.")
    print(f"Initial budget: ${initial_budget:.2f}")

    print("\nMenu:")
    print("1. Burger - $10.99")
    print("2. Pizza - $12.99")
    print("3. Salad - $8.49")
    print("4. Soda - $2.49")
    print("5. Wine - $15.99")
    print("6. Dessert - $6.99")
    
    while True:
        choice = input("Enter the number of your choice (or '0' to finish): ")
        
        if choice == '0':
            break
        elif choice == '1':
            if remaining_budget >= 10.99:
                print("You ordered Burger for $10.99.")
                remaining_budget -= 10.99
            else:
                print("Insufficient funds for Burger. Please choose something else.")
        elif choice == '2':
            if remaining_budget >= 12.99:
                print("You ordered Pizza for $12.99.")
                remaining_budget -= 12.99
            else:
                print("Insufficient funds for Pizza. Please choose something else.")
        elif choice == '3':
            if remaining_budget >= 8.49:
                print("You ordered Salad for $8.49.")
                remaining_budget -= 8.49
            else:
                print("Insufficient funds for Salad. Please choose something else.")
        elif choice == '4':
            if remaining_budget >= 2.49:
                print("You ordered Soda for $2.49.")
                remaining_budget -= 2.49
            else:
                print("Insufficient funds for Soda. Please choose something else.")
        elif choice == '5':
            if remaining_budget >= 15.99:
                print("You ordered Wine for $15.99.")
                remaining_budget -= 15.99
            else:
                print("Insufficient funds for Wine. Please choose something else.")
        elif choice == '6':
            if remaining_budget >= 6.99:
                print("You ordered Dessert for $6.99.")
                remaining_budget -= 6.99
            else:
                print("Insufficient funds for Dessert. Please choose something else.")
        else:
            print("Invalid choice. Please enter a valid number.")

    # Check if there's enough budget for a second date
    if remaining_budget >= 20.0:
        print("\nCongratulations! You have enough budget for a second date.")
    else:
        print("\nSorry, your budget is too low for a second date.")

if __name__ == "__main__":
    dateNight()
    
''''''
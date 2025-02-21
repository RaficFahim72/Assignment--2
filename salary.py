# Function to manage finances
def manage_finances():
    # Ask for salary and month
    salary = float(input("Enter your salary for the month: $"))
    month = input("Enter the month: ")

    # Ask for percentage allocations
    savings_percentage = float(input("Enter the percentage for savings: "))
    rent_percentage = float(input("Enter the percentage for rent: "))
    electricity_percentage = float(input("Enter the percentage for electricity: "))

    # Calculate allocations
    savings_amount = (savings_percentage / 100) * salary
    rent_amount = (rent_percentage / 100) * salary
    electricity_amount = (electricity_percentage / 100) * salary

    # Calculate total expenses
    total_expenses = savings_amount + rent_amount + electricity_amount

    # Calculate remainder
    remainder = salary - total_expenses

    # Yearly estimation for rent and electricity
    yearly_rent_electricity = (rent_amount + electricity_amount) * 12

    # Salary raised to the power of 2
    salary_squared = salary ** 2

    # Monthly additional savings
    additional_savings = 50
    amount_left = additional_savings / savings_amount if savings_amount != 0 else 0

    # Output all results
    print(f"\n--- Financial Summary for {month} ---")
    print(f"Amount allocated to savings: ${savings_amount:.2f}")
    print(f"Amount allocated to rent: ${rent_amount:.2f}")
    print(f"Amount allocated to electricity: ${electricity_amount:.2f}")
    print(f"Total amount spent on savings, rent, and electricity: ${total_expenses:.2f}")
    print(f"Remaining salary after expenses: ${remainder:.2f}")
    print(f"Estimated yearly rent and electricity costs: ${yearly_rent_electricity:.2f}")
    print(f"Your total salary squared: ${salary_squared:.2f}")
    print(f"Amount left when dividing additional savings by total allocated to savings: ${amount_left:.2f}")

# Run the function
manage_finances()
def main():
    print("Welcome to your monthly finance manager, Nabiha!")
    
    # Get user inputs
    salary = float(input("First, please enter your salary for the month: $"))
    month = input("Great! Which month are you storing this salary for? ")
    savings_percentage = float(input("Now, what percentage of your salary would you like to save? "))
    rent_percentage = float(input("What percentage of your salary goes towards rent? "))
    electricity_percentage = float(input("Lastly, what percentage do you spend on electricity? "))

    # Calculate allocations
    savings = (savings_percentage / 100) * salary
    rent = (rent_percentage / 100) * salary
    electricity = (electricity_percentage / 100) * salary

    # Calculate total expenses and remainder
    total_expenses = savings + rent + electricity
    remainder = salary - total_expenses

    # Calculate yearly costs
    yearly_rent = rent * 12
    yearly_electricity = electricity * 12

    # Calculate salary squared
    salary_squared = salary ** 2

    # Assume an additional random savings amount
    additional_savings = 50
    if savings > 0:
        savings_ratio = additional_savings / savings
    else:
        savings_ratio = 0  # Avoid division by zero

    # Output results
    print("\n--- Monthly Financial Summary for {} ---".format(month))
    print("Your total salary for the month: ${:.2f}".format(salary))
    print("Amount allocated to savings: ${:.2f}".format(savings))
    print("Amount allocated to rent: ${:.2f}".format(rent))
    print("Amount allocated to electricity: ${:.2f}".format(electricity))
    print("Total amount spent on savings, rent, and electricity: ${:.2f}".format(total_expenses))
    print("Remaining amount after expenses: ${:.2f}".format(remainder))
    print("Estimated yearly rent cost: ${:.2f}".format(yearly_rent))
    print("Estimated yearly electricity cost: ${:.2f}".format(yearly_electricity))
    print("Just for fun, your salary squared is: ${:.2f}".format(salary_squared))
    print("If you save an additional ${} each month, that would be {:.2f} times your savings allocation.".format(additional_savings, savings_ratio))

    print("Thank you for using the finance manager! Have a great month ahead!")
main()

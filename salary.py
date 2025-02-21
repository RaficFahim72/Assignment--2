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


    print("\nThank you for using the finance manager! Have a great month ahead!")

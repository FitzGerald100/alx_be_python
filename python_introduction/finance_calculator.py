income = float(input("Enter your monthly income: "))
    expenses = float(input("Enter your total monthly expenses: "))

    # Calculate monthly savings
    monthly_savings = income - expenses

    # Project annual savings with interest
    annual_savings = monthly_savings * 12  # Total savings without interest
    interest = annual_savings * 0.05  # Assuming a 5% interest rate
    projected_savings = annual_savings + interest
    
    income = %5000
    expenses = $4000
    montly_savings = $1000
    # Output results
    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

# Call the function to calculate and display savings
calculate_savings()


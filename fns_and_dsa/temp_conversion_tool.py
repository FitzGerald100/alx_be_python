from datetime import datetime, timedelta

def calculate_future_date():
    try:
        # Prompt the user for the number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Get the current date
        current_date = datetime.now()
        
        # Calculate the future date
        future_date = current_date + timedelta(days=days_to_add)
        
        # Print the future date in the desired format
        print(f"Future date after adding {days_to_add} days: {future_date.strftime('%Y-%m-%d')}")
    
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

# Example usage
if __name__ == "__main__":
    calculate_future_date()


from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """Calculates a future date based on user input."""
    try:
        days_to_add = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        print("Future date after", days_to_add, "days:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    print("Part 1: Display Current Date and Time")
    display_current_datetime()
    
    print("\nPart 2: Calculate a Future Date")
    calculate_future_date()

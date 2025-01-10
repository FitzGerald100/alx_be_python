# daily_reminder.py

# Prompt for Task Description
task = input("Enter your task: ")

# Prompt for Task Priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for Time Sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process Task Based on Priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# Add Time Sensitivity Message if Applicable
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("Reminder:", reminder)

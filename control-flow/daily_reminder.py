# daily_reminder.py

# Prompt for Task Description
task = input("What is the task for today? ")

# Prompt for Task Priority
priority = input("What is the priority of this task (high, medium, low)? ").lower()

# Prompt for Time Sensitivity
time_bound = input("Is this task time-sensitive (yes/no)? ").lower()

# Customized Reminder Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"Task: {task} - Priority: High."
    case "medium":
        reminder = f"Task: {task} - Priority: Medium."
    case "low":
        reminder = f"Task: {task} - Priority: Low."
    case _:
        reminder = f"Task: {task} - Priority: Unknown."

# Check Time Sensitivity
if time_bound == "yes":
    reminder += " This requires immediate attention today!"

# Print the customized reminder
print(reminder)

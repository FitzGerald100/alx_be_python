# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Inside the while loop, use a for loop to print asterisks in a row
    for col in range(size):
        print("*", end="")  # Print '*' without a newline
    # After completing a row, print a newline character
    print()  # Move to the next line
    row += 1  # Increment the row counter

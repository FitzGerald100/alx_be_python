# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)  # Ensure input is numeric
        return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)  # Ensure input is numeric
        return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# User interaction
def main():
    while True:
        print("\nTemperature Conversion Tool")
        print("1. Convert Fahrenheit to Celsius")
        print("2. Convert Celsius to Fahrenheit")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            temp = input("Enter the temperature in Fahrenheit: ")
            try:
                converted = convert_to_celsius(temp)
                print(f"{temp}°F is {converted:.2f}°C")
            except ValueError as e:
                print(e)
        elif choice == "2":
            temp = input("Enter the temperature in Celsius: ")
            try:
                converted = convert_to_fahrenheit(temp)
                print(f"{temp}°C is {converted:.2f}°F")
            except ValueError as e:
                print(e)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

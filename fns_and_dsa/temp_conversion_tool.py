# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
        return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    while True:
        print("\nTemperature Conversion Tool")
        temp = input("Enter the temperature to convert (or type 'exit' to quit): ").strip()
        if temp.lower() == 'exit':
            print("Goodbye!")
            break
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == 'C':
            try:
                converted = convert_to_fahrenheit(temp)
                print(f"{temp}°C is {converted:.2f}°F")
            except ValueError as e:
                print(e)
        elif unit == 'F':
            try:
                converted = convert_to_celsius(temp)
                print(f"{temp}°F is {converted:.2f}°C")
            except ValueError as e:
                print(e)
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temp = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        converted = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    elif unit == "C":
        converted = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()




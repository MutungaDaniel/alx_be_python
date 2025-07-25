
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def get_temperature_input():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        return temperature
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")


def main():
    try:
        
        temperature = get_temperature_input()

        
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        
        if unit == 'C':
            new_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {new_temp}°F")
        elif unit == 'F':
            new_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {new_temp}°C")
        else:
            print("Invalid input. Use 'c' or 'f' Kindly")
    
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

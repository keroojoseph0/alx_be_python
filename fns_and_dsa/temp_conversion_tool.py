FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = int(input("Enter the temperature to convert: "))

temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp_type = temp_type.capitalize()

if temp_type == 'F':
    print(f"{temp}°F is {convert_to_celsius(temp)}°C")
elif temp_type == 'C':
    print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")

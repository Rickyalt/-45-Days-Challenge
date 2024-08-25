
def celsius(celsius):
    return (celsius * 9/5) + 32


def fahrenheit(fahrenheit):
    return (fahrenheit - 32) * 5/9

type= input("Enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: ")

if type == 'C' or type=='c':
    in_celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius(in_celsius)
    print(in_celsius,"°C is equal to",fahrenheit,"°F.")

elif type == 'F'or type=='f':
    in_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit(in_fahrenheit)
    print(in_fahrenheit,"°F is equal to",celsius,"°C.")

else:
    print("Invalid input. Please enter 'C' or 'F'.")

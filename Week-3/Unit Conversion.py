def length_conversion(value, from_unit, to_unit):
    length_units = {
        'meter': 1,
        'kilometer': 1000,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }
    
    if from_unit in length_units and to_unit in length_units:
        return value * (length_units[from_unit] / length_units[to_unit])
    else:
        return None

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        'kilogram': 1,
        'gram': 0.001,
        'milligram': 0.000001,
        'pound': 0.453592,
        'ounce': 0.0283495
    }
    
    if from_unit in weight_units and to_unit in weight_units:
        return value * (weight_units[from_unit] / weight_units[to_unit])
    else:
        return None

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return None

def convert(value, from_unit, to_unit, unit_type):
    if unit_type == 'length':
        return length_conversion(value, from_unit, to_unit)
    elif unit_type == 'weight':
        return weight_conversion(value, from_unit, to_unit)
    elif unit_type == 'temperature':
        return temperature_conversion(value, from_unit, to_unit)
    else:
        return None

value = float(input("Enter value: "))
unit_type = input("Enter unit type (length, weight, temperature): ").lower()
from_unit = input("Enter from unit: ").lower()
to_unit = input("Enter to unit: ").lower()

result = convert(value, from_unit, to_unit, unit_type)

if result is not None:
    print(f"{value} {from_unit} is {result:.2f} {to_unit}")
else:
    print("Invalid conversion")

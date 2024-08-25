def sum_of_digits(number):
    total = 0

    while number > 0:

        last_digit = number % 10

        total =total + last_digit
        
        number=number // 10
    
    return total


number = int(input("Enter a number: "))


result = sum_of_digits(number)

print(f"The sum of the digits in",number,"is",result)

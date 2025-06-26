import math


try:
    number = float(input("Enter a number: "))

    if number <= 0:
        print("Note: Square root and logarithm are only defined for positive numbers.")


    if number > 0:
        sqrt_result = math.sqrt(number)
        log_result = math.log(number)
    else:
        sqrt_result = "Undefined"
        log_result = "Undefined"

    sine_result = math.sin(number)

    print(f"Square root: {sqrt_result}")
    print(f"Logarithm: {log_result}")
    print(f"Sine: {sine_result}")

except ValueError:
    print("Please enter a valid number.")

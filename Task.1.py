n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
addition = n1 + n2
subtraction = n1 - n2
multiplication = n1 * n2
if n2 != 0:
    division = n1 / n2
else:
    division = "Undefined (cannot divide by zero)"
print("\nResults:")
print(f"Addition: {n1} + {n2} = {addition}")
print(f"Subtraction: {n1} - {n2} = {subtraction}")
print(f"Multiplication: {n1} * {n2} = {multiplication}")
print(f"Division: {n1} / {n2} = {division}")

#get the User's input
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
operator=input(("Enter the operation (+, -, *, / ):" ))

# Perform the operation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator"

# Display result
print(f"{num1} {operator} {num2} = {result}")
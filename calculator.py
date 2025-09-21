x = float(input("Input the first number ").strip())
y = float(input("Input the second number ").strip())

operator = input("Input the operation you want to perform ").strip()
 
if operator == '+':
    result = x+y
elif operator == '-':
    result = x-y
elif operator == '*':
    result = x*y
elif operator == '/':
    result = x/y
else:
    result = "Error! Unable to read the operator."

print(f"The result is {result}")
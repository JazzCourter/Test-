# Define the function
"greaterThan"
def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False

# Main section of the program
a = 2
b = 3

# Call the function and store the result
result = greaterThan(a, b)

# Print the output
print(f"The statement {a} > {b} is {result}")

# Test scenario 2
a = 10
b = 6

# Call the function and store the result
result = greaterThan(a, b)

# Print the output
print(f"The statement {a} > {b} is {result}")

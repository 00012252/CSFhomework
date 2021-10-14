# Example 1:
def example(num, power=2):  # num and power are parameters
    return num ** power


print(example(2, 3))  # 2, 3 - arguments

# Example 2:
print(example(2))  # value

var = 12
print(example(var))  # variable

print(example(var * 2 - 15))  # expression


# Example 3:
def example(num):
    power = 2  # local variable
    return num ** power


print(example(5))  # 25
print(power)  # Error: name 'power' is not defined
# variable 'power' does not exist outside example

num1 = int(input("insert number 1: "))
num2 = int(input("insert number 2: "))


# Arithmetic operators

# add
add = num1 + num2
print(f"{num1} + {num2} = {add}")

# sus
sus = num1 - num2
print(f"{num1} - {num2} = {sus}")

# prod
prod = num1 * num2
print(f"{num1} * {num2} = {prod}")

# div - used condicional for correct math
if (num2 != 0):
    div = num1 / num2
    print(f"{num1} / {num2} = {div}")
else:
    print("The division by cero isn't posible")

# mod
mod = num1 % num2
print(f"{num1} % {num2} = {mod}")

# Comparation operators
# Greatest than
greatest_than = num1 > num2
print(f"is number 1 greatest than number 2?: {greatest_than}")

# Lessest equal
greatest_equal = num1 >= num2
print(f"is number 1 greatest or equal than number 2?: {greatest_equal}")

# Lessest than
less_than = num1 < num2
print(f"is number 1 lessest than number 2?: {less_than}")

# Lessest equal
lessest_equal = num1 <= num2
print(f"is number 1 lessest or equal than number 2?: {lessest_equal}")

# Equal
equal_than = num1 == num2
print(f"is number 1 equals than number 2?: {equal_than}")

# Diferent
diferent_than = num1 != num2
print(f"is number 1 diferent than number 2?: {diferent_than}")


# Logic Operators
# and
is_true = True and False
print(f"v and f: {is_true}")

is_true = True and True
print(f"v and v: {is_true}")

is_true = False and False
print(f"f and f: {is_true}")

is_true = False and True
print(f"f and v: {is_true}")

# or
is_true = True or False
print(f"v or f: {is_true}")

is_true = True or True
print(f"v or v: {is_true}")

is_true = False or False
print(f"f or f: {is_true}")

is_true = False or True
print(f"f or v: {is_true}")


# Asignation operators =, +=, -=, *=, /=

# Long way
num1 = num1 + num2
 
#Short way
num1 += num2

# Hierarchy
"""

    1. ()
    2. ^ , rad
    3. * , / , %
    4. + , -
    5. > , >= , < , <= , == , !=
    6. = , += , -= , *= , /=

"""

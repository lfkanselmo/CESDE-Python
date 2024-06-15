# Variables

# String
name = "Anselmo"
lastName = "Ortega"

# Int
age = 31
id = 1152197943
weight = 74

# Boolean
anxity = True
money = False

# Float
heigh = 1.71

print(type(name))
print(type(age))
print(type(anxity))
print(type(id))
print(type(heigh))

imc = weight / (heigh**2)
print(imc)

# List
sisters = ["Lei", "Sa", "Anngie"]

print(type(sisters))

# Tuple
week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print(type(week_days))

# Dict
profile = {"Nick": "Krausser", "Type":"Warrior","Level": 99}

print(type(profile))

# Set
colors = {"Black", "Red", "Blue"}

print(type(colors))

# Insert value by keyboard  - Cast with reserved word int
num1 = int(input("Please insert number 1: "))

sum = num1 + 2

print(f"The sum value is: {sum}")


# Funtion with return
def add(num1):
    return num1 + 2

print(f"The 'add' funtion result is: {add(num1)}")
# if

# if - else

isCorrect = True

if isCorrect:
    print("it's correct")
else:
    print("it's not correct")

# elif (If anidados)

num1 = int(input("insert number 1: "))
num2 = int(input("insert number 2: "))

print("\n\nSelect 1. add\n 2. res\n 3. prod \n 4. div \n")

sel = int(input("Select option: "))
if sel == 1:
    add = num1 + num2
    print(f"{num1} + {num2} = {add}")
elif sel == 2:
    res = num1 - num2
    print(f"{num1} - {num2} = {res}")
elif sel == 3:
    prod = num1 * num2
    print(f"{num1} * {num2} = {prod}")
elif sel == 4:
    if num2 != 0:
        div = num1 / num2
        print(f"{num1} / {num2} = {div}")
    else:
        print("Undetermined")
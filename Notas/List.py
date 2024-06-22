# Data structure List
#            0        1       2       3         4
my_list = ["blue", "white", "red", "yellow", "green"]


print(my_list[1])

my_list[1] = "grey"

print(my_list[1])

my_list.append("black")

print(my_list)

# slicing

numbers = [1,2,3,4,5,6,7,8,9]

print(numbers[5:8])
print(numbers[1:-5])

for num in numbers:
    print(num)

for i in range(len(numbers)):
    print(numbers[i])

while num < len(numbers):
    if num in numbers:
        print(num)
    num+=1
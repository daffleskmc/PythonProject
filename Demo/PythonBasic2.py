if 5 > 3:
    print("5 is greater than 3")

num = 0
if num > 0:
    print("This is a positive number")
elif num == 0:
    print("number is zero")
else:
    print("This is a negative number")

num = [1,2,3,4,5]
sum = 0

for val in num:
    sum = sum + val

print("Total is ", sum)

fruits = ["apple" "oranges", "grapes"]

for val in fruits:
    print(val)
else:
    print("No more fruits left")

print("Enter a number: ")
num = int(input())
sum = 0
i = 1

while i < num:
    sum = sum + i
    i = i + 1
print("Total is ", sum)
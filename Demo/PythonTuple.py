
my_tuple = ("Apples", "Watermelon", "Mango")
print(my_tuple)
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[0:2])

for val in my_tuple:
    print(val)

print(len(my_tuple))

my_tuple_2 = ("Banana", "Avocado", (1,2,3), ["Tokyo", "Osaka"])
print(my_tuple_2)
print(my_tuple_2[3][1])

my_tuple_2[3][1] = "Sydney"
print(my_tuple_2)

print("Banana" in my_tuple_2)
print("Cherry" in my_tuple_2)
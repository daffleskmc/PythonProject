my_sets = {"Blue", "Black", "White"}
print(my_sets)

for x in my_sets:
    print(x)

print("White" in my_sets)

my_sets.add("Red")
print(my_sets)
my_sets.update(["Green", "Pink"])
print(my_sets)

len(my_sets)

my_sets.remove("Blue")
print(my_sets)
my_sets.discard("Red")
print(my_sets)
# my_sets.remove("Blue")
my_sets.discard("Red")

my_sets.pop()
my_sets.clear()
print(my_sets)

del my_sets

my_sets_2 = {"Apples", 1,2, (3,4,5)}
print(my_sets_2)

my_list = [1,2,3]
print(my_list)
my_sets_3 = set(my_list)
print(my_sets_3)

# UNION | Intersection | Diff | Symmetric Diff
A = {'A', 'B', 1, 2, 3}
B = {'B', 'C', 3, 4, 5}

print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)

print(A.symmetric_difference(B))
print(A ^ B)
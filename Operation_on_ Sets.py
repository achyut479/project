my_set = {1,2,2,3,4,4,4}
print("set :", my_set)

my_set.add(5)
print("update set :", my_set)

set1 = my_set
set2 = {2,4,4,6}

print("\nset 1", set1)
print("set 2", set2)
print("difference")
print(set1.difference(set2))
print("symmeteric difference")
print(set1.symmeteric difference(set2))

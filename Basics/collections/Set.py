# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)  # adds one set to another
# print()
# for x in dishes:
#     print(x)
print(utensils.difference(dishes))
print()
print(dishes.difference(utensils))
print()
print(utensils.intersection(dishes)) #returns elements that both sets have in common
print()

dinner_table=utensils.union(dishes) #combines 2 sets into a new set
print("dinner_table items:")
for x in dinner_table:
    print(x)

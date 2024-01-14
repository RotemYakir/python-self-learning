# sort() method   = used with lists
# sort() function = used with iterables

# https://youtu.be/XKHEtdqhLK8?t=17323

# students = [("Squidward", "F", 60),  # list of tuples
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr.Krabs", "C", 78)]

# grade=lambda grades:grades[1]
# students.sort(key=grade,reverse=True)
# age = lambda ages:ages[2]
# students.sort(key=age)
#
# for i in students:
#     print(i)

students = (("Squidward", "F", 60),  # tuple of tuples
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

age = lambda ages: ages[2]
sorted_by_age = sorted(students,key=age)

for i in sorted_by_age:
    print(i)
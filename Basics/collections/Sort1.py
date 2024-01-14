# sort() method   = used with lists
# sort() function = used with iterables

# https://youtu.be/XKHEtdqhLK8?t=17162

students_list = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]
students_tuple = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")

# students_list.sort(reverse=True)
students_list.sort()  # will not work on a tuple
# sorted_students_tuple = sorted(students_tuple,reverse=True)
sorted_students_tuple = sorted(students_tuple)

for i in sorted_students_tuple:
    print(i)


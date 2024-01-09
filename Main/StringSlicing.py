# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]
print("indexing:")
name = "Rotem Yakir"

# first_name = name[0:5:1]  # the stopping index is exclusive
first_name = name[:5]  # [start:stop:step]
# last_name = name[6:11]
last_name = name[6:]  # [start:stop:step]
# funny_name=name[0:11:3]
funny_name = name[::3]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funny_name)
print(reversed_name)

print()
print("slice():")

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice=slice(7,-4)

print(website1[slice])
print(website2[slice])

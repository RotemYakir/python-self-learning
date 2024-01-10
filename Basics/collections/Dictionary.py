# Dictionary = A changeable, unordered collection of unique key:value pairs.
#              Fast because the use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Israel':'Jerusalem'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
# capitals.clear()

# print(capitals['Russia'])
print(capitals.get('Russia'))
# print(capitals['Germany']) # will make an error
print(capitals.get('Germany'))  # will return None

print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals)

for key, value in capitals.items():
    print(key, value)

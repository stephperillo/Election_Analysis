# one dimensional data it could be a row or column
# list

#these square brackets will always tell you have a list
# how to create a list
names = ["Adams", "Alicia", "Jadon", "Luis"]
print(type(10))

# this list has different types of items
random_stuff = [10, "bob", False, True]

# how to read a list
print(random_stuff)

# how to read an individual item
print(names[2])

# how to update a list
names[2] = "Amy"

print(names)

names.append("Alberto")
print(names)

# delete
names.remove("Amy")
print(names)

names.pop(1)
print(names)

# alphabetize
names.sort()
print(names)

# mutable => can you be changed

# tuple are not mutable . tuple is ()

nuclear_launch_codes = (0, "mohan", "xyz12")

print(nuclear_launch_codes[1])
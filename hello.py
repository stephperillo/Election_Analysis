print('Hello')
name = "Mohan"
print(name)
isCarOwner = True

# python 2.X
print(name + " owns a car ")

# python 3.X
print(f"{name} owns a car")

age = 15

# Is python smart enough to convert an intger to a string
print(f"(Mohan is str(age) years old")

print(f"Mohan is {age} years old")

age = 1 + 10
print(f"Mohan is {age} years old {isCarOwner}")

print(f"Mohan is {age * 10 + 5} years old {isCarOwner}")

name = "Stephanie"
country = "United States"
hourly_wage = 15
daily_wage = hourly_wage * 8
print(daily_wage)
satisfied = True
print("You live in" + country)
print(f"You make {daily_wage} per day")
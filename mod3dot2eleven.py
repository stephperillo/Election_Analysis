# f strings
    #og code
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#f string (and remove percentage_votes line)
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# f strings with dicts
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# formatting floating pt decimals
f'{value:{width}.{precision}}'
# width is num chars
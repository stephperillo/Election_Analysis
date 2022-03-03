voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# to print counties using range() to iterate over the list of dictionaries
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

# to get vals from dict in list of dict, use a nested for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# to get num of registered voters from each dict
for county_dict in voting_data:
     print(county_dict['registered_voters'])

# to get county name from each dict
for county_dict in voting_data:
    print(county_dict['county'])
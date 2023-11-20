state_names = ['Arizona', 'California', 'California', 'Kencutcky', 'Louisiana']
county_names = ['Maricopa', 'Alameda', 'Sacramento', 'Jefferson', 'East Baton Rouge']
state_county_tuples = zip(state_names, county_names)

# For loop implementation
ca_counties_loop = []
for state, county in state_county_tuples:
    if state == 'California':
        ca_counties_loop.append(county)

print (ca_counties_loop)

# List Comprehension Implementation
ca_counties_listcomp = []
ca_counties = [county for (state, county) in state_county_tuples if state == 'Cal    ifornia']
print(ca_counties_listcomp)

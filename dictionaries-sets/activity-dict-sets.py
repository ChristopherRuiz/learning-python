epa_tuple_loop = list()

## loop to create list of tuples with record looking lik: (state, county, aqi)
for i in range(len(state_list)):
    epa_tuple_loop.append((state_list[i], county_list[i], aqi_list[i]))

#epa_tuple_loop


## zip to do same thing
if len(state_list) == len(county_list) == len(aqi_list):
    print("Size of all lists are the same:")
    print(f"Length of state_list = {len(state_list)}")
    print(f"Length of county_list = {len(county_list)}")
    print(f"Length of aqi_list = {len(aqi_list)}")
    epa_tuple = zip(state_list, county_list, aqi_list)    # zip only works if each list is same size
    print(list(epa_tuple))
else:
    print("List lengths did not match. ")



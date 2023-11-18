team = [
	('Bill', 20, 'center'),
	('Will', 22, 'point guard'),
	('Phil', 19, 'center')
]

# Create dict from tuple team
new_team = {}
for name, age, position in team:
	if position in new_team:
		new_team[position].append((name, age))
	else: 	
		new_team[position] = [(name, age)]

new_team 

# keys()  retireve keys
new_team.keys()

# values() retriece values
new_team.values()

# items() retrieve both keys and values
new_team.items()

# Loop to retrieve items in easier to view format
for a, b in new_team.items():
	print(a, b)


# Instatiate a set
set = {5, 10, 10, 20} 	# can only instantioate set like this if has values

# to create empty list use set()
empty_set = set()

# Performing Union
set_1 = {'a', 'b', 'c'}
set_2 = {'b', 'c', 'd'}

print(set_1.union(set_2))	# Prints: {'b', 'c', 'd', 'a'}
print(set_1 | set_2)		# prints same as above. Uses union operator '|'

# Intersection
set_1 = {'a', 'b', 'c'}
set_2 = {'b', 'c', 'd'}

print(set_1.intersection(set_2))
print(set_1 & set_2) 

# Difference
set_1 = {'a', 'b', 'c'}		
set_2 = {'b', 'c', 'd'}		

print(set_1.difference(set_2))	# {'a'}
print(set_1 - set_2)			# {'a'}

# Symmetric Difference
set_1 = {'a', 'b', 'c'}
set_2 = {'b', 'c', 'd'}

print(set_1.symmetric_difference(set_2))	# {'d', 'a'}
print(set_1 ^ set_2)						# {'d', 'a'}

# Specify the file path
file_name = 'sample-d3.txt'

# Initialize an empty list to store the grid
schematics = []

# Open the file and read its content
with open(file_name, 'r') as file:
    for line in file:
        # Remove newline characters and append each character as a list
        row = list(line.strip())
        schematics.append(row)

# Now, 'grid' contains the data from the file
# You can print it to verify
for row in schematics:
    print(row)

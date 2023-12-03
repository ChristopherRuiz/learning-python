import re

letter_to_digit = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

# Example string
input_string = "neightwompstbkqv1fourfthdcfgtrkqzgrbfrczxbdn"

# Replace spelled-out words with digits
for word, digit in letter_to_digit.items():
    input_string = input_string.replace(word, digit)

ans_list = []

# Find all single digits in the modified string and add to a list
strint = [digit for digit in re.findall(r'\d', input_string)]

for digit in strint:
    combined_strint = digit + digit
    ans_list.append(combined_strint)
    print(f"{combined_strint} was added to the answer list")

# Sum up the numbers in the answer list
result = sum(int(num) for num in ans_list)
print(f"Final result: {result}")

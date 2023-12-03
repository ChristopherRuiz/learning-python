import re

### Challenge 1:
## Find first and last numbers in a string and combine to form single two digit number (i.e 34dsf85k6 == 36)
## If there is only one number, use itseld to form two digit number (i.e adf5ds == 55)

# Read in file containing words and variable instantiation
word_list = open("day1input.txt").read().split()
ans_list = []

# for word in word_list:
#     # find all single digits in the word and add to a list (i.e 352dsf53k8 == ['3', '5', '2', '5', '3', '8'])
#     strint = [digit for digit in re.findall(r'\d', word)]

#     if len(strint) == 1:
#         combined_strint = strint[0] + strint[0]
#         ans_list.append(combined_strint)
#     else:
#         combined_strint = strint[0] +  strint[-1]
#         ans_list.append(combined_strint)

# print(sum(map(int, ans_list)))

### Challenge Two:
## Numbers written out are to be included (i.e zoneight234 == 14)

letter_to_digit = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

# Create a new list to store the modified words
modified_word_list = []

for word in word_list:
    for key, value in letter_to_digit.items():
        word = word.replace(key, value)
    modified_word_list.append(word)


# Now, modified_word_list contains the words with spelled-out numbers replaced by digits
print(modified_word_list)

# for word in word_list:
#     for word_index, word in enumerate(word_list):
#         for key, value in letter_to_digit.items():
#             if key in word:
#                 word_list[word_index] = word.replace(key, value)
                
        
# for word in word_list:
#     # find all single digits in the word and add to a list (i.e 352dsf53k8 == ['3', '5', '2', '5', '3', '8'])
#     strint = [digit for digit in re.findall(r'\d', word)]

#     if len(strint) == 1:
#         combined_strint = strint[0] + strint[0]
#         ans_list.append(combined_strint)
#         print(f"{combined_strint} was added to the answer list")
#     else:
#         combined_strint = strint[0] +  strint[-1]
#         ans_list.append(combined_strint)
#         print(f"{combined_strint} was added to the answer list") 

# print(sum(map(int, ans_list)))

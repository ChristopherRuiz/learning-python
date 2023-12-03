import re

def find_digits(word):
    digits = re.findall(r'\d', word)
    return int(digits[0] * 2) if len(digits) == 1 else int(digits[0] + digits[-1])

def main():
    with open("day1input.txt", "r") as file:
        word_list = file.read().split()

    ans_list = [find_digits(word) for word in word_list]

    total_sum = sum(ans_list)
    print(total_sum)

if __name__ == "__main__":
    main()


from collections import Counter

string = input()
substring_length = int(input())
string_length = len(string)

count_substrings = dict(Counter(string[index: index + substring_length] for index in range(string_length - 1)))
print(sorted([substring[0] for substring in count_substrings.items() if substring[1] > 1]))

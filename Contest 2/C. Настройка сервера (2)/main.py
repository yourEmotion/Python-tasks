max_length = int(input())
string = input()

string_length = len(string)

print(string[:max_length])
for index in range(max_length, string_length):
    print('&' * (max_length - 1) + string[index])
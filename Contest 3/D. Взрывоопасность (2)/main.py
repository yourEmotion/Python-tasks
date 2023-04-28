number_of_permutations = [1, 3]

N = int(input())

for index in range(2, N + 1):
    number_of_permutations.append((number_of_permutations[index - 1] + number_of_permutations[index - 2]) * 2)

print(number_of_permutations[N])

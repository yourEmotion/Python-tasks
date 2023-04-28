def to_roman(dec_num):
    dec_num_list = (dec_num // 10, dec_num % 10)
    roman_num = 'X' * dec_num_list[0]
    if 0 <= dec_num_list[1] <= 3:
        roman_num += 'I' * dec_num_list[1]
    elif dec_num_list[1] == 4:
        roman_num += 'IV'
    elif 5 <= dec_num_list[1] <= 8:
        roman_num += 'V' + 'I' * (dec_num_list[1] - 5)
    else:
        roman_num += 'IX'
    return roman_num


lines = ('alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa')
columns = tuple(to_roman(num) for num in range(1, 31))

a = int(input())
b = int(input())

if a * b > 0:
    for line in lines[:a]:
        for column in columns[:(b-1)]:
            print('{}_{}'.format(line, column), end=' ')
        print('{}_{}'.format(line, columns[b-1]))

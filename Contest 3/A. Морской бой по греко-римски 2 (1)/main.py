def to_roman(dec_num: int) -> str:
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


def get_key(dictionary: dict, expected_value: str) -> int:
    for key, value in dictionary.items():
        if value == expected_value:
            return key
    return 0


point_coordinates = input().split('_')

lines = {1: 'alpha',
         2: 'beta',
         3: 'gamma',
         4: 'delta',
         5: 'epsilon',
         6: 'zeta',
         7: 'eta',
         8: 'theta',
         9: 'iota',
         10: 'kappa'}

columns = dict((index, to_roman(index)) for index in range(1, 31))

print(get_key(lines, point_coordinates[0]), get_key(columns, point_coordinates[1]))

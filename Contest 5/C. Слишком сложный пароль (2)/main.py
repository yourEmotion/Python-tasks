from string import ascii_lowercase as lc, ascii_uppercase as uc, digits


def is_strong(s: str) -> bool:
    set_string = set(s)
    return bool(set_string.intersection(lc)) and bool(set_string.intersection(uc)) and\
        bool(set_string.intersection(digits))


def is_memorable(s: str) -> bool:
    return len(s) <= 10 and sum(s.count(digit) for digit in digits) <= 3


with open('input.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        string = input_file.read()

        if is_strong(string):
            output_file.write('YES\n')
        else:
            output_file.write('NO\n')

        if is_memorable(string):
            output_file.write('YES')
        else:
            output_file.write('NO')

with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line in input_file.readlines():
        data = line.split('\t')
        sha_1 = data[0]
        message = data[-1] if data[-1][-1] != '\n' else data[-1][:-1]
        dots = '.' * (73 - len(message))
        output_file.write('{}{}{}\n'.format(sha_1[:7], dots, message))

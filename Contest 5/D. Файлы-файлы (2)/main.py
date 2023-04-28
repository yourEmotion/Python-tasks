templates = ('.hlm', '.brhl')
with open('input.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        for line in input_file:
            for word in line.split():
                if word.startswith('.') or '..' in word or word != word.lower():
                    continue
                for template in templates:
                    if word.endswith(template):
                        output_file.write(word + '\n')
                    if word.endswith(template + '.'):
                        output_file.write(word[:-1] + '\n')
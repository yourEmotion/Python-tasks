screen_width = int(input())
max_count_words_in_line = int(input())

result_string = ''
count_words_in_current_line = 0
length_of_current_line = 0
while True:
    current_word = input()
    if current_word == '0':
        break
    if count_words_in_current_line < max_count_words_in_line\
            and len(current_word) + length_of_current_line + (1 if (count_words_in_current_line > 0) else 0)\
            <= screen_width:
        result_string += ' ' * (count_words_in_current_line > 0) + current_word
        length_of_current_line += len(current_word) + (1 if (count_words_in_current_line > 0) else 0)
        count_words_in_current_line += 1
    else:
        result_string += '\n{}'.format(current_word)
        length_of_current_line = len(current_word)
        count_words_in_current_line = 1

print(result_string)

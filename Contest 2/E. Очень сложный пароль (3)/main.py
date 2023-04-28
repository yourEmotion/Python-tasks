index = int(input())
current_index = 0
number = 0
while True:
    if str(number).count('3') == 3:
        current_index += 1
        if current_index == index:
            print(number)
            break
    number += 1

string = input()
print(*tuple(string[i].lower() if (i % 2 == 0) else string[i].upper() for i in range(len(string))), sep='')

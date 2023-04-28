from sys import stdout

print('? 1000000 1000000')
dist_1 = int(input())
print('? -1000000 1000000')
dist_2 = int(input())
print('! {} {}'.format((dist_2 - dist_1) // 2, -(dist_1 + dist_2) // 2 + 2 * 10 ** 6))

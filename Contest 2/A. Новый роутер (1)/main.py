def is_column_in_unavailable_area(point_A, point_B, point_C):
    if point_C['x'] > point_A['x'] and point_C['x'] > point_B['x']:
        return True
    if point_C['y'] > point_A['y'] and point_C['y'] > point_B['y']:
        return True
    if point_C['x'] < point_A['x'] and point_C['x'] < point_B['x']:
        return True
    if point_C['y'] < point_A['y'] and point_C['y'] < point_B['y']:
        return True
    return False


x = int(input())
y = int(input())
point_A = {'x': x, 'y': y}

x = int(input())
y = int(input())
point_B = {'x': x, 'y': y}

x = int(input())
y = int(input())
point_C = {'x': x, 'y': y}

if is_column_in_unavailable_area(point_A, point_B, point_C):
    sym_point_A = {'x': 2 * point_C['x'] - point_A['x'], 'y': 2 * point_C['y'] - point_A['y']}
    sym_point_B = {'x': 2 * point_C['x'] - point_B['x'], 'y': 2 * point_C['y'] - point_B['y']}
    print(sym_point_A['x'], sym_point_A['y'], sym_point_B['x'], sym_point_B['y'], sep='\n')
else:
    print('False')

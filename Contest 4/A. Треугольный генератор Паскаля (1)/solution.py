def pascal_triangle():
    row = [1]
    while True:
        for element in row:
            yield element
        row = [0] + row + [0]
        new_row = []
        for index in range(len(row) - 1):
            new_row.append(row[index] + row[index + 1])
        row = new_row

def pascal_triangle(rows):
    row = [1]
    for i in range(rows):
        for element in row:
            yield element
        row = [0] + row + [0]
        new_row = []
        for index in range(len(row) - 1):
            new_row.append(row[index] + row[index + 1])
        row = new_row


print(*pascal_triangle(10))

def print_letters(rows: int, columns: int) -> None:
    for _ in range(rows - 1):
        print('*   * ' * (columns - 1) + '*   *')
        print('*  ** ' * (columns - 1) + '*  **')
        print('* * * ' * (columns - 1) + '* * *')
        print('**  * ' * (columns - 1) + '**  *')
        print('*   * ' * (columns - 1) + '*   *')
        print()
    print('*   * ' * (columns - 1) + '*   *')
    print('*  ** ' * (columns - 1) + '*  **')
    print('* * * ' * (columns - 1) + '* * *')
    print('**  * ' * (columns - 1) + '**  *')
    print('*   * ' * (columns - 1) + '*   *')


a, b = int(input()), int(input())
print_letters(a, b)

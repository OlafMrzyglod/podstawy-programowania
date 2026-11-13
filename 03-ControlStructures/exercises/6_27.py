row_base = 6
while row_base >= 0:
    column = 1
    while column <= 3:
        print(row_base + column, end=" ")
        column += 1
    print()
    row_base -= 3

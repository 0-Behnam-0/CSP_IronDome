def pretty_matrix(matrix):

    row_break = len(matrix[0])

    wise_list = []
    for row in matrix:
        for wise in row:
            wise_list.append(wise)

    max_col_length_list = []
    row_index = 0
    while row_index < row_break:
        col_index = row_index
        col_list = []
        while col_index < len(wise_list):
            col_list.append(str(wise_list[col_index]))
            col_index += row_break
        max_col_length_list.append(len(max(col_list, key=len)))
        row_index += 1

    row_length = 0
    for ele in max_col_length_list:
        row_length = row_length + ele
    row_length = row_length + 2*(1+len(max_col_length_list)) - 4

    cnt = 1
    print("       ", end="")
    for ele in max_col_length_list:
        print("t"+ str(cnt), end="")
        print(ele*" ", end="")
        cnt += 1
    print()

    print("   +-- " + row_length*" " + " --+")

    cnt = 1
    for row in matrix:
        index = 0
        print("s"+ str(cnt) +" ¦ ", end="")
        for wise in row:
            padding = max_col_length_list[index] - len(str(wise))
            print("  " + str(wise), end="")
            print(padding*" ", end="")
            index += 1
        cnt += 1
        print("   ¦")

    print("   +-- " + row_length*" " + " --+")

    if len(matrix)>=10 or len(matrix[0])>=10: print("Note: 9x9 limited!")

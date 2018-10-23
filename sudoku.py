def check_sudoku(p):
    n = len(p) # get size of grid
    digit = 1 #start with 1
    while digit <= n: # go through each digit
        i = 0
        while i < n: # go through each row and column at the same time
            row_count = 0
            col_count = 0
            j = 0
            while j < n: #for each entry in ith row/column
                if p[i][j] == digit: #check row count
                    row_count += 1
                if p[j][i] == digit:
                    col_count += 1
                j += 1
            if row_count != 1 or col_count != 1:
                return False
            i += 1 # next row/column
        digit += 1 #next digit
    return True #nothing was wrong, it's a valid sudoku board

def find_next_empty(puzzle):
    # find next row and column that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # We're using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None # If no spaces in the puzzle are empty (-1), we've solved it!

def is_valid(puzzle, guess, row, col):
    # check if the guess is valid for the row, col
    # return True if it is valid, False if it's not
    # check row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # check col
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # The square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # If we reach this point, we're good!
    return True

def solve_sudoku(puzzle):
    # Solve the sudoku puzzle using backtracking
    # our puzzle is a list of lists, where each inner list a row in our sudoku puzzle
    # return wether a solution exists or not
    # mutate the puzzle to contain the solution if it exists

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there is no empty space, we've solved the puzzle
    if row == None:
        return True

    # step 2: try all possible values for the empty space
    for guess in range(1, 10):
        # step 3: if the guess is valid, make a recursive call
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # recurse using this puzzle
            # step 4: recursively call solve_sudoku
            if solve_sudoku(puzzle):
                return True

        # step 5: if the guess is invalid, backtrack and try another guess
        puzzle[row][col] = -1 # reset guess
    
    # step 6: if we reach this point, we've tried all possible guesses and none of them worked
    return False

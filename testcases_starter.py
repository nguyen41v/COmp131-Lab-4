from connect_four import str_to_board, print_board, has_connect_four, lowest_empty_row

def fail(board):
    print("FAIL on ")
    print_board(board)
    exit(1)

def main():
    # HAS_CONNECT_FOUR TEST CASES

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  _  _  _  _  _ |
    4  | _  _  _  _  _  _  _ |
    5  | _  _  _  _  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  _  _  _  _  _ |
    4  | _  _  _  _  _  _  _ |
    5  | X  X  X  X  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | O  O  O  O  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  _  _  _  _  _ |
    4  | _  _  _  _  _  _  _ |
    5  | O  X  X  X  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | O  O  O  X  X  X  X |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  _  _  _  _  _ |
    4  | _  _  _  _  _  _  _ |
    5  | O  X  X  X  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | O  O  O  X  X  O  X |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  _  _  _  _  _ |
    4  | _  _  _  _  _  _  _ |
    5  | O  X  _  X  X  X  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  X  _  _ |
    2  | X  _  _  _  _  _  _ |
    3  | X  _  _  X  X  _  X |
    4  | X  _  X  X  _  _  _ |
    5  | X  _  _  X  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)
    board = str_to_board('''
    0  | X  _  _  _  _  _  _ |
    1  | X  _  _  _  X  _  _ |
    2  | X  _  _  _  _  _  _ |
    3  | X  _  _  X  X  _  X |
    4  | _  _  X  X  _  _  _ |
    5  | _  _  _  X  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  X |
    1  | _  _  _  _  X  _  X |
    2  | _  _  _  _  _  _  X |
    3  | _  _  _  X  X  _  X |
    4  | _  _  X  X  _  _  _ |
    5  | _  _  _  X  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | _  _  _  X  _  _  _ |
    1  | _  _  _  _  X  _  X |
    2  | _  _  _  _  _  X  X |
    3  | _  _  _  X  _  _  X |
    4  | _  _  X  X  _  _  _ |
    5  | _  _  _  X  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')

    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  X  _  X |
    2  | _  _  _  X  _  X  X |
    3  | _  _  _  X  X  _  X |
    4  | _  _  X  _  _  X  _ |
    5  | _  _  _  X  _  _  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  X  _  X |
    2  | X  _  _  X  _  X  X |
    3  | _  X  _  X  _  _  X |
    4  | _  _  X  _  _  X  _ |
    5  | _  _  _  X  _  _  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | X  _  _  _  _  _  _ |
    1  | _  X  _  _  X  _  X |
    2  | _  _  X  X  _  X  X |
    3  | _  X  _  X  _  _  X |
    4  | _  _  X  _  _  X  _ |
    5  | _  _  _  X  _  _  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | X  _  _  X  _  _  _ |
    1  | _  X  X  _  _  _  X |
    2  | _  X  _  X  _  X  X |
    3  | X  X  _  X  _  _  X |
    4  | _  _  X  _  _  X  _ |
    5  | _  _  _  X  _  _  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | X  _  _  X  _  _  _ |
    1  | _  O  O  _  _  _  X |
    2  | _  X  _  X  _  X  X |
    3  | X  O  X  X  _  _  X |
    4  | _  X  X  _  _  X  _ |
    5  | X  _  _  X  _  _  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | X  _  _  X  _  _  _ |
    1  | _  O  X  _  _  _  X |
    2  | _  X  _  X  _  X  X |
    3  | X  O  X  X  O  X  X |
    4  | _  O  X  _  X  X  _ |
    5  | X  _  _  X  _  _  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | X  _  _  X  _  _  X |
    1  | _  O  X  _  X  X  X |
    2  | _  X  _  X  X  X  O |
    3  | X  O  X  X  _  _  X |
    4  | _  O  O  _  X  X  _ |
    5  | X  _  _  X  _  _  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)


    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  O  X  _  _ |
    3  | _  _  O  X  X  O  X |
    4  | _  _  X  O  O  O  X |
    5  | _  X  X  O  O  X  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)


    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  _  _  _  _  _ |
    4  | _  _  _  _  _  _  _ |
    5  | O  X  X  X  X  O  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | O  O  O  O  O  O  O |
    1  | O  O  O  O  O  O  O |
    2  | O  O  O  O  O  O  O |
    3  | O  O  O  O  O  O  O |
    4  | O  O  O  O  O  O  O |
    5  | O  O  O  O  O  O  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')

    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  O  X  _  _  _  _ |
    3  | _  O  O  _  _  _  _ |
    4  | _  O  X  O  _  _  _ |
    5  | X  O  X  X  O  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
     0  | _  _  _  _  _  _  _ |
     1  | _  _  _  _  _  _  _ |
     2  | _  _  _  _  _  _  _ |
     3  | _  O  _  _  _  _  _ |
     4  | _  O  X  O  _  _  _ |
     5  | X  O  X  X  O  _  _ |
        +---------------------+
          0  1  2  3  4  5  6
     ''')
    if has_connect_four(board):
        fail(board)
    board = str_to_board('''
     0  | _  _  _  _  _  _  _ |
     1  | _  _  _  _  _  _  _ |
     2  | _  _  _  _  _  _  _ |
     3  | _  O  _  _  _  _  _ |
     4  | _  O  _  O  O  _  _ |
     5  | X  X  X  X  X  _  _ |
        +---------------------+
          0  1  2  3  4  5  6
     ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
     0  | _  _  _  _  _  _  _ |
     1  | _  _  _  _  _  _  _ |
     2  | _  _  _  _  _  _  _ |
     3  | _  O  _  _  _  _  _ |
     4  | O  O  O  _  O  _  _ |
     5  | X  X  X  X  X  X  X |
        +---------------------+
          0  1  2  3  4  5  6
     ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  O  _  _  _  _  _ |
    4  | O  O  _  _  O  _  _ |
    5  | X  X  X  X  X  X  _ |
       +---------------------+
         0  1  2  3  4  5  6
         ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  X  _  _ |
    2  | _  _  _  X  O  X  _ |
    3  | O  O  X  O  X  O  _ |
    4  | O  X  O  O  O  X  _ |
    5  | X  X  X  O  X  X  _ |
       +---------------------+
         0  1  2  3  4  5  6
         ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | _  _  _  _  _  X  _ |
    1  | _  _  _  _  X  O  _ |
    2  | _  _  _  X  O  X  _ |
    3  | O  O  X  O  X  O  _ |
    4  | O  X  O  O  O  X  _ |
    5  | X  X  X  O  X  X  _ |
       +---------------------+
         0  1  2  3  4  5  6
         ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | X  O  X  O  X  O  X |
    1  | X  O  X  O  X  O  X |
    2  | O  X  O  X  O  X  O |
    3  | O  X  O  X  O  X  O |
    4  | X  O  X  O  X  O  X |
    5  | X  O  X  O  X  O  X |
       +---------------------+
         0  1  2  3  4  5  6
         ''')
    if has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | X  X  X  X  O  O  X |
    1  | X  O  X  O  X  O  X |
    2  | O  X  O  X  O  X  O |
    3  | O  X  O  X  O  X  O |
    4  | X  O  X  O  X  O  X |
    5  | X  O  X  O  X  O  X |
       +---------------------+
         0  1  2  3  4  5  6
         ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | O  X  X  X  O  O  X |
    1  | X  O  X  O  X  O  X |
    2  | O  X  O  X  O  X  O |
    3  | O  X  O  O  O  X  O |
    4  | X  O  X  O  X  O  X |
    5  | X  O  X  O  X  O  X |
       +---------------------+
         0  1  2  3  4  5  6
         ''')
    if not has_connect_four(board):
        fail(board)

    board = str_to_board('''
    0  | X  X  X  X  X  O  X |
    1  | X  O  X  O  X  O  X |
    2  | O  X  O  X  O  X  O |
    3  | O  X  O  X  O  X  O |
    4  | X  O  X  O  X  O  X |
    5  | X  O  X  O  X  O  X |
       +---------------------+
         0  1  2  3  4  5  6
             ''')
    if not has_connect_four(board):
        fail(board)
    board = str_to_board('''
     0  | _  _  _  _  _  _  _ |
     1  | _  _  _  _  _  _  _ |
     2  | _  _  _  _  _  _  _ |
     3  | _  O  _  _  _  _  _ |
     4  | O  O  O  _  O  _  _ |
     5  | X  X  X  O  X  X  X |
        +---------------------+
          0  1  2  3  4  5  6
     ''')
    if has_connect_four(board):
        fail(board)


    # LOWEST_EMPTY_ROW TEST CASES

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  O  X  _  _  _  _ |
    3  | _  O  O  _  _  _  _ |
    4  | _  O  X  O  _  _  _ |
    5  | X  O  X  X  O  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')

    if lowest_empty_row(board, 0) != 4:
        fail(board)

    board = str_to_board('''
    0  | O  O  O  O  O  O  O |
    1  | O  _  _  _  _  _  O |
    2  | O  _  _  _  _  _  O |
    3  | O  _  _  _  _  _  O |
    4  | O  _  _  _  _  _  O |
    5  | O  O  O  O  O  O  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 0) != -1:
        fail(board)



if __name__ == "__main__":
    main()

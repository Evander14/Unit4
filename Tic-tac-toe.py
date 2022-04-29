#tic tak toe
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]

#board
def print_board():
    print(
        f"{board[0][0]} | {board[0][1]} | {board[0][2]} \n"
        "---------\n"
        f"{board[1][0]} | {board[1][1]} | {board[1][2]} \n"
        "---------\n"
        f"{board[2][0]} | {board[2][1]} | {board[2][2]} \n"
    )
#player turns
def player_turn(name, symbol):
    valid_spot = False
    while not valid_spot:
        valid_row = False
        while not valid_row:
            row_choice = int(input(f"{name}, it is your turn to place your {symbol}. Choose a row: ")) - 1
            if row_choice < 0 or row_choice > 3:
                print(f"Invalid choice {name}, try again.")
            else:
                valid_row = True
        
        
        valid_column = False
        while not valid_column:
            column_choice = int(input(f"{name}, choose a column to place your {symbol}: ")) - 1
            if column_choice < 0 or column_choice > 2: 
                print(f"Invalid choice {name}, try again.")
            else:
                valid_column = True
        
        if board[row_choice][column_choice] == " ":
            board[row_choice][column_choice] = symbol
            valid_spot = True
        else:
            print(f"That spot is already occupied {name}, try again.")

def win_condition():
#row win
    for row in range(len(board)):
        if board[row][0] != " ":
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                return True
#column win
    for column in range(len(board)):
        column_values = []
        for row in range(len(board)):
            column_values.append(board[row][column])
        if column_values[0] != " ":
            if column_values[0] == column_values[1] and column_values[1] == column_values[2]:
                return True

    #diagonal win
    #left to right
    if board[0][0] != " ":
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True
    #right to left
    if board[0][2] != " ":
        if board[0][0] == board[1][1] and board[1][1] == board[2][0]:
            return True


#player info
p1_name = input ("Enter player 1's name: ")
p2_name = input ("Enter player 2's name: ")

current_player = p1_name
current_symbol = 'X'

print_board()

turns = 0
#game loop
while turns < 9:
    player_turn(current_player, current_symbol)

    print_board()

    if win_condition():
        print(f"{current_player} wins the game!")
        break

    if current_player == p1_name:
        current_player = p2_name
        current_symbol = "O"
    else: 
        current_player = p1_name
        current_symbol = 'X'

    turns += 1
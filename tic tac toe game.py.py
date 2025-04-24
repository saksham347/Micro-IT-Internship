def initialize_board():
    return [' ' for _ in range(9)]  
def display_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")
def check_win(board, player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    for (x, y, z) in win_positions:
        if board[x] == board[y] == board[z] == player:
            return True
    return False
def check_tie(board):
    return ' ' not in board
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("This spot is already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")
def play_game():
    board = initialize_board()
    current_player = 'X'  
    while True:
        display_board(board)
        player_move(board, current_player)
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
if __name__ == "__main__":
    play_game()

# Tic-Tac-Toe by Pierre Aguirre

def main():
    player = next_player("")
    board = create_board()
    while not (winning(board) or is_a_draw(board)):
        display(board)
        turns(player, board)
        player = next_player(player)
    display(board)
    winner = next_player(player)
    print(f"Good game. Player {winner} won. Thanks for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display(board):
    print(f"\n{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}\n")
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def winning(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def turns(player, board):
    square = int(input(f"Player {player}: Choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"

if __name__ == "__main__":
    main()
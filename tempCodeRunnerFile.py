
        
def play_game(board):
    # calls the initialise_board function
    board = initialise_board(board)
    # calls the draw_board function
    draw_board(board)

    # Defining the player and computer marks
    player_mark = 'X'
    computer_mark = 'O'

    # Define the current player (player who goes first)
    current_player = 'player'

    #  The game loop starts
    while True:
        # Get the current player's move
        if current_player == 'player':
            row, col = get_player_move(board)
            mark = player_mark
        else:
            row, col = choose_computer_move(board)
            mark = computer_mark

        # Update the board with the current player's move
        board[row][col] = mark

        # Draw the updated board
        draw_board(board)

        # Check for a win
        if check_for_win(board, mark):
            if current_player == 'player':
                # When the Player wins
                return 1
            else:
                # when the computer Computer wins
                return -1

        # conditional statement to check draw
        if check_for_draw(board):
            # Draw
            return 0

        # Switch to the other player
        if current_player == 'player':
            current_player = 'computer'
        else:
            current_player = 'player'

               
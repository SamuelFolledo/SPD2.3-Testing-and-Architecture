# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

# TODOs:  
# 1. Find all TODO items and see whether you can improve the code. 
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

BOARD_LENGTH = 10

def draw_board(board):
    """ 
        This function prints out the board that it was passed.
        "board" is a list of 10 strings representing the board (ignore index 0)
    """
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_player_letter():
    """
        Lets the player type which letter they want to be.
        Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:                       
        return ['O', 'X']

def who_goes_first():
    """ Randomly choose the player who goes first. """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def play_again():
    """ This function returns True if the player wants to play again, otherwise it returns False. """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    """
        Given a board and a player’s letter, this function returns True if that player has won.
        We use bo instead of board and le instead of letter so we don’t have to type as much.
    """
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle    # TODO: Fix the indentation of this lines and the following ones.
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def get_board_copy(board):
    """ Make a duplicate of the board list and return it the duplicate. """
    dupe_board = []
    for item in board: # TODO: Clean this mess!
        dupe_board.append(item)
    return dupe_board

def is_space_free(board, move):
    """ Return true if the passed move is free on the passed board. """
    return board[move] == ' '

def get_player_move(board):
    """ Let the player type in their move. """
    player_move = ' ' # TODO: W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    while player_move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(player_move)):
        print('What is your next move? (1-9)')
        player_move = input()
    return int(player_move)

def choose_random_move_from_list(board, movesList):
    """
        Returns a valid move from the passed list on the passed board.
        Returns None if there is no valid move.
    """
    possible_moves = []
    for i in movesList:
        if is_space_free(board, i):
            possible_moves.append(i)
    if possible_moves: # TODO: How would you write this pythonically? (You can google for it!)
        # Note: Conditional above works because empty sequences are false
        return random.choice(possible_moves)
    # TODO: is this 'else' necessary?
    return None

def get_computer_move(board, opponent_letter): # TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    """ Given a board and the computer's letter, determine where to move and return that move. """
    if opponent_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, BOARD_LENGTH):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, opponent_letter, i)
            if is_winner(copy, opponent_letter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, BOARD_LENGTH):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None: # TODO: Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    """ Return True if every space on the board has been taken. Otherwise return False. """
    for i in range(1, BOARD_LENGTH):
        if is_space_free(board, i):
            return False
    return True

def did_win(move, board, letter):
    """
        Applies the move on board and returns 
        - True if the move resulted to a win
        - False if move resulted to a tie
        - None if game did not end
    """
    make_move(board, letter, move)
    if is_winner(board, letter):
        draw_board(board)
        return True
    if is_board_full(board):
        draw_board(board)
        print('The game is a tie!')
        return False
    return None

def play_new_game():
    """ Starts a new game. """
    the_board = [' '] * BOARD_LENGTH # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
    player_letter, opponent_letter = input_player_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')
    while not is_board_full(the_board):
        if turn == 'player':
            # Player’s turn.
            draw_board(the_board)
            move = get_player_move(the_board)
            did_player_win = did_win(move, the_board, player_letter)
            if did_player_win is None:
                turn = 'computer'
                continue
            if did_player_win:
                print('Hooray! You have won the game!')
            break

        else:
            # Computer’s turn.
            move = get_computer_move(the_board, opponent_letter)
            did_computer_win = did_win(move, the_board, opponent_letter)
            if did_computer_win is None:
                turn = 'player'
                continue
            if did_computer_win:
                print('The computer has beaten you! You lose.')
            break

print('Welcome to Tic Tac Toe!')

# TODO: The following mega code block is a huge hairy monster. Break it down 
# into smaller methods. Use TODO s and the comment above each section as a guide 
# for refactoring.

while True:
    play_new_game()
    if not play_again():
        break
"""
Problem
Imagine working on software that determines the winner of a game of Tic Tac Toe. Create a function named tic_tac_toe_winner that is responsible for determing the state of a Tic Tac Toe board - Either there's no winner, it's a tie, 'X' won, or 'O' won. This function should take in 3x3 matrix as a parameter. Each element is either an 'X', 'O', or empty string ''. This function should have a return value of the winner 'X' or 'O', 'Tie' (for a full board with no winner), or None (for a game that is still in progress).

Example 1: Input:

[
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'X', 'O']
]
Output: 'Tie'

Example 2: Input:

[
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'O', '']
]
Output: 'O'

Example 3: Input:

[
    ['X', 'O', 'O'],
    ['O', 'X', 'O'],
    ['', '', 'X']
]
Output: 'X'

Example 4: Input:

[
    ['X', '', 'O'],
    ['O', 'X', 'X'],
    ['', '', '']
]
Output: None
"""

def tic_tac_toe_winner(board):
    '''
    INPUT: Tic Tac Toe board (3x3 matrix)
    OUTPUT: Winner
    '''
    if not isinstance(board, list):
        return None
    
    if len(board) != 3 or board == [['','',''], ['','',''], ['','','']]:
        return None
    
    winning_combinations = [ 
        [(0, 0), (0, 1), (0, 2)], 
        [(1, 0), (1, 1), (1, 2)], 
        [(2, 0), (2, 1), (2, 2)], 
        [(0, 0), (1, 0), (2, 0)], 
        [(0, 1), (1, 1), (2, 1)], 
        [(0, 2), (1, 2), (2, 2)], 
        [(0, 0), (1, 1), (2, 2)], 
        [(0, 2), (1, 1), (2, 0)] 
        ]
    
    for combo in winning_combinations:
        letter = ''
        for index in combo:
            if board[index[0]][index[1]] == '':
                letter = ''
                break
            elif letter and letter != board[index[0]][index[1]]:
                letter = ''
                break
            elif letter and index == combo[-1]:
                return letter
            else:
                letter = board[index[0]][index[1]]
            
    for row in board:
        if '' in row:
            return None
        
    return 'Tie'
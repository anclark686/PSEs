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
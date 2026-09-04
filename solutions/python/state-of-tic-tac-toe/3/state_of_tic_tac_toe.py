"""Determine the state of a tic-tac-toe game board."""


def gamestate(board):
    """Return whether the tic-tac-toe game is won, drawn, ongoing, or invalid."""
    win_lines = []
    
    for line in board:
        win_lines.append(line)
        
    for column in range(3):
        full_column = board[0][column] + board[1][column] + board[2][column]
        win_lines.append(full_column)
    
    first_diagonal = board[0][0] + board[1][1] + board[2][2]
    second_diagonal = board[0][2] + board[1][1] + board[2][0]
    
    win_lines.append(first_diagonal)
    win_lines.append(second_diagonal)
    
    X_win = "XXX" in win_lines
    O_win = "OOO" in win_lines
    
    X_count = 0
    O_count = 0
    
    for line in board:
        for value in line:
            if value == "X":
                X_count += 1
            elif value == "O":
                O_count += 1
                
    if X_count - O_count > 1:
        raise ValueError("Wrong turn order: X went twice")
    if O_count > X_count:
        raise ValueError("Wrong turn order: O started")
    
    if X_win and O_win:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )
    if X_win and X_count != O_count + 1:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )
    if O_win and X_count != O_count:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )
        
    if X_win or O_win:
        return "win"
    if X_count + O_count == 9:
        return "draw"
    else: 
        return "ongoing"

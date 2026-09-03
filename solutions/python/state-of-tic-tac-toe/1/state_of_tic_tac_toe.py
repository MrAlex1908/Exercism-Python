"""Determine the state of a tic-tac-toe game board."""


def gamestate(board):
    """Return whether the tic-tac-toe game is won, drawn, ongoing, or invalid."""
    X = "X"
    O = "O"
    X_count = 0
    O_count = 0
    X_win = False
    O_win = False

    for line in board:
        for value in line:
            if value == X:
                X_count += 1
            elif value == O:
                O_count += 1

        if line == "XXX":
            X_win = True
        elif line == "OOO":
            O_win = True

    for column in range(3):
        if (
            board[0][column] == X
            and board[1][column] == X
            and board[2][column] == X
        ):
            X_win = True
        elif (
            board[0][column] == O
            and board[1][column] == O
            and board[2][column] == O
        ):
            O_win = True

    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        X_win = True
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        O_win = True

    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        X_win = True
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        O_win = True

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
    elif X_count + O_count == 9:
        return "draw"
    else:
        return "ongoing"

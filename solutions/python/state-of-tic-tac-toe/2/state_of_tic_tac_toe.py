"""Determine the state of a tic-tac-toe game board."""


def gamestate(board):
    """Return whether the tic-tac-toe game is won, drawn, ongoing, or invalid."""
    X = "X"
    O = "O"

    X_count = 0
    O_count = 0

    # 1. Count how many moves each player made.
    for line in board:
        for value in line:
            if value == X:
                X_count += 1
            elif value == O:
                O_count += 1

    # 2. Validate turn order.
    if X_count - O_count > 1:
        raise ValueError("Wrong turn order: X went twice")

    if O_count > X_count:
        raise ValueError("Wrong turn order: O started")

    # 3. Collect all possible winning lines.
    winning_lines = []

    # Add all rows.
    for row in board:
        winning_lines.append(row)

    # Add all columns.
    for column in range(3):
        column_line = (
            board[0][column]
            + board[1][column]
            + board[2][column]
        )
        winning_lines.append(column_line)

    # Add both diagonals.
    first_diagonal = board[0][0] + board[1][1] + board[2][2]
    second_diagonal = board[0][2] + board[1][1] + board[2][0]

    winning_lines.append(first_diagonal)
    winning_lines.append(second_diagonal)

    # 4. Check whether X or O has a winning line.
    X_win = "XXX" in winning_lines
    O_win = "OOO" in winning_lines

    # 5. Validate impossible game states.
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

    # 6. Determine the final game state.
    if X_win or O_win:
        return "win"

    if X_count + O_count == 9:
        return "draw"

    return "ongoing"
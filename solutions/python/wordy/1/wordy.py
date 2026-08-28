"""
# Parse and evaluate simple mathematical word problems.
# Supports addition, subtraction, multiplication, and division.
# Multiple operations are evaluated strictly from left to right.
# Raises ValueError for invalid syntax or unknown operations.
"""
def answer(question):
    """
    Parse and evaluate a simple mathematical word problem.

    The question must begin with "What is" and may contain addition,
    subtraction, multiplication, and division operations. Multiple
    operations are evaluated strictly from left to right, ignoring
    the standard mathematical order of operations.

    Args:
        question (str): A mathematical question written in words.

    Returns:
        int: The evaluated result of the expression.

    Raises:
        ValueError: If the question has invalid syntax.
        ValueError: If the question contains an unknown operation.
    """
    clean_question = question.replace("What is", "").replace("?", "").strip()
    tokens = clean_question.split()

    if not tokens:
        raise ValueError("syntax error")

    try:
        result = int(tokens[0])
    except (ValueError, IndexError):
        raise ValueError("syntax error")

    index = 1

    while index < len(tokens):
        if tokens[index] == "plus" or tokens[index] == "+":
            next_index = index + 1
            try:
                result += int(tokens[next_index])
                index += 2
            except (ValueError, IndexError):
                raise ValueError("syntax error")

        elif tokens[index] == "minus" or tokens[index] == "-":
            next_index = index + 1
            try:
                result -= int(tokens[next_index])
                index += 2
            except (ValueError, IndexError):
                raise ValueError("syntax error")

        elif tokens[index] == "divided" or tokens[index] == "/":
            try:
                if tokens[index] == "divided":
                    if tokens[index + 1] != "by":
                        raise ValueError("syntax error")

                    next_index = index + 2
                    index_step = 3
                else:
                    next_index = index + 1
                    index_step = 2

                result /= int(tokens[next_index])
                index += index_step

            except (ValueError, IndexError):
                raise ValueError("syntax error")

        elif tokens[index] == "multiplied" or tokens[index] == "*":
            try:
                if tokens[index] == "multiplied":
                    if tokens[index + 1] != "by":
                        raise ValueError("syntax error")

                    next_index = index + 2
                    index_step = 3
                else:
                    next_index = index + 1
                    index_step = 2

                result *= int(tokens[next_index])
                index += index_step

            except (ValueError, IndexError):
                raise ValueError("syntax error")

        else:
            try:
                int(tokens[index])
            except ValueError:
                raise ValueError("unknown operation")
            else:
                raise ValueError("syntax error")

    return int(result)
"""Convert OCR-formatted digit grids into strings of decimal numbers."""


def convert(input_grid):
    """Return the decimal numbers represented by a grid of OCR characters."""
    # Value errors logic != % 4; != % 3
    if (len(input_grid) % 4) != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    for line in input_grid:
        if (len(line) % 3) != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    # Split the OCR grid into 3x4 digit blocks.
    all_blocks = []

    for start_row in range(0, len(input_grid), 4):
        row_blocks = []
        current_4_lines = input_grid[start_row:start_row + 4]

        for start in range(0, len(current_4_lines[0]), 3):
            block = []

            for line in current_4_lines:
                current_line = line[start:start + 3]
                block.append(current_line)

            row_blocks.append(block)

        all_blocks.append(row_blocks)

    template_0 = (
        " _ ",
        "| |",
        "|_|",
        "   "
    )

    template_1 = (
        "   ",
        "  |",
        "  |",
        "   "
    )

    template_2 = (
        " _ ",
        " _|",
        "|_ ",
        "   "
    )

    template_3 = (
        " _ ",
        " _|",
        " _|",
        "   "
    )

    template_4 = (
        "   ",
        "|_|",
        "  |",
        "   "
    )

    template_5 = (
        " _ ",
        "|_ ",
        " _|",
        "   "
    )

    template_6 = (
        " _ ",
        "|_ ",
        "|_|",
        "   "
    )

    template_7 = (
        " _ ",
        "  |",
        "  |",
        "   "
    )

    template_8 = (
        " _ ",
        "|_|",
        "|_|",
        "   "
    )

    template_9 = (
        " _ ",
        "|_|",
        " _|",
        "   "
    )

    digital_patterns = {
        template_0: "0",
        template_1: "1",
        template_2: "2",
        template_3: "3",
        template_4: "4",
        template_5: "5",
        template_6: "6",
        template_7: "7",
        template_8: "8",
        template_9: "9"
    }

    result = []

    for row_blocks in all_blocks:
        row_result = []

        for block in row_blocks:
            if tuple(block) in digital_patterns:
                row_result.append(digital_patterns[tuple(block)])
            else:
                row_result.append("?")

        result.append("".join(row_result))

    return ",".join(result)
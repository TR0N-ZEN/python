import math
import pprint

# array for each of the 81 boxes
# containing possible values
fields = [
    [
        [1], [], [], [], [4], [], [5], [], []
    ],
    [
        [], [6], [], [], [], [], [2], [], []
    ],
    [
        [9], [], [], [3], [], [], [], [4], [6]
    ],

    [
        [], [7], [], [], [1], [], [], [9], [4]
    ],
    [
        [], [], [1], [2], [], [], [], [], []
    ],
    [
        [], [], [], [], [], [], [], [5], []
    ],

    [
        [], [9], [], [], [2], [], [], [1], [7]
    ],
    [
        [3], [], [], [], [], [8], [], [], []
    ],
    [
        [], [], [], [], [], [], [6], [], []
    ]
]

# fields = [
#     [
#         [], [], [], [], [], [], [], [], []
#     ],
#     [
#         [], [], [], [], [], [], [], [], []
#     ],
#     [
#         [], [], [], [], [], [], [], [], []
#     ],
#
#     [
#         [], [], [], [], [], [], [], [], []
#     ],
#     [
#         [], [], [], [], [], [], [], [], []
#     ],
#     [
#         [], [], [], [], [], [], [], [], []
#     ],
#
#     [
#         [], [], [], [], [], [], [], [], []
#     ],
#     [
#         [], [], [], [], [], [], [], [], []
#     ],
#     [
#         [], [], [], [], [], [], [], [], []
#     ]
# ]
# enter given values for boxes manually


# give empty boxes all possibilities
for row in range(9):
    for column in range(9):
        if fields[row][column] == []:
            fields[row][column] = list(range(1, 10))


n_times_nothing_removed = 0
n_times_things_removed = 0

"""
should at max be necessary 81 times
because after each iteration at least one field
should be narrowed down to holding one possible value
"""
for count in range(81):
    """
    narrow down possibilities
    find arrays of length one and use their value to
    remove it from all other possibilites inside the boxes which are
    either in the same row or in the same column
    """
    for row_number in range(9):
        for column_number in range(9):

            # if there is only one possibility then this is the number and
            # it should be removed from the same row, column and 3x3 box
            if len(fields[row_number][column_number]) == 1:
                value_to_remove = fields[row_number][column_number][0]
                print(f"value to remove: {value_to_remove} from column {column_number} and row {row_number}")

                # remove from all possibilities inside boxes in the same column
                for index, row in enumerate(fields):
                    try:
                        # TESTME do not remove the item itself.
                        if index == row_number:
                            print(f"skipped row {index} since {row_number}")
                            continue

                        row[column_number].remove(value_to_remove)
                        print(f"removed {value_to_remove} from row {index}")
                        n_times_things_removed += 1
                    except ValueError:
                        # print(f"Nothing to remove in row {column_number}")
                        n_times_nothing_removed += 1

                # remove from all possibilities inside boxes in the same row
                for index, possibilities in enumerate(fields[row_number]):
                    try:
                        # TESTME do not remove the item itself
                        if index == column_number:
                            print(f"skipped row {index} since {column_number}")
                            continue

                        possibilities.remove(value_to_remove)
                        print(f"removed {value_to_remove} from column {index}")
                        n_times_things_removed += 1
                    except ValueError:
                        # print(f"Nothing to remove in row {row_number}")
                        n_times_nothing_removed += 1

                """
                use the 3 by 3 squares to remove possibilities
                use integer division without remainder
                """
                three_by_three_row = math.floor(row_number/3)
                three_by_three_column = math.floor(column_number/3)
                for row_number_delete in range(three_by_three_row,
                                               three_by_three_row+3):
                    for column_number_delete in range(three_by_three_column,
                                                      three_by_three_column+3):
                        try:
                            if row_number_delete == row_number and \
                                    column_number_delete == column_number:
                                print(f"skipped row {index} since column {column_number} and row {row_number}")
                                continue

                            fields[row_number_delete][column_number_delete]\
                                .remove(value_to_remove)
                            n_times_things_removed += 1
                        except ValueError:
                            print(f"Nothing to remove in box starting in row {three_by_three_row} and colum {three_by_three_column}")
                            n_times_nothing_removed += 1

for row in range(9):
    for column in range(9):
        if len(fields[row][column]) > 1:
            fields[row][column] = [0]

print(f"Nothing removed {n_times_nothing_removed} times.")
print(f"Things removed {n_times_things_removed} times.")
pprint.pprint(fields)

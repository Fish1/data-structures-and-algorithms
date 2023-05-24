import numbers
import sys

sys.setrecursionlimit(1000)

def print_numbers(array):
    for x in array:
        if isinstance(x, numbers.Number):
            print(x)
        else:
            print_numbers(x)


mydata = [
    1, 2, 3,
    [4, 5, 6],
    7,
    [8, [9, 10, 11, [12, 13, 14]]],
    [15, 16, 17, 18, 19,
        [20, 21, 22,
            [23, 24, 25,
                [26,27,28], 29, 30
            ],
         31], 32
    ]
]

print_numbers(mydata)

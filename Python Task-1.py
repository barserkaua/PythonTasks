""" Write a program that takes 4 inputs, where each input consists of 2 numbers in the format x,y.
 You are required to print a two-dimensional array having x rows and y columns for each input.
 The elements of the arrays should be whole numbers starting from 1 and incrementing by 1.
"""


def array(x: int, y: int):  # x - column, y - numbers
    result = []
    sort_by_number = []
    for i in range(x * y):
        sort_by_number.append(int(i + 1))
        if len(sort_by_number) >= y:
            copy_list = sort_by_number.copy()
            result.append(copy_list)
            sort_by_number.clear()
    return result


print(array(3, 4))

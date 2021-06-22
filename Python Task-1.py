""" Write a program that takes 4 inputs, where each input consists of 2 numbers in the format x,y.
 You are required to print a two-dimensional array having x rows and y columns for each input.
 The elements of the arrays should be whole numbers starting from 1 and incrementing by 1.
"""


def array(x: int, y: int):  # x - column, y - numbers
    result = []
    app_list = []
    for i in range(x * y):
        app_list.append(int(i + 1))
        if len(app_list) >= y:
            a = app_list.copy()
            result.append(a)
            app_list.clear()
    return result


print(array(3, 4))

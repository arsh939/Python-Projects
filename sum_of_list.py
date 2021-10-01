"""
Write a Python program of recursion list sum.
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
"""


def sum_list(array: list) -> int:
    sum_array = 0
    for elm in array:
        if isinstance(elm, int):
            sum_array += elm
        else:
            sum_array += sum_list(elm)
    return sum_array


print(sum_list([1, 2, [3, 4], [5, 6]]))  # 21

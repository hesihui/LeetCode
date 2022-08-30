
def searchMatrix(matrix, target):
    # conner case
    if len(matrix) == 0 or len(matrix[0] == 0):
        return False
    left = 0
    row = len(matrix)
    col = len(matrix[0])
    right = row * col - 1
    while left <= right:
        # col_index = mid % col
        # row_index = mid / col
        mid =  (left + right) // 2
        print(mid)
        mid_col = mid % col
        mid_row = mid // col
        if matrix[mid_row][mid_col] == target:
            return True
        else:
            if matrix[mid_row][mid_col] < target:
                left = mid + 1
            elif matrix[mid_row][mid_col] > target:
            # mid > target
                right = mid - 1
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    searchMatrix(matrix, target)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

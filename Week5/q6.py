import numpy as np

array = np.array([[12, 5, 7],
                  [3, 8, 1],
                  [6, 2, 9]])

# Sort array by the second row
second_row_sort = array[:, array[1, :].argsort()]

# Sort array by the second column
second_column_sort = array[array[:, 1].argsort()]

print("\nArray sorted by the second row:")
print(second_row_sort)

print("\nArray sorted by the second column:")
print(second_column_sort)

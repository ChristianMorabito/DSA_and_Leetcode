# refer to Rotate_Image.gif to see algorithm

def rotate_image(array):
    row = len(array)

    for i in range(1, row):
        for j in range(i):
            array[i][j], array[j][i] = array[j][i], array[i][j]

    for k in range(row):
        array[k].reverse()


matrix = [[5,  1,  9,  11],
          [2,  4,  8,  10],
          [13, 3,  6,  7],
          [15, 14, 12, 16]]

rotate_image(matrix)
for sub_array in matrix:
    print(sub_array)


# Add matrices together
def add(*args):
    num_mat = len(args)
    if num_mat < 2:
        raise ValueError("Need at least two matrices to add.")
    width = len(args[0][0])
    height = len(args[0])
    final_matrix = [ [0 for x in range(width)] for y in range(height) ]
    for matrix in args:
        w = len(matrix[0])
        h = len(matrix)
        if h != height:
            raise ValueError("Given matrices are not the same size.")
        for row in range(h):
            if len(matrix[row]) != w:
                raise ValueError("Given matrices are not the same size.")
        for i in range(h):
            for j in range(w):
                final_matrix[i][j] += matrix[i][j]
    return final_matrix


if __name__ == '__main__':
    matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
    final = add(matrix1, matrix2)
    print(final)
    print(add([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]]))
    # Test ValueError:
    # print(add([[1, 9], [7, 3]], [[1, 2], [3]]))
    # Test only sending one matrix to add function
    # print(add([[1, 9]]))


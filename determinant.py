import doctest  

def smaller_matrix(A, col):
    '''
    (dict, num) -> dict
    input: dict of matrix A, and the number of the column to be removed
    output: the dict of new matrix with the last row and colth column removed
    
    >>> A = [[1,0,-1],[1,4,1],[5,2,5]]
    >>> smaller_matrix(A, 0)
    [[0, -1], [4, 1]]
    >>> smaller_matrix(A, 1)
    [[1, -1], [1, 1]]
    >>> B = [[1,-2,0,-1],[0,7,1,0],[1,2,4,1],[5,10,2,5]]
    >>> smaller_matrix(B, 2)
    [[1, -2, -1], [0, 7, 0], [1, 2, 1]]
    '''
    new_matrix = []
    for row in range(len(A)-1):
        new_matrix.append([])
        col_met = False
        for i in range(len(A)-1):
            col_index = i
            if col_index == col or col_met:
                col_index += 1
                col_met = True
            new_matrix[row].append(A[row][col_index])
            
    return new_matrix
    

def det_calc(A):
    '''
    (dict) -> num
    input: dict of dict of row vectors of matrix
    output: the determinant of matrix

    >>> A = [[1,0,3],[0,-1,4],[2,1,-2]]
    >>> det_calc(A)
    4
    >>> B = [[2,7,10,0,3],[0,-7,-10,-9,7],[0,0,-8,3,-10],[0,0,0,-3,-5],\
    [0,0,0,0,5]]
    >>> det_calc(B)
    -1680
    '''
    if len(A) == 2:
        det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    else:
        det = 0
        for col, row in enumerate(A):
            smaller = smaller_matrix(A, col)
            # recursion
            det += (-1)**(len(A)+col+1)*A[-1][col]*det_calc(smaller)
            
    return det



if __name__ == '__main__':
    doctest.testmod()

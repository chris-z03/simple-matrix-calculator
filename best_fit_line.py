import doctest
from rref import *

def matrix_mult(A, B):
    '''
    (list, list) -> list
    return the product of AB

    >>> A = [[2,2],[-3,-2]]
    >>> B = [[3,-2,-1],[2,2,3]]
    >>> matrix_mult(A, B)
    [[10, 0, 4], [-13, 2, -3]]
    >>> A = [[1, 2, 3, 4], [1, 1, 1, 1]]
    >>> B = [[0], [2], [4], [4]]
    >>> matrix_mult(A, B)
    [[32], [10]]
    '''
    if len(A[0]) != len(B):
        return 'DNE'
    product = []
    
    for row in range(len(A)):
        product.append([])
        for col in range(len(B[0])):
            dot_product = 0
            for i in range(len(A[0])):
                dot_product += A[row][i] * B[i][col]
            product[row].append(dot_product)

    return product

def transpose(A):
    '''
    (list) -> list
    return the transpose of A
    >>> A = [[3,-2,-1],[2,2,3]]
    >>> transpose(A)
    [[3, 2], [-2, 2], [-1, 3]]
    '''
    transpose = []
    for row in range(len(A[0])):
        transpose.append([])
        for col in range(len(A)):
            transpose[row].append(A[col][row])
        
    return transpose

def matrix_from_points(points, degree):
    '''
    (list, int) -> list
    input a list of coordinates of points and the degree of polynomial
    output the matrix generated

    >>> points = [[1,0],[2,2],[3,4],[4,4]]
    >>> matrix_from_points(points, 2)
    [[1, 1, 1, 0], [4, 2, 1, 2], [9, 3, 1, 4], [16, 4, 1, 4]]
    '''
    A = []
    for i in range(len(points)):
        A.append([])
        for exp in range(degree, -1, -1):
            A[i].append(points[i][0]**exp)
        A[i].append(points[i][1])
    return A


def curve_fitting(points, degree):
    '''
    (list, int) -> list
    input a list of coordinates of points and the degree of polynomial
    if only 1 solution exists, return the list of coefficients
    if infinite solutions exist, return the solution matrix
    >>> points = [[1,0],[2,2],[3,4],[4,4]]
    >>> curve_fitting(points, 1)
    [1.4, -1]
    '''
    augmented_A = matrix_from_points(points, degree)
    A = []
    B = []
    for row in augmented_A:
        A.append(row[:len(row)-1])
        B.append([row[-1]])

    right_side = matrix_mult(transpose(A), B)
    left_side = matrix_mult(transpose(A), A)

    solution = solve_matrix(left_side, right_side)
    
    if len(solution)<len(solution[0])-1 or \
       solution[len(solution[0])-2][len(solution[0])-2] != 1:
        return solution

    coefficients = []
    for row in solution:
        coefficients.append(row[-1])
    return coefficients

if __name__ == '__main__':
    doctest.testmod()

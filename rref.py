import doctest
from determinant import *
import copy

def get_leading_places(A):
    '''
    >>> get_leading_places([[0,0,0],[0,0,0],[0,0,0]])
    [3, 3, 3]
    >>> get_leading_places([[1,2,3,],[0,0,3],[0,3,1]])
    [0, 2, 1]
    '''
    leading_places = []
    for vec in A:
        no_leading = True
        for place, element in enumerate(vec):
            if element != 0:
                leading_places.append(place)
                no_leading = False
                break
        if no_leading:
                leading_places.append(len(A))
    return leading_places

def rearrange(A):
    '''
    (list) -> list
    input: list of row vectors of A.
    output: a rearranged matrix of A.

    >>> A = [[0,0,0,0],[1,0,2,-10],[0,1,-2,3]]
    >>> B = [[0,0,0],[0,0,0],[0,0,0]]
    >>> C = [[1,2,3,],[0,0,3],[0,3,1]]
    >>> rearrange(A)
    [[1, 0, 2, -10], [0, 1, -2, 3], [0, 0, 0, 0]]
    >>> rearrange(B)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> rearrange(C)
    [[1, 2, 3], [0, 3, 1], [0, 0, 3]]
    '''
    rearranged = []
    while len(A) != 0:
        leading_places = get_leading_places(A)

        for row, vec in enumerate(A):
            no_leading = True
            for place, element in enumerate(vec):
                if element != 0:
                    leading = place
                    no_leading = False
                    break
            if no_leading:
                leading = len(A)
            if leading == min(leading_places):
                rearranged.append(A.pop(row))
    return rearranged
                
    

def rref(A):
    '''
    (list) -> list
    input: list of lists of row vectors of A
    output: rref(A) with number of leading 1's no more than n

    >>> A = [[1,2,-2],[3, 8, -10],[3,9,-2]]
    >>> rref(A)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> B = [[3,6],[5,6],[0,0]]
    >>> rref(B)
    [[1, 0], [0, 1], [0, 0]]
    >>> C = [[1,2,3,4],[3,4,2,1],[5,2,1,4]]
    >>> rref(C)
    [[1, 0, 0, 1], [0, 1, 0, -1.5], [0, 0, 1, 2]]
    >>> D = [[0,0,2,1],[3,2,0,3],[0,3,5,2]]
    >>> rref(D)
    [[1, 0, 0, 10/9], [0, 1, 0, -1/6], [0, 0, 1, 1/2]]
    '''
    # 1. make the leading number to be 1
    # 2. clear all the non-zero numbers above and below leading 1's

    A = copy.deepcopy(rearrange(A))
    for row in range(len(A)):
        # get new leading number places
        leading_places = get_leading_places(A)
        
        # check if the row is all zero
        if leading_places[row] < len(A[row]):
            # divide the row by its leading number
            factor = A[row][leading_places[row]]
            for col in range(len(A[row])):
                A[row][col]/= factor
                
            # and make sure all numbers above and below it are zero's
            for otherrow in range(len(A)):
                # if the number at that row is not zero
                if otherrow != row and A[otherrow][leading_places[row]] != 0:
                    # the number at that row's leading number's place
                    factor = A[otherrow][leading_places[row]]
                    for col in range(len(A[otherrow])):
                        A[otherrow][col] -= factor * A[row][col]

    return A

def inverse(A):
    '''
    (list) -> list
    return the inverse of A
    
    >>> inverse([[4,0],[0,7]])
    [[1/4, 0], [0, 1/7]]
    >>> A = [[1,7,0],[1,7,4],[1,-6,8]]
    >>> inverse(A)
    [[1.538, -1.078, 0.538], [-0.077,0.154,-0.077],[-0.25,0.25,0]]
    '''
    if len(A) != len(A[0]):
        return 'DNE'
    if det_calc(A) == 0:
        return 'DNE'
    I = []
    for row in range(len(A)):
        I.append([])
        for col in range(len(A)):
            if col == row:
                I[row].append(1)
            else:
                I[row].append(0)
    for row in range(len(A)):
        A[row].extend(I[row])
    A = rref(A)

    A_inv = []
    for row in range(len(A)):
        A_inv.append(A[row][len(A):])
        
    return A_inv

def solve_matrix(A, B):
    
    for row in range(len(A)):
        A[row].extend(B[row])
    A = rref(A)
    return A

if __name__ == '__main__':
    doctest.testmod()

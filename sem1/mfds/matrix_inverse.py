import enum
from operator import ge
from gauss_jacobi_method import generate_iteration_matrix
from imp import get_magic
from utils import str_matrix
import math

def get_minor(A, i, j):
    # create an empty matrix with dimension (m-1) * (n-1)
    M = [[0 for idx in range(len(A)-1)] for idx in range(len(A)-1)]
    c_row = 0
    for row_idx, row in enumerate(A):
        c_column = 0
        if row_idx == i:
            continue
        for col_idx, col in enumerate(row):
            if col_idx ==j:
                continue
            M[c_row][c_column] = col
            c_column = c_column + 1
        c_row = c_row + 1            


    return M

def get_determinant(A):
    if len(A) == 1 and len(A[0]) == 1:
        return A[0][0]
    if len(A) == 2 and len(A[0]) == 2:
        return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
    C = get_cofactor_matrix(A)        
    det = 0
    for idx, a in enumerate(A[0]):          
        det = det + a * C[0][idx]
    return det        

def get_cofactor_matrix(A):
    # create an empty matrix with dimension (m-1) * (n-1)
    C = [[0 for idx in range(len(A))] for idx in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):        
            k = i + j
            M = get_minor(A, i, j)
            det = get_determinant(M)
            c = math.pow(-1, k) * det
            C[i][j] = c
    return C            

def get_transpose(A):
    T = [[0 for idx in range(len(A))] for idx in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):        
            T[j][i] = A[i][j]            

    return T

def get_matrix_inverse(A):
    det = get_determinant(A)
    C = get_cofactor_matrix(A)
    Adj = get_transpose(C)
    AInv = [[0 for idx in range(len(A))] for idx in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):        
            AInv[i][j] = Adj[i][j]/det

    return AInv

if __name__ == "__main__":

    A1 = [
        [5, -1, 3],
        [2, -8, 1],
        [-2, 0, 4]
    ]

    A2 = [
        [1, 2, 3],
        [0, 6, 5],
        [0, 0, 2]
    ]

    A3 = [
        [-1, 1, 2],
        [3, -1, 1],
        [-1, 3, 4]
    ]

    A4 = [
        [4, 7],
        [2, 6],
    ]

    A5 = [
        [3, 0, 2],
        [2, 0, -2],
        [0, 1, 1]
    ]    


    A = A5

    C = get_cofactor_matrix(A)
    print("cofactor:\n", str_matrix(C))

    det = get_determinant(A)
    print("det:", det)

    inverse = get_matrix_inverse(A)
    print("Inverse:\n", str_matrix(inverse))

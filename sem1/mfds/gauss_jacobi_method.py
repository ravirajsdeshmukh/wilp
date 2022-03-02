from copy import deepcopy
from utils import str_matrix, convertToDS, generate_matrix_norms, str_vector
import random
from digonally_dominant import is_diagonally_dominant, make_diagonally_dominant
from tabulate import tabulate

localDS = 5

def generate_iteration_matrix(L, U):
    '''
    Iteration matrix for gauss jacobi is
    H = -(L+U)
    '''
    if len(L) != len(U):
        raise Exception("matrix dimension mismatch")

    H = [[0 for idx in range(len(L))] for idx in range(len(U))]
    for l in range(len(L)):
        for u in range(len(U)):
            sum = (L[l][u] + U[l][u])             
            H[l][u] = (-1) * sum

    return H


def generate_one_iteration(A, X, b):
    '''
    Generates one iteration for guass seidel method
    A is the coefficent matrix
    X is the vector with initial values of the variables
    b is the constant matrix

    '''
    if len(X) != len(A) != len(b):
        raise Exception("matrix dimension mismatch")

    X1 = [0 for idx in range(len(X))]
    for row_idx, row in enumerate(A):
        col_sum = 0            # represents sum of all elements of row excluding diagonal element
        diagonal = 0       # represents diagonal element
        for col_idx, col in enumerate(row):
            if row_idx == col_idx:
                diagonal = col
                continue
            col_sum = col_sum + col * X[col_idx]

        sum = b[row_idx] - col_sum
        val = float(sum)/diagonal
        X1[row_idx] = convertToDS(val)

    return X1

def normalize_matrix(A):
    '''
    Makes all diagonal elements 1 for the matrix
    '''
    for row_idx, row in enumerate(A):
        diag_elm = A[row_idx][row_idx]
        for col_idx, col in enumerate(row):
            new_value = col/diag_elm
            new_value = convertToDS(new_value, localDS)
            row[col_idx] = new_value

    return A


def generate_I_L_U_factorization(A):
    '''
    So, we need to first determine L & U

    1. Make all the diagonal elements of A as 1, that is divide by a(ii)
    2. Generate LU factorization as below
        A = I + L + U
    '''
    # Step-1 Make all the diagonal elements 1
    A = normalize_matrix(A)

    # Step-2 Generate factorization A = I + L + U
    # Populate Unit Matrix
    I = [[0 for idx in range(len(A))] for idx in range(len(A))]
    for row_idx in range(len(A)):
        for col_idx in range(len(A)):
            if row_idx == col_idx:
                I[row_idx][col_idx] = 1

    # Populate lower triangular matrix
    L = [[0 for idx in range(len(A))]for idx in range(len(A))]
    for row_idx in range(len(A)):
        for col_idx in range(len(A)):
            if col_idx < row_idx:
                L[row_idx][col_idx] = A[row_idx][col_idx]

    # Populate upper triangular matrix
    U = [[0 for idx in range(len(A))]for idx in range(len(A))]
    for row_idx in range(len(A)):
        for col_idx in range(len(A)):
            if col_idx > row_idx:
                U[row_idx][col_idx] = A[row_idx][col_idx]

    return A, I, L, U

if __name__ == "__main__":
    '''
    A = [
        [5, -1, 3],
        [2, -8, 1],
        [-2, 0, 4]
    ]

    A1 = [
        [4, 2, -2],
        [0, 4, 2],
        [1, 0, 4]
    ]
    '''
    iterations = 3
    dim = 4
    results = list()
    for idx in range(0, iterations):
        result = list()
        results.append(result)

        A = [[0 for c in range(0, dim) ] for r in range(0, dim)]
        b = [0 for c in range(0, dim)]
        X = [0 for c in range(0, dim)]
        for row_idx in range(0, dim):
            for col_idx in range(0, dim):
                A[row_idx][col_idx] = random.randint(1, 8)

        original_matrix = str_matrix(A)
        result.append(original_matrix)
        constants_vector = str_vector(b)
        result.append(constants_vector)    
        # is_dd = is_diagonally_dominant(A)
        # A2 = None
        # if not is_dd:
        #     print("matrix is not diagonally dominant, attempting to make diagonally dominant")
        #     try:
        #         A2 = make_diagonally_dominant(A)
        #     except Exception as ex:
        #         print("Exception occurred while attempting to make diagonally dominant:", ex)  
        #     if A2:                      
        #         print("diagonally dominant matrix:\n", str_matrix(A2))
        
        # if A2 is not None:
        #     A = A2
        

        AN, I, L, U = generate_I_L_U_factorization(deepcopy(A))

        result.append(str_matrix(L))
        result.append(str_matrix(U))

        H = generate_iteration_matrix(L, U)
        iteration_matrix = str_matrix(H)
        result.append(iteration_matrix)

        l1, l2, l_infinity = generate_matrix_norms(H)
        result.append("l1-norm:{}\nl2-norm:{}\nl-infinity:{}".format(l1, l2, l_infinity))

        X1 = generate_one_iteration(A, deepcopy(X), b)
        sol = str_vector(X1)

        result.append(sol)

    print(tabulate(results, headers=("Original", "b", "L", "U", "Iteration Matrix", "Norms", "Iteration-1"), tablefmt="grid"))
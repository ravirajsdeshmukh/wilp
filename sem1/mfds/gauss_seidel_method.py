from copy import deepcopy
import enum
import random
from  utils import convertToDS, str_matrix, str_vector, generate_matrix_product
from gauss_jacobi_method import generate_I_L_U_factorization, generate_matrix_norms
from matrix_inverse import get_matrix_inverse
from tabulate import tabulate
from digonally_dominant import make_diagonally_dominant, is_diagonally_dominant

def generate_one_iteration(A, X, b):
    '''
    Generates one iteration for guass seidel method
    A is the coefficent matrix
    X is the vector with initial values of the variables
    b is the constant matrix

    '''
    if len(X) != len(A) != len(b):
        raise Exception("matrix dimension mismatch")

    # X1 = [0 for idx in range(len(X))]
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
        X[row_idx] = convertToDS(val)

    return X

def generate_iteration_matrix(I, L, U):
    '''
    Iteration matrix for gauss jacobi is
    H = -(I+L)^-1 * U
    '''
    if len(L) != len(U):
        raise Exception("matrix dimension mismatch")

    # first we compute I + L
    IplusL = [[0 for idx in range(len(A))] for idx in range(len(A))]
    for i in range(len(I)):
        for j in range(len(I)):    
            IplusL[i][j] = I[i][j] + L[i][j]

    # second we compute the inverse of I+L i.e. (I+L)^-1
    IplusLInvrs = get_matrix_inverse(IplusL)

    # third we compute the product of (I+L)^-1 * U
    H = generate_matrix_product(IplusLInvrs, U)

    # fourth we multiply all elements of H by -1 to get term -(I+L)^-1 * U
    for l in range(len(H)):
        for u in range(len(H[0])):
            elm = (-1) * H[l][u]
            elm = convertToDS(elm)
            H[l][u] = elm

    return H


if __name__ == "__main__":
    '''
          A = [
            [2, 1, 1],
            [1, 2, 1],
            [1, 1, 2]
        ]

        (I+L)^-1 * U = [
            [0, -1/2, -1/2],
            [0, 1/4, -1/4],
            [0, 1/8, 3/8]
        ]
    '''

    iterations = 1
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
                if row_idx == col_idx:
                    A[row_idx][col_idx] = random.randint(10, 20)
                else:                        
                    A[row_idx][col_idx] = random.randint(-6, 6)
            b[row_idx] = random.randint(-2, 2)

        '''
        A = [
            [6, -2, 1],
            [-2, 7, 2],
            [1, 2, -5]
        ]

        b  = [11, 5, -1]
        '''
              
        is_dd = is_diagonally_dominant(A)
        A2 = None
        if not is_dd:
            print("matrix is not diagonally dominant, attempting to make diagonally dominant")
            try:
                A2 = make_diagonally_dominant(A)
            except Exception as ex:
                print("Exception occurred while attempting to make diagonally dominant:", ex)  
            if A2:                      
                print("diagonally dominant matrix:\n", str_matrix(A2))
        
        if A2 is not None:
            A = A2

        original_matrix = str_matrix(A)
        result.append(original_matrix)
        constants_vector = str_vector(b)
        result.append(constants_vector)            
                

        normalizedA, I, L, U = generate_I_L_U_factorization(deepcopy(A))

        result.append(str_matrix(L))
        result.append(str_matrix(U))

        H = generate_iteration_matrix(I, L, U)
        iteration_matrix = str_matrix(H)
        result.append(iteration_matrix)

        l1, l2, l_infinity = generate_matrix_norms(H)

        result.append("l1-norm:{}\nl2-norm:{}\nl-infinity:{}".format(l1, l2, l_infinity))


        X1 = generate_one_iteration(A, X, b)
        sol = str_vector(X1)

        result.append(sol)


    print(tabulate(results, headers=("A", "b", "L", "U", "Iteration Matrix", "Norms", "Iteration-1"), tablefmt="grid"))
    
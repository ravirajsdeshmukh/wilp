from copy import deepcopy
import imp
from multiprocessing.spawn import import_main_path
from tabulate import tabulate
from utils import generate_vector_norms, generate_vector_substraction, str_matrix, str_vector, convertToDS
import random
from digonally_dominant import is_diagonally_dominant, make_diagonally_dominant
from gauss_jacobi_method import generate_one_iteration


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
    D = list()
    N = list()
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

        # A = [
        #     [6, -2, 1],
        #     [-2, 7, 2],
        #     [1, 2, -5]
        # ]

        # b  = [11, 5, -1]
              
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

        approximation = str_vector(X)                
        result.append(approximation) 

        E = list()
        L = list()
        for idx in range(0, 10):
            X1 = generate_one_iteration(A, deepcopy(X), b)
            sol = str_vector(X1)
            result.append(sol)
            V = generate_vector_substraction(X1, X)
            E.append(str_vector(V))
            X = X1
            l1, l2, l_infinity = generate_vector_norms(V)
            L.append(convertToDS(l2, 5))

        D.append(E)
        N.append(L)


    headers=["A", "b", "Iteration_0"]
    iterations = []
    for idx in range(1, 11):
        iterations.append("Iteration_" + str(idx))
    
    headers.extend(iterations)

    # Print original matrix A, constants vector V and value of X for each iteration
    print(tabulate(results, headers=headers, tablefmt="grid"))
 
    print(tabulate(D, headers=iterations, tablefmt="grid"))

    print(tabulate(N, headers=iterations, tablefmt="grid"))
       
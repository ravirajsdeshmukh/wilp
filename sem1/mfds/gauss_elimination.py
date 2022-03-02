from copy import deepcopy
from tabulate import tabulate
from utils import *
import math

'''
P1

x1 + x2 + x3 = 2
2x1 + 3x2 + 4x3 = 3
x1 - 2x2 - x3 = 1

P2

2x1 + x2 - x3 = 0
x1 + x3 = 4
x1 + x2 + x3 = 0

P3
x1 - x2 + x3 = 1
-x1     + x3 = 1
x1 + x2 - x3 = 0

P4
4x1 + 5x2 + 5x3 = 2
5x1 + 5x2 + 2x3 = 3
3x1 + 5x2 + 2x3 = 2
'''

localDs=5            

def reduced_echelon_form_with_pivoting(A):
    # operation counter to track the number of additions, multiplications and division
    counter = OpCount()

    # loop to perform gaussian elimination using partial pivoting
    # iterate from rows 0 to n-1
    for row_idx in range(len(A)):
        # perform partual pivoting by iterating through rows row_idx + 1 to (n-1)
        next_idx = row_idx + 1
        # initialize pivot row
        pivot_row = A[row_idx]
        # initialize the pivot row index
        pivot_idx = row_idx

        # iterate over the next rows to do partial pivoting
        for curr_idx in range(next_idx, len(A)):
            curr_row = A[curr_idx]
            if abs(pivot_row[row_idx]) < abs(curr_row[row_idx]):
                pivot_idx = curr_idx
                pivot_row = curr_row


        # exchange current row with the pivot row
        tmp = A[row_idx]
        A[row_idx] = A[pivot_idx]
        A[pivot_idx] = tmp

        # iterate over the next rows to perform Gauss Elimination
        for curr_idx, curr_row in enumerate(A[next_idx:]):
            factor = curr_row[row_idx]/pivot_row[row_idx]      # 1 division
            counter.IncrD()                                    # Record division operation
            factor = convertToDS(factor, localDs)
            for col_idx in range(pivot_idx, len(curr_row)):
                if col_idx == row_idx:
                    curr_row[col_idx] = convertToDS(0, localDs)
                    continue
                value = curr_row[col_idx]
                t = factor * pivot_row[col_idx]                 # 1 multiplication
                counter.IncrM()                                 # Record multiplication operation
                value = value - t                               # 1 addition(or subtraction)
                counter.IncrA()                                 # Record addition operation
                curr_row[col_idx] = convertToDS(value, localDs)    

    return A, counter

def reduced_echelon_form_without_pivoting(A):
    # operation counter to track the number of additions, multiplications and division
    counter = OpCount()

    # loop to perform gaussian elimination
    for pivot_idx in range(len(A)):
        pivot_row = A[pivot_idx]
        for row_idx, curr_row in enumerate(A[pivot_idx+1:]):
            if pivot_row[pivot_idx] == 0:
                raise Exception("encoutered 0 in the pivot position")
            factor = curr_row[pivot_idx]/pivot_row[pivot_idx]       # 1 division
            counter.IncrD()                                         # record 1 division operation
            factor = convertToDS(factor, localDs)
            for col_idx in range(pivot_idx, len(curr_row)):
                if col_idx == pivot_idx:
                    curr_row[col_idx] = convertToDS(0, localDs)
                    continue
                value = curr_row[col_idx]
                t = factor * pivot_row[col_idx]                     # 1 multiplication
                counter.IncrM()                                     # Record 1 multiplication operation
                value = value - t                                   # 1 subtraction
                curr_row[col_idx] = convertToDS(value, localDs)
                counter.IncrA()                                     # Record 1 addition/substration operation

    return A, counter               

def perform_back_sustitution(A):
    '''
    Matrix is expeced to be present in the REF form 
    with p(A) = p(A|b)
    '''
    # op counter to count the number of addtions, divisiona nd multiplications
    counter = OpCount()

    # perform back substitution
    sol = [0 for i in range(0, len(A))]

    for row_idx in range(len(A)-1, -1, -1):
        coeff_idx = row_idx
        curr_row = A[row_idx]
        l = len(curr_row)
        b = curr_row[l-1]
        for col_idx in range(coeff_idx, l-1):
            t = (sol[col_idx] * curr_row[col_idx])      # 1 multiplication
            counter.IncrM()                             # record one multiplication operation
            b = b - t                                   # 1 subtraction            
            counter.IncrA()                             # record one addition(or substraction) operation
        value = b / curr_row[coeff_idx]                 # 1 division
        counter.IncrD()                                 # record one division operation
        sol[coeff_idx] = convertToDS(value, localDs)

    return sol, counter

# compare rank of co-efficient matrix and augmented matrix
def compare_ranks(A):
    for row_idx, row in enumerate(A):
        for col_idx, col in enumerate(row):
            if (row_idx - col_idx) > 0:
                continue
            if col != 0:
                break
        if col_idx == row_idx:
            continue
        if col_idx == len(row)-1 and row[col_idx] == 0:
            raise Exception("Free variable found")
        if col_idx == len(row)-1 and row[col_idx] != 0:            
            raise Exception("Inconsistent system found")

if __name__ == "__main__":
    P1 = [
        [1, 1, 1, 2],
        [2, 3, 4, 3],
        [1, -2, -1, 1]
    ]

    P2 = [
        [2, 1, -1, 0],
        [1, 0, 1, 4],
        [1, 1, 1, 0]
    ]

    P3 = [
        [1, -1, 1, 1],
        [-1, 0, 1, 1],
        [1, 1, -1, 0]
    ]

    P4 = [
        [4, 5, 5, 2],
        [5, 5, 2, 3],
        [3, 5, 2, 2]
    ]

    # free variable found
    P5 = [
            [3, 2, 4, 3], 
            [4, 3, 4, 4], 
            [4, 3, 4, 4]
        ]
    
    P6 = [
        [1, 2, 0, 3, 4],
        [4, 3, 2, 1, 1],
        [3, 2, 1, 1, 2],
        [2, 1, 2, 1, 1]
    ]

    linear_systems = [P1, P2, P3, P4, P5, P6]
    # linear_systems = [P6]

    solutions = []
    for idx, A in enumerate(linear_systems):
        solution = list()
        solution.append(str_matrix(A))
        A1 = deepcopy(A)
        A1, counter1 = reduced_echelon_form_without_pivoting(A1)
        solution.append(str_matrix(A1))
        solution.append(str(counter1))
        try:
            compare_ranks(A1)
            sol1, counter2 = perform_back_sustitution(A1)    
            solution.append(str_vector(sol1))
            solution.append(str(counter2))
        except Exception as ex:
            solution.append("Free Var Found")
            solution.append("Free Var Found")
        
        A2 = deepcopy(A)
        A2, counter3  = reduced_echelon_form_with_pivoting(A2)
        solution.append(str_matrix(A2))
        solution.append(str(counter3))
        try:
            compare_ranks(A2)
            sol2, counter4 = perform_back_sustitution(A2)  
            solution.append(str_vector(sol2))
            solution.append(str(counter4))
        except Exception as ex:
            solution.append("Free Var Found")
            solution.append("Free Var Found")            
        solutions.append(solution)

    print(tabulate(solutions, headers=["System", "REF", "OpsREF", "Sol1", "OpsBS", "REF-WithPivot", "OpsREF-WithPivot", "Sol2-WithPivot", "OpsBS-WithPivot"], tablefmt="grid"))

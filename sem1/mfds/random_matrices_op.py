import imp
import random
from gauss_elimination import *
from tabulate import tabulate
from datetime import datetime

if __name__ == "__main__":
    n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    # n = [100, 200]
    solutions = list()
    for dim in n:
        A = [[0 for c in range(0, dim) ] for r in range(0, dim)]
        b = [0 for c in range(0, dim)]
        time_start = datetime.now()
        for row_idx in range(0, dim):
            for col_idx in range(0, dim):
                A[row_idx][col_idx] = random.randint(1, 5)
            b[row_idx] = random.randint(1, 5)

        for idx in range(len(A)):            
            A[idx].append(b[idx])
        time_end = datetime.now()
        print("Time taken to generate augmented matrix in microsecond:", time_end.microsecond)                    
        summary = list()
        try:
            summary.append(dim)           

            time_start = datetime.now()
            A1, counter1 = reduced_echelon_form_without_pivoting(A)         
            time_end = datetime.now()
            total_time = time_end - time_start
            summary.append(str(counter1))
            summary.append(time_end.microsecond)
            '''
            compare_ranks(A1)
            sol1, counter2 = perform_back_sustitution(A1)
            summary.append(str(counter2))
            '''
            print("Dim:", dim, "microsecond:", time_end.microsecond)
        except Exception as ex:
            print(ex)
            summary.append(ex)
        solutions.append(summary)

    print(tabulate(solutions, headers=["dimension", "OpCount", "Time(Microseconds)"], tablefmt="grid"))




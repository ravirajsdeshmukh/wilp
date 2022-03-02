from gauss_elimination import str_matrix
from tabulate import tabulate


def is_diagonally_dominant(A):
    # variable to indicate if the matrix is diagonally dominant or not
    isDD = True
    # iterate over all the rows of matrix A
    for row_index, row in enumerate(A):
        sum = 0                 # represents the absoluate sum of all elements except the diagonal element
        diagnoal = 0            # represents the absoluate value of diagonal element
        for col_index, column in enumerate(row):
            if row_index == col_index:
                diagnoal = abs(column)
            else:
                sum += abs(column)
        # check if digonal is smaller than or equal to sum                
        if diagnoal <= sum:
            isDD = False

    return isDD


def make_diagonally_dominant(A):
    # for each row try identify the index of dominant element,
    # i.e. element whose absoluate value is larger that sum of
    # all other elements. 
    # Populate array k in such a way that at each index will hold the
    # diagonally dominant row at that index from the original matrix A
    #   k[0] = 3 
    #   k[1] = 2
    #   k[2] = 0
    #   k[3] = 1
    k = [-1 for idx in range(len(A))]
    for row_index, row in enumerate(A):
        for idx in range(len(row)):
            elm = row[idx]
            sum = 0
            for col_index, column in enumerate(row):
                if idx == col_index:
                    continue
                sum = sum + abs(column)
            if elm > sum:
                k[idx] = row_index
                break

    # Initialize the empty matrix to populate from original matrix                
    A2 = [[0 for idx in range(len(A))] for idx in range(len(A))]
    for idx in range(len(k)):
        c = k[idx]
        # if the diagonally dominant element is not present for that 
        # index then raise an error
        if c == -1:
            raise Exception("Not possible to make diagonally dominant")
        A2[idx] = A[c]

    return A2


if __name__ == "__main__":
    '''
    Below P1, P2, P3 and P4 are input matrices for testing program
    '''
    P1 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    P2 = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]

    P3 = [
        [-1, 3, 4, 10],
        [0, 1, 0, 0],
        [10, 4, -3, 1],
        [0, 0, 1, 0]
    ]
    P4 = [
        [1, 0, 0],
        [2, 3, 4],
        [1, -2, -1]
    ]

    matrices = [P1, P2, P3, P4]

    results = list()
    for A in matrices:
        result = list()
        results.append(result)
        original = str_matrix(A)
        result.append(original)
        isDD = is_diagonally_dominant(A)
        if isDD:
            result.append("already DD")
            continue
        try:
            dd = make_diagonally_dominant(A)
        except Exception as Ex:
            result.append("Can't make DD")
            continue

        dd_matrix = str_matrix(dd)
        result.append(dd_matrix)

    # print the result in the tabular format
    print(tabulate(results, headers=[
          "Original", "Diagonally Dominant"], tablefmt="grid"))

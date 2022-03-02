import math

globaldS = 5

class OpCount:
    def __init__(self, disabled=False) -> None:
        self.A = 0
        self.M = 0
        self.D = 0
        self.disabled = disabled

    def IncrA(self):
        if self.disabled:
            return
        self.A = self.A + 1

    def IncrM(self):
        if self.disabled:        
            return
        self.M = self.M + 1

    def IncrD(self):        
        if self.disabled:        
            return        
        self.D = self.D + 1

    def __str__(self) -> str:
        return "Additions:{}\nMultiplications:{}\nDivisions:{}".format(self.A, self.M, self.D)

# print matrix
def str_matrix(A):
    matrix = "["
    for row_idx, row in enumerate(A):
        matrix += "["
        for col_idx, col in enumerate(A[row_idx]):
            matrix += str(col)
            if col_idx < len(A[row_idx])-1:
                matrix += " "
        matrix += "]" 
        if row_idx < len(A) -1:
            matrix += "\n" 
    matrix += "]"         
    return matrix      

# print vector
def str_vector(A):
    vector = "["
    for row_idx, row in enumerate(A):
        vector += str(row)
        if row_idx < len(A)-1:
            vector += "\n"
    vector += "]"         
    return vector  

# convert a number to dS arithmetic form
def convertToDS(num, dS=globaldS):
    '''
    num is the number to convert to DS 
    d number of significant digits required
    '''
    if dS == -1:
        return num
    factor5 = 5 / math.pow(10, (dS+1))
    num2 = factor5 + num
    num2 = format(num2,  "." + str(dS-1) + 'f')
    return float(num2)

# find maximum element of the array
def find_array_max(a, absolute=False):
    max = a[0] if not absolute else abs[a[0]]
    for idx, elm in enumerate(a):
        if absolute:
            elm = abs(elm)
        if elm > max:
            max = elm
    return max

# generate l1, l2 and l-infinity norms for a matrix
def generate_matrix_norms(A, dS=globaldS):
    '''
    Returns 3 norms for matrix
    l(1) - max of column sums
    l(infinity) - max of row sums
    l(2) - frobenius norm, square root of sum of squares of all element
    '''

    # find the l1 norm i.e. max column sum
    colum_sums = [0 for idx in range(len(A[0]))]
    for row_idx, row in enumerate(A):
        for col_idx, col in enumerate(row):
            colum_sums[col_idx] += abs(col)

    l1_norm = find_array_max(colum_sums)
    l1_norm = convertToDS(l1_norm, dS)

    # find the l infinity norm i.e. max row sum
    row_sums = [0 for idx in range(len(A))]
    for row_idx, row in enumerate(A):
        for col_idx, col in enumerate(row):
            row_sums[row_idx] += abs(col)

    l_infinity_norm = find_array_max(row_sums)
    l_infinity_norm = convertToDS(l_infinity_norm, dS)

    # find the l2 norm i.e. squre root of sum of squares of all elements
    elem_sqr_sum = 0
    for row_idx, row in enumerate(A):
        for col_idx, col in enumerate(row):
            elem_sqr_sum += col * col

    l2_norm = math.sqrt(elem_sqr_sum)
    l2_norm = convertToDS(l2_norm, dS)

    return l1_norm, l2_norm, l_infinity_norm      

# generate l1, l2 and l-infinity norms for a matrix
def generate_vector_norms(V):
    '''
    Returns 3 norms for matrix
    l(1) - max of column sums
    l(infinity) - max of row sums
    l(2) - frobenius norm, square root of sum of squares of all element
    '''

    # find the l1 norm i.e. absolute sum of all elements of vector
    l1_norm = 0
    for value in V:
        l1_norm += l1_norm + abs(value)

    # l infinity norm is the max element of vector om absolute terms
    l_infinity_norm = find_array_max(V)

    # find the l2 norm i.e. square root of sum of all elements
    sum = 0
    for value in V:
        sum = sum + (value * value)
    
    l2_norm = math.sqrt(sum)

    return l1_norm, l2_norm, l_infinity_norm            

def generate_matrix_product(A, B):
    if len(A[0]) != len(B):
        raise Exception("Cannot multiply, invalid matrix dimensions")

    P = [[0 for idx in range(len(A))] for idx in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(B[0])):
                P[i][k] += A[i][j] * B[j][k]

    return P    

def generate_matrix_addition(A, B):
    if len(A) != len(B) and len(A[0]) != len(B[0]):
        raise Exception("Cannot multiply, invalid matrix dimensions")

    A = [[0 for idx in range(len(A))] for idx in range(len(B))]
    for i in range(len(A)):
        for j in range(len(B)):
            A[i][j] = convertToDS(A[i][j] + B[i][j])

    return A

def generate_matrix_substraction(A, B):
    if len(A) != len(B) and len(A[0]) != len(B[0]):
        raise Exception("Cannot multiply, invalid matrix dimensions")

    A = [[0 for idx in range(len(A))] for idx in range(len(B))]
    for i in range(len(A)):
        for j in range(len(B)):
            A[i][j] = convertToDS(A[i][j] - B[i][j])

    return A    

def generate_vector_substraction(A, B, dS=globaldS):
    if len(A) != len(B):
        raise Exception("Cannot multiply, invalid matrix dimensions")

    S = [0 for idx in range(len(A))]
    for i in range(len(A)):
        S[i] = convertToDS(A[i] - B[i], dS)

    return S
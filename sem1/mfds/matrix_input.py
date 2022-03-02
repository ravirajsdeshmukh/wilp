
def get_input_from_cli():
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
    
    # Initialize matrix
    matrix = []   
    # For user input
    for i in range(R):          # A for loop for row entries
        a =[]
        for j in range(C):      # A for loop for column entries
            print("Enter element {},{}:".format(i+1, j+1))
            a.append(int(input()))
            # a.append(map(int, input()))
        matrix.append(a)
    
    # For printing the matrix
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end = " ")
        print()

    return matrix

if __name__ == "__main__":
    get_input_from_cli()
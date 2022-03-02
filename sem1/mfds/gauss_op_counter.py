
if __name__ == "__main__":
    dimensions = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for dim in dimensions:
        additions = (dim*dim-1) * (dim) * (1/3)
        multiplications = (dim*dim-1) * (dim) * (1/3)
        divisions = (1/2) * (dim) * (dim-1)
        print("Dim:{}, Additions:{}, Multiplications:{}, Divisions:{}, Total:{}".format(dim, additions, multiplications, divisions, (additions + multiplications + divisions)))        

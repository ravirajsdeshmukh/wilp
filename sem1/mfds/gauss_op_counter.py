import math
from utils import convertToDS
# average time taken computed
tt_addition =  0.059038
tt_multiplication = 0.082586
tt_division = 0.239391

if __name__ == "__main__":
    dimensions = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for dim in dimensions:
        additions = (dim*dim-1) * (dim) * (1/3)
        multiplications = (dim*dim-1) * (dim) * (1/3)
        divisions = (1/2) * (dim) * (dim-1)
        theretical_total_time = (additions * tt_addition) + (multiplications * tt_multiplication) + (divisions * tt_division)
        total_time = float(theretical_total_time) / math.pow(10, 6)
        total_time = convertToDS(total_time, 7)
        print("Dim:{}, Additions:{}, Multiplications:{}, Divisions:{}, Total-Ops:{}, Total-Time:{}".format(dim, additions, multiplications, divisions, (additions + multiplications + divisions), total_time))        



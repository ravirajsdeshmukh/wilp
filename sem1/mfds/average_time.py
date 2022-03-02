from audioop import mul
import math
import time
from tabulate import tabulate

start = 1
end = 1000000 + 1

def compute_addition_time():
    result = 0
    total_time = 0
    avg_time = 0
    time_start = time.process_time()
    for idx in range(start, end):
        result = result + idx
    time_end = time.process_time()
    total_time = (time_end - time_start)                                # total time in fractional seconds
    avg_time = (float(total_time) / float(end-1)) * math.pow(10, 6)     # average time in microseconds
    return total_time, avg_time

def compute_multiplication_time():
    result = 0
    total_time = 0
    avg_time = 0
    time_start = time.process_time()
    for idx in range(start, end):
        result = (end-idx) * (idx)
    time_end = time.process_time()
    total_time = (time_end - time_start)                                # total time in fractional seconds
    avg_time = (float(total_time) / float(end-1)) * math.pow(10, 6)     # average time in microseconds
    return total_time, avg_time

def compute_division_time():
    result = 0
    total_time = 0
    avg_time = 0
    time_start = time.process_time()
    for idx in range(start, end):
        result = float(end-idx)/float(idx)
    time_end = time.process_time()
    total_time = time_end - time_start                                  # total time in fractional seconds
    avg_time = (float(total_time) / float(end-1)) * math.pow(10, 6)
    return total_time, avg_time                                         # average time in microseconds

if __name__ == "__main__":
    results = list()
    addition = list()
    total_time, avg_time = compute_addition_time()
    addition.extend(["Addition", total_time, avg_time])

    multiplication = list()
    total_time, avg_time = compute_multiplication_time()
    multiplication.extend(["Multiplication", total_time, avg_time])

    division = list()
    total_time, avg_time = compute_division_time()
    division.extend(["Division", total_time, avg_time])

    results.extend([addition, multiplication, division])

    print(tabulate([addition, multiplication, division], headers=["Operation", "Total Time(Sec)", "Average Time(mS)"], tablefmt="grid"))


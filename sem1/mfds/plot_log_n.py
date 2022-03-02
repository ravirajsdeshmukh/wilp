import matplotlib.pyplot as plt
import numpy as np
import math


# solve for a and b
def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))
    print("slope:", b)
    print("intercept:", a)

    return a, b

if __name__ == "__main__":
    ypoints = np.array([0.030736,0.225368, 0.682324, 1.5764, 3.22768, 5.16081, 9.52642, 16.4807, 25.509, 34.4998])
    xpoints = np.array([100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0])
    for idx, x in enumerate(xpoints):
        x1 = math.log(x, 2)
        print("x:" + str(idx), x, x1)
        xpoints[idx] = x1

    for idx, y in enumerate(ypoints):
        print("y:" + str(idx), y)
        y = math.log(y, 2)
        
        ypoints[idx] = y        



    '''
    m, b = np.polyfit(xpoints, ypoints, 1)
    print("m:", m)        # slope
    print("b:", b)        # interceptor
    '''
    # solution
    a, b = best_fit(xpoints, ypoints)
    yfit = [a + b * xi for xi in xpoints]

    plt.xlabel("log(n)")
    plt.ylabel("log(T(n))")

    # make the scatter plot
    # plt.xticks(np.arange(min(xpoints), max(xpoints)+0.1, 0.1))
    plt.scatter(xpoints, ypoints)
    plt.plot(xpoints, yfit)

    plt.show()






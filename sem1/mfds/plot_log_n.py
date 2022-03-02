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
    xpoints = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    ypoints = []
    for x in xpoints:
        y = math.log(x, 2)
        ypoints.append(y)


    m, b = np.polyfit(xpoints, ypoints, 1)
    print("m:", m)        # slope
    print("b:", b)        # interceptor

    # solution
    a, b = best_fit(xpoints, ypoints)
    yfit = [a + b * xi for xi in xpoints]

    # make the scatter plot
    plt.scatter(xpoints, ypoints)
    plt.plot(xpoints, yfit)

    plt.show()






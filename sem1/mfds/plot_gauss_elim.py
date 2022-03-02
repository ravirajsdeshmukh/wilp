import matplotlib.pyplot as plt
import numpy as np
import math
from plot_log_n import best_fit

if __name__ == "__main__":
    xpoints = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    ypoints = np.array([671550, 5353100, 18044650, 42746200, 83457750, 144179300, 228910850, 341652400, 486403950, 667165500])

    m, b = np.polyfit(xpoints, ypoints, 1)
    print("m:", m)        # slope
    print("b:", b)        # interceptor

    a, b = best_fit(xpoints, ypoints)
    yfit1 = [a + b * xi for xi in xpoints]

    plt.scatter(xpoints, ypoints)
    plt.plot(xpoints, yfit1)

    # plt.show()
    plt.show()
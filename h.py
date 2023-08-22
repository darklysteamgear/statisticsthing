import numpy as np
from scipy import stats as st
# the main method
if __name__ == '__main__':
    c = 0
    largest = 0
    smallest = 0
    values = [3.4, 2.5, 4.8, 2.9, 3.6, 2.8, 3.3, 5.6, 3.7, 2.8, 4.4, 4.0, 5.2, 3.0, 4.8]
    mean = np.mean(values)
    median = np.median(values)
    mode = st.mode(values, keepdims=True)
    variance = st.variation(values, keepdims=True)
    standarddev = st.tstd(values)
    for x in values:
        c += 1
        if x > largest:
            largest = x
        if x < smallest:
            smallest = x
    rang = largest - smallest

    print("Mean: " + str(mean) + "\nMedian: " + str(median) + "\nMode: " + str(mode[0]) + "\nRange: " + str(rang) + "\nStandard Deviation: " + str(standarddev),"\nVariance: " + str(variance),"\nCount: " + str(c))
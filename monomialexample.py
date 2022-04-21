import polyhorner
import numpy as np


def main():
    # polynomial of order 3 in x
    Mat = np.array([1, 2, 3, 4, 6, 10], dtype=float)
    # We do not scale because the order of the polynomial is low and rounding error issues are unlikely
    X3 = polyhorner.horner(Mat, 3, Scale=False)
    print(X3['X'])
    
    # polynomial of order 15 in x
    # We do scale because the order of the polynomial is high and rounding error issues are very likely
    X15 = polyhorner.horner(Mat, 15)
    print(X15['X'])



if __name__ == '__main__':
    main()

import polyhorner
import numpy as np


def main():
    # polynomial of order 3 in x
    Mat = np.array([1, 2, 3, 4, 6, 10], dtype=float)
    X = polyhorner.horner(Mat, 3)
    print(X['X'])


if __name__ == '__main__':
    main()

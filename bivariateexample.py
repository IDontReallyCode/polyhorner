import polyhorner
import numpy as np

def main():
    # 2 input variables, 4 data points Mat is of size (4,2)
    Mat = np.array([[1,2],[3,-4],[-4,2],[1.5,-4]], dtype=float)
    # We wish to estimate a polynomial of order 4 in x1, and 3 in x2
    Expo = np.array([4,3],dtype=int)
    # We do not scale because the order of the polynomial is small and rounding error issues are unlikely
    X = polyhorner.horner(Mat,Expo, Scale=False)
    print(X['X'])
    done=1

#### __name__ MAIN()
if __name__ == '__main__':
    main()

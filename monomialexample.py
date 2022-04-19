import polyhorner
import numpy as np

def main():
    X = np.array([1,2,3,4,6,10], dtype=float)
    t = polyhorner.polyhorner.horner(X,3)
    print(t)

#### __name__ MAIN()
if __name__ == '__main__':
    main()

import numpy as np


def CalculateLeastSquaresSolution(Hmatrix, Ymatrix):
    # Enter Your Code Here to calculate the least Squares Solution
    Xmatrix = []
    Rmatrix = np.matmul(np.transpose(Hmatrix), Hmatrix)
    Rmatrix = np.linalg.inv(Rmatrix)
    Rmatrix = np.matmul(Rmatrix, np.transpose(Hmatrix))
    Xmatrix = np.matmul(Rmatrix, Ymatrix)

    return Xmatrix


def CalculateLineOfBestFitSolution(Dataset):
    # Generate the H and Y matrices for the Measurement Dataset
    Hmatrix = [[i[1], 1] for i in Dataset]
    Ymatrix = [i[0] for i in Dataset]
    LineParam = CalculateLeastSquaresSolution(Hmatrix, Ymatrix)
    return LineParam


def main():
    Dataset = list([[65, 1], [65, 2], [81, 3], [92, 4], [97, 5]])
    'Exercise 1'
    CalculateLineOfBestFitSolution(Dataset)




if __name__ == '__main__':
    main()
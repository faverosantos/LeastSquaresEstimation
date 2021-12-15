import numpy as np

def CalculateWeightedLeastSquaresSolution(Hmatrix, Rmatrix, Ymatrix):
    # Enter Your Code Here to calculate the least Squares Solution
    Xmatrix = []
    Pmatrix = []

    'Amatrix follows a set of operations'
    step1 = np.matmul(np.transpose(Hmatrix), np.linalg.inv(Rmatrix))
    Pmatrix = np.linalg.inv(np.matmul(step1, Hmatrix))
    step3 = np.matmul(Pmatrix, np.transpose(Hmatrix))
    Amatrix = np.matmul(step3, np.linalg.inv(Rmatrix))

    Xmatrix = np.matmul(Amatrix, Ymatrix)

    return Xmatrix, Pmatrix


def CalculateLineOfBestFitSolution(Dataset):
    # Generate the H, R and Y matrices for the Measurement Dataset
    Ymatrix = [i[0] for i in Dataset]
    Hmatrix = [[i[1], 1] for i in Dataset]
    Sigmamatrix = [i[2] for i in Dataset]

    ' This is an interesing usage of the multiplication of two matrices instead of using the line by line multiplication'
    Rmatrix = np.eye(len(Sigmamatrix)) * np.transpose(np.power(Sigmamatrix, 2))


    LineParam, LineParamCov = CalculateWeightedLeastSquaresSolution(Hmatrix, Rmatrix, Ymatrix)
    return LineParam


def main():
    Dataset = list([[65, 1, 5], [65, 2, 5], [81, 3, 1], [92, 4, 2], [97, 5, 3]])
    'Exercise 2'
    CalculateLineOfBestFitSolution(Dataset)

if __name__ == '__main__':
    main()
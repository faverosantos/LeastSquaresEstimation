import numpy as np


def CalculateRecursiveLeastSquaresSolution(Xmatrix, Pmatrix, Hmatrix, Rmatrix, Ymatrix):
    # Enter Your Code Here to calculate the Recursive Least Squares Solution
    Kmatrix = []


    step1 = np.matmul(Pmatrix, np.transpose(Hmatrix))
    step2 = np.matmul(Hmatrix, Pmatrix)
    step3 = np.linalg.inv(np.matmul(step2, np.transpose(Hmatrix)) + Rmatrix)
    Kmatrix = np.matmul(step1, step3)
    Xmatrix = Xmatrix + np.matmul(Kmatrix, Ymatrix - np.matmul(Hmatrix, Xmatrix))
    PmatrixIdentity = np.eye(len(Hmatrix))
    step4 = PmatrixIdentity - np.matmul(Kmatrix, Hmatrix)
    step5 = np.matmul(step4, Pmatrix)
    step6 = np.matmul(step5, np.transpose(step4))
    step7 = np.matmul(Kmatrix, Rmatrix)
    step8 = np.matmul(step7, np.transpose(Kmatrix))
    Pmatrix = step6 + step8

    return Xmatrix, Pmatrix


def CalculateLineOfBestFitSolution(LineParam, LineParamCov, Dataset):
    # Generate the H, R and Y Matrices (or scalars for Y and R)
    Hmatrix = []
    Rmatrix = []
    Ymatrix = []

    Ymatrix = [i[0] for i in Dataset]
    Hmatrix = [[i[1], 1] for i in Dataset]
    Sigmamatrix = [i[2] for i in Dataset]

    ' This is an interesing usage of the multiplication of two matrices instead of using the line by line multiplication'
    Rmatrix = np.eye(len(Sigmamatrix)) * np.transpose(Sigmamatrix)


    LineParam, LineParamCov = CalculateRecursiveLeastSquaresSolution(LineParam, LineParamCov, Hmatrix, Rmatrix, Ymatrix)
    return LineParam, LineParamCov

def main():
    Dataset = list([[65, 1, 25], [65, 2, 25], [81, 3, 1], [92, 4, 4], [97, 5, 9]])
    'Exercise 3'

    'Initial guess'
    RPMmatrix = [i[1] for i in Dataset]
    Xmatrix = np.eye(len(RPMmatrix)) * np.mean(RPMmatrix)
    residualMatrix = RPMmatrix - Xmatrix
    Pmatrix = np.eye(len(RPMmatrix)) * np.mean(np.matmul(residualMatrix, np.transpose(residualMatrix)))

    CalculateLineOfBestFitSolution(Xmatrix, Pmatrix, Dataset)

if __name__ == '__main__':
    main()
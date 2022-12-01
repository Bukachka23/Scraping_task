# A system of linear equations

#1 Solving with a function numpy.linalg.solve.
import numpy as np
A = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]) # матрица 4 на 4
b = np.array([1, 2, 3, 4])                                             # Массив коэффициентов матрицы
x = np.linalg.solve(A, b)
print("Solving with solve=",x)


#2 Solution with inverse matrix
Ainv=np.linalg.inv(A)                                                  # The function linalg.inv() calculates the inverse matrix.
x=Ainv.dot(b)                                                          # The scalar product of two arrays.
print("Solution with inverse matrix=",x)


#3 Solving by Cramer's method
import numpy as np
A1 = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]] # The list of matrix coefficients
B1 = [1, 2, 3, 4]                                             # A list of vectors of free members
def Kram(A,B):                                                # Cramer user function
    m = len(A)                                                # Determine the number of rows in the matrix (how many equations)
    det_m = np.linalg.det(A)                                  # Determinant of the coefficient matrix
    r = list()                                                # Put the result of finding the unknowns in the list
    for i in range(m):                                            # Loop - which allows you to replace the vector-column matrix by the coefficients of the free terms
        VM = np.copy(A)                                           # Creating an auxiliary matrix
        B = VM[:,i]                                                # To access the corresponding column in the list
        r.append(np.linalg.det(VM)/ det_m)                        # Calculating a system of linear equations by dividing the determinant of a matrix by the determinant
    return r                                                  # Return the result in a list
X3 = Kram(A1,B1)                                              # Call the Kramer function
print("Solution with Cramer's method",X3)
print(np.matmul(A,X3))

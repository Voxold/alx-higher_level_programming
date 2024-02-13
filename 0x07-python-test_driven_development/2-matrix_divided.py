#!/usr/bin/python3
def matrix_divided(matrix, div):
	#Checks for matrix & divisor
    	if not isinstance(matrix, list) or len(matrix) == 0:
        	raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    	if not isinstance(div, (int, float)):
        	raise TypeError("div must be a number")
    	if div == 0:
        	raise ZeroDivisionError("division by zero")

    	new_matrix = []

    	for row in matrix:
		if not isinstance(row, list) or len(row) == 0:
            		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        	if len(row) != len(matrix[0]):
            		raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
    	return (new_matrix)

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    ''' prints a matrix of integers '''
    if matrix == [[]] or len(matrix) == 1 :
        return matrix

    for each in range(0, len(matrix)):
        for every in matrix[each]:
            print('{:d}'.format(every),  end=' ')
        print()

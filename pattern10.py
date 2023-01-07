# Vertically printing symbols based on input_array values

import numpy as np

def pattern(input_array=np.array([]), symbol='*'):
    i = input_array.max()

    while i > 0:
        for j in input_array:
            if j >= i:
                print(symbol, end=' ')
            else :
                print(' ', end=' ')
        print()
        i -= 1

def main():
    array1 = np.array([1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1])
    print('For array ', array1, ' the pattern is :')
    pattern(array1)

    array2 = np.array([5,3,6,2,4])
    print('For array ', array2, ' the pattern is :')
    pattern(array2, '#')

    array3 = np.array([3,5,3,5,3,5,3,5])
    print('For array ', array3, ' the pattern is :')
    pattern(array3, symbol = '$')

main()
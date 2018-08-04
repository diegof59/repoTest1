import math
import os
import random
import re
import sys

# From:
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


# Recibe una matriz cuadrada 6x6, la cual contiene relojes de arena.
# Devuelve la mayor entre las sumas de los elementos de cada reloj de arena.
def hourglassSum(arr):

for i in range(6):
	for j in range(6):
		
		



if __name__ == '__main__':
    
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
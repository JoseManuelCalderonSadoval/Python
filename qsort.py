#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
#
# ## #############################################################

import sys
import matplotlib.pyplot as plt
from random import randint, seed
from time import perf_counter

def swap(A, i, j):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp
# end def


def quicksort(A, p, r):
	if p < r:
		q = partition(A, p, r) #partition -> metodo de ordenamiento
		quicksort(A, p, q-1)
		quicksort(A, q+1, r)
# end def


def partition(A, p, r):
	x = A[r]
	i = p-1
	for j in range(p, r):
		if A[j] <= x:
			i+= 1
			swap(A, i, j)
	swap(A, i+1, r)
	return i+1
# end def


def plot(x, y):
	plt.title("Time graph")
	plt.plot(x, y,'go')
	plt.xlabel("PASSWORD LENGTH")
	plt.ylabel("TIME")
	plt.grid(True)
	plt.show()
#end def

def main(argv):
	#max_n = int(argv[1])
	n = list(range(3, 10))
	times = []
	seed(69)
	for size in n:
		A = [randint(-size, size+1) for i in range(size)]
		if A != all(caracter.islower() and caracter in string.ascii_lowercase for caracter in n):
			return
		start = perf_counter()
		quicksort(A, 0, len(A)-1)
		elapsed = perf_counter() - start
		times.append(elapsed)
	plot(n, times)

if __name__ == '__main__':
	main(sys.argv)

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

def insertionsort(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j-1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i-=1
		A[i+1] = key
# end def

def plot(x, y):
	plt.title("Time graph")
	plt.plot(x, y,'go')
	plt.legend(["EXECUTION TIME"])
	plt.xlabel("INPUT VALUE")
	plt.ylabel("TIME")
	plt.grid(True)
	plt.show()
#end def

def main(argv):
	max_n = int(argv[1])
	n = list(range( 1, max_n+1))
	times = []
	seed(69)
	for size in n:
		A = [randint(-size, size+1) for i in range(size)]
		start = perf_counter()
		insertionsort(A)
		elapsed = perf_counter() - start
		times.append(elapsed)
	plot (n, times)

if __name__ == '__main__':
	main(sys.argv)

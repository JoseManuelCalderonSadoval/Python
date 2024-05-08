#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
#
# ## #############################################################
import sys
from time import perf_counter, sleep

def fact(n):
	f = 1
	for i in range(2, n+1):
		f*= i
	return f
	
#def foo():
#	sleep(1)

def main(argv):
	start = perf_counter()
	n = int(argv[1])
	fact(n)
	elapsed = perf_counter() - start
	print("Foo took {:.2f}ms".format(elapsed*1000))


if __name__ == '__main__':
	main(sys.argv)

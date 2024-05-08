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
	return 1 if n <= 1 else n * fact(n-1)
	
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

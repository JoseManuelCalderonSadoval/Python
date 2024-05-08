#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
#
# ## #############################################################

import sys

def fact(n):
	f = 1
	for i in range(2, n+1):
		f*= i
	return f

def main(argv):
	n = int(argv[1])
	print(n, "! = ", fact(n), sep="")


if __name__ == '__main__':
	main(sys.argv)

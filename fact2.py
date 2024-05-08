#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
#
# ## #############################################################

import sys

def fact(n):
	return 1 if n <= 1 else n * fact(n-1)

def main(argv):
	n = int(argv[1])
	print(n, "! = ", fact(n), sep="")


if __name__ == '__main__':
	main(sys.argv)

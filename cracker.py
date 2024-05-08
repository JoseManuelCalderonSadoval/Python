#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
#
# ## #############################################################

import sys
from random import randint, seed, choice
from time import perf_counter

dictionary = "0123456789"

def randompwd(n):
	pwd = ''
	for i in range(n):
		pwd+= choice(dictionary)
	return pwd
# end def

def genpwd(counters):
	mypwd = [None] * len(counters)

	for i in range(len(counters)-1, -1, -1):
		if counters[i] >= len(dictionary):
			counters[i] = 0
			counters[i-1]+= 1
		mypwd[i] = dictionary[ counters[i] ]
	counters[-1]+= 1
	return ''.join(mypwd)
# end def

def guesspwd(pwd, n):
	counters = [0] * n
	while counters[0] < len(dictionary):
		mypwd = genpwd(counters)
		if(pwd == mypwd):
			print(pwd, '==', mypwd)
			break
		# else:
		# 	print(pwd, '!=', mypwd)
	print('Password not found')
# end def

def time2str(t):
	t = t*1000000
	ldiv    = [1000, 1000, 60, 60, 24]
	lsuffix = ['us', 'ms', 's', ' minutes', ' hours', ' days']
	ix = 0
	while (ix < len(ldiv)) and (t > ldiv[ix]):
		t/= ldiv[ix]
		ix+=1
	return '{:0.2f}{}'.format(t, lsuffix[ix])
# end def

def main(argv):
	# seed(69)
	n = int(argv[1]) or 3 if len(argv) > 1 else 3
	# pwd = randompwd(n)
	pwd = '9' * n
	print('Randomly generated password:', pwd)
	print('Trying to guess password')
	start = perf_counter()
	guesspwd(pwd, n)
	elapsed = perf_counter() - start
	print('Brute-force password guess took ', time2str(elapsed))
# end def

if __name__ == '__main__':
	main(sys.argv)

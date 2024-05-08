#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
#
# ## #############################################################
import sys
import matplotlib.pyplot as plt
import numpy as np

coins = {
	0.1 : 3,
	0.2 : 3,
	0.5 : 2,
	1 : 0,
	2 : 3,
	5 : 0,
	10 : 3,
	20 : 3,
	50 : 3,
	100 : 3,
}

def change(amount):
	i = np.array(sorted(coins.keys(), reverse=True))
	my_change = []
	for coin in i:
		num_coins = min(coins[coin], amount // coin)
		my_change.append(num_coins)
		amount -= num_coins * coin
	return i, np.array(my_change)
# end def

def plot(amount):
	denominations, num_coins_list = change(amount)
	plt.title("Graph of the change given for the amount of {}".format(amount))
	plt.bar(denominations, num_coins_list, align='center', alpha=0.5)
	plt.xlabel("Denomination")
	plt.ylabel("Number of coins")
	plt.show()
#end def

def main(argv):
	amount = float(argv[1])
	plot(amount)

if __name__ == '__main__':
	main(sys.argv)

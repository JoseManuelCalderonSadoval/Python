#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Calderón Sandoval José Manuel 
#
# ## #############################################################
import sys
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
	i = sorted(coins.keys(), reverse=True)
	my_change = []
	for coin in i:
		num_coins = min(coins[coin], amount // coin)
		my_change.append([coin, num_coins])
		amount -= num_coins * coin
	return my_change
# end def


def main(argv):
	amount = float(argv[1])
	print("Cambio de", amount, "en:")
	for (coin, num) in sorted(change(amount), reverse=True):
		if not num:
			continue
		print(num,
			"moneda" if num == 1 else "monedas",
			"de",
			coin if coin >= 1 else coin * 10,
			"pesos" if coin >= 1 else "centavos")

# end def


if __name__ == '__main__':
	main(sys.argv)

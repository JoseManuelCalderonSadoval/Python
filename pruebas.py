#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
#
# ## #############################################################
import sys
import numpy as np
import matplotlib.pyplot as plt

coins = {
    0.1: 3,
    0.2: 3,
    0.5: 2,
    1: 0,
    2: 3,
    5: 0,
    10: 3,
    20: 3,
    50: 3,
    100: 3,
}

def change(amount):
    denominations = np.array(sorted(coins.keys(), reverse=True))
    num_coins_list = []
    remaining_amount = amount

    for coin in denominations:
        num_coins = min(coins[coin], remaining_amount // coin)
        num_coins_list.append(num_coins)
        remaining_amount -= num_coins * coin

    return denominations, np.array(num_coins_list)

def plot_change(amount):
    denominations, num_coins_list = change(amount)
    plt.bar(denominations, num_coins_list, align='center', alpha=0.5)
    plt.xlabel('Denominación')
    plt.ylabel('Cantidad de monedas')
    plt.title('Cantidad de monedas para el monto de {}'.format(amount))

    # Añadir etiquetas a las barras
    for i in range(len(denominations)):
        plt.text(denominations[i], num_coins_list[i], str(num_coins_list[i]), ha='center', va='bottom')

    plt.xticks(denominations, rotation=45, ha='right')
    plt.show()


def main(argv):
    if len(argv) != 2:
        print("Uso: python3 programa.py <monto>")
        sys.exit(1)

    amount = float(argv[1])
    plot_change(amount)

if __name__ == '__main__':
    main(sys.argv)

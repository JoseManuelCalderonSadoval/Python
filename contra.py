import sys
import matplotlib.pyplot as plt
import time
import string
import random

def generar_contraseña(n):
    return ''.join(random.choices(string.ascii_lowercase, k=n))

def fuerza_bruta(contraseña):
    intentos = 0
    while True:
        intentos += 1
        contraseña_generada = generar_contraseña(len(contraseña))
        if contraseña_generada == contraseña:
            return intentos

def plot(x, y):
    plt.title("Tiempo de cómputo en función de la longitud de la contraseña")
    plt.plot(x, y, 'go-')
    plt.xlabel("Longitud de la contraseña")
    plt.ylabel("Tiempo (segundos)")
    plt.grid(True)
    plt.show()

def verf_seed(contraseña):
    return all(caracter.islower() and caracter in string.ascii_lowercase for caracter in contraseña)

def main(argv):
    max_n = int(argv[1])
    n = list(range(3, 11))
    times = []
    for size in n:
        contraseña = generar_contraseña(size)
        if not verf_seed(contraseña):
            print("La contraseña generada no cumple con los requisitos (debe ser minúscula y pertenecer al alfabeto en inglés).")
            return
        start = time.perf_counter()
        intentos = fuerza_bruta(contraseña)
        elapsed = time.perf_counter() - start
        times.append(elapsed)
    plot(n, times)

if __name__ == '__main__':
    main(sys.argv)

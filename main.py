import msvcrt
import time
import os
import random

from funcoes import capturar_digitos

def main():
    print("Inicio do programa Sinforoso")
    
    resposta = capturar_digitos()
    print("\nTexto capturado no teclado:", resposta)


if __name__ == "__main__":
    main()



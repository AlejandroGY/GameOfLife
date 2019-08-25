# /usr/env/bin python
# encoding:utf-8

import random
import itertools
import os, time

UNIX = False
clear = lambda: os.system('clear') if UNIX else os.system('cls')

class GameOfLife(object):
   def __init__(self, filas, columnas):
      self.filas = filas
      self.columnas = columnas

      fila_vida = lambda: [random.randint(0, 1) for i in range(self.columnas)]
      self.juego = [fila_vida( ) for i in range(self.filas)]

   def __str__(self):
      juego = ''
      for fila in self.juego:
         for celula in fila:
            juego += '■ ' if celula else '. '
         juego += '\n'
      return juego

   def vecinos(self, nf, nc):
      distancias_vecinos = list(set(itertools.permutations([-1, -1, 1, 1, 0], 2)))
      fuera_de_juego = lambda x, y: not(x in range(self.filas) and y in range(self.columnas))

      res = 0
      for dist_fila, dist_columna in distancias_vecinos:
         dx = nf + dist_fila
         dy = nc + dist_columna
         if not fuera_de_juego(dx, dy):
            res += 1 if self.juego[dx][dy] else 0
      return res
   
   def recorrer(self):
      for nf in range(self.filas):
         for nc in range(self.columnas):
            vecinos = self.vecinos(nc, nf)

            if vecinos < 2 or vecinos > 3:
               self.juego[nf][nc] = 0
            elif vecinos == 3:
               self.juego[nf][nc] = 1

def main( ):
   clear( )
   print("------------------------------")
   print("Bienvenido al juego de la vida")
   print("------------------------------")

   n = int(input("N >> "))
   juego = GameOfLife(n, n)

   while True:
      clear( )
      print(juego)
      juego.recorrer( )
      time.sleep(1)

if __name__ == "__main__":
   main( )

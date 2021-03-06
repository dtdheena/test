import matplotlib.pyplot as plt
import numpy as np
import cv2
import json
import os

def Colores(paleta, x, archivo):
  
  # Construyo la paleta
  figure = plt.figure(figsize=(6, 2), dpi=80)
  gradient = np.linspace(0, 1, 256)
  gradient = np.vstack((gradient, gradient))
  
  # La guardo como imagen
  plt.imshow(gradient, aspect='auto', cmap=paleta)
  plt.savefig('paleta.png')

  #-----------------------------------------------

  # Cargo la imagen con cv2
  imagen = cv2.imread('paleta.png')
  cv2.imshow('a', imagen)
  yy, xx, zz = imagen.shape
  maximo = 431    # extremo izquierdo donde comienza borde blanco
  minimo = 61     # extremo derecho donde termina borde blanco
  y = yy//2       # coordenada central de la imagen

  deltaColor = (maximo-minimo)/(len(x)) 
  puntosTest = [round(i*deltaColor + minimo) for i in range(len(x))]

#'#%02x%02x%02x' % (0, 128, 64)


  # Lista donde cada elemento es una lista rgb en cada punto de test
  color = [list(imagen[y][i]) for i in puntosTest]
  dic = {}
  for i in range(len(x)):
    key = "{0:.2f}".format(x[i])  # trunco a 2 decimales
    value = list(color[i])   # Cada elemento es [ B G R]
    value.reverse()     # invierto lista
    value = '#%02x%02x%02x' % tuple(value)
    dic[key] = value    # agrego elemento

  with open(archivo, 'w') as f:
    f.write( str(json.dumps(dic)) )

  os.system('rm paleta.png')

  return dic


if (__name__ == '__main__'):
  
  x = [i for i in np.linspace(-1,1,10)]
  Colores('viridis', x, 'datos.json')

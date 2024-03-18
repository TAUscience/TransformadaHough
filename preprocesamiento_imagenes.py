import numpy as np
from PIL import Image

import random
import canny


def obtener_nombres_imagenes_aleatorias(n):
    numeros_img=random.sample(range(1, 289 + 1), n)
    nombres_img=[]
    for numero in numeros_img:
        numero_cadena=str(numero)
        nombres_img.append("image_224 ("+numero_cadena+").png")

    return nombres_img


def obtener_imagenes(n,nombre_carpeta):
    nombre_imagenes=obtener_nombres_imagenes_aleatorias(n)
    imagenes_prepro=[]

    for nombre in nombre_imagenes:
        ruta_img=nombre_carpeta+"/"+nombre
        imagenes_prepro.append(canny.aplicar_canny(ruta_img))
    
    return imagenes_prepro


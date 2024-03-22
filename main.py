import preprocesamiento_imagenes as prepro
import trans_hough as hough

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#Traer las imagenes preprocesadas
cantidad_img=2                      # <<< Modificar para traer más o menos imagenes
carpeta_img="imagenes_KITTI"        # <<< Carpeta en que se encuentran las imagenes
mis_imagenes=prepro.obtener_imagenes(cantidad_img,carpeta_img)

for imagen in mis_imagenes:
    buscar_numero_lineas=5 #        <<< CAMBIAR PARA BUSCAR MÁS O MENOS LINEAS
    plt.imshow(imagen,cmap='gray')
    plt.title("Imagen preprocesada con Canny")
    plt.show()

    espacio_parametros,picos,img_lineas=hough.encuentra_lineas_hough(imagen,buscar_numero_lineas)
    plt.imshow(espacio_parametros,cmap="gray")
    plt.title("Espacio de parámetros")
    plt.show()

    plt.imshow(picos)
    plt.title(f'Buscando {buscar_numero_lineas} picos en espacio de parámetros')
    plt.show()

    plt.imshow(img_lineas)
    plt.title(f'Buscando {buscar_numero_lineas} lineas en la imagen')
    plt.show()


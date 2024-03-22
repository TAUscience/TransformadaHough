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
    plt.imshow(imagen,cmap='gray')
    plt.show()

    espacio_parametros,picos,img_lineas=hough.encuentra_lineas_hough(imagen,2)
    plt.imshow(espacio_parametros,cmap="gray")
    plt.show()

    plt.imshow(picos)
    plt.show()

    plt.imshow(img_lineas)
    plt.show()


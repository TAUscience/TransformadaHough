import preprocesamiento_imagenes as prepro

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#Traer las imagenes preprocesadas
cantidad_img=5                      # <<< Modificar para traer más o menos imagenes
carpeta_img="imagenes_KITTI"        # <<< Carpeta en que se encuentran las imagenes
mis_imagenes=prepro.obtener_imagenes(cantidad_img,carpeta_img)

for imagen in mis_imagenes:
    plt.imshow(imagen,cmap='gray')
    plt.show()




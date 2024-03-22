import numpy as np
import matplotlib.pyplot as plt
import math

#Entrada imagen binaria

def normalizar(valor_original, rango_original_min, rango_original_max, rango_nuevo_min, rango_nuevo_max):
    rango_original = rango_original_max - rango_original_min
    rango_nuevo = rango_nuevo_max - rango_nuevo_min
    valor_normalizado = ((valor_original - rango_original_min) / rango_original) * rango_nuevo + rango_nuevo_min
    return valor_normalizado

def grados_a_radianes(grados):
    return (grados * math.pi) / 180    

def un_canal_a_tres(imagen):
    filas=len(imagen)
    cols=len(imagen[0])

    imagen3_canales=np.zeros((filas,cols,3),dtype="int")
    for i in range(filas):
        for j in range(cols):
            imagen3_canales[i][j]=imagen[i][j]
    return imagen3_canales


def encuentra_lineas_hough(imagen, n_lineas):
    x=len(imagen)
    y=len(imagen[0])

    #Rango de parámetros
    rho_inf=-np.sqrt(2)*len(imagen)
    rho_sup=np.sqrt(2)*len(imagen)
    theta_inf=-90
    theta_sup=90

    #Crear matriz de parámetros
    acumulador=np.zeros((int(rho_sup)*2,180), dtype=int)
    
    #Recorrer imagen buscando puntos de interés
    for x_i in range(x):
        for y_i in range(y):
            #Cuando encuentre un punto de interés
            if(imagen[x_i][y_i]==255):
                #Calcular curva sinusoidal en espacio de parámetros
                for theta in range(len(acumulador[0])):
                    theta_normalizado_radianes=grados_a_radianes( normalizar(theta,0,179,-90,90) )
                    rho=x_i*np.cos(theta_normalizado_radianes)+y_i*np.sin(theta_normalizado_radianes)
                    rho_desnormalizado=round(normalizar(rho,int(rho_inf),int(rho_sup),0,int(rho_sup)*2-1))
                    acumulador[rho_desnormalizado][theta]+=1
    
    #Encontrar los n índices del valor máximo
    indices_ordenados = np.argsort(acumulador, axis=None)[::-1][:n_lineas]
    # Convertir los índices plano a pares de índices (fila, columna)
    rhos_max, thetas_max = np.unravel_index(indices_ordenados, acumulador.shape)
    
    puntos=np.zeros((int(rho_sup)*2,180,3),dtype="int")
    for i in range(n_lineas):
        puntos[rhos_max[i]][thetas_max[i]][1]=255
    
    img_con_lineas=un_canal_a_tres(imagen)
    
    #Para cada coordenada (rho,theta) calcular recorriendo x
    for i in range(n_lineas):
        rho_max_k=rhos_max[i]
        theta_max_k=thetas_max[i]

        for x_k in range(x):
            y_k=-(  grados_a_radianes(np.cos(normalizar(theta_max_k,0,179,-90,90))) / grados_a_radianes(np.sin(normalizar(theta_max_k,0,179,-90,90))) )*x_k + ( normalizar(rho_max_k,0,int(rho_sup)*2-1,int(rho_inf),int(rho_sup)) / grados_a_radianes(np.sin(normalizar(theta_max_k,0,179,-90,90))) )
            if y_k >= 0 and y_k < y:
                img_con_lineas[x_k][int(y_k)][1]=255

    return acumulador, puntos, img_con_lineas






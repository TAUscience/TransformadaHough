
import subprocess

def verificar_opencv():
    try:
        # Intenta importar OpenCV
        import cv2
    except ImportError:
        # Si OpenCV no está instalado, instálalo usando pip
        subprocess.check_call(["pip", "install", "opencv-python"])

def aplicar_canny(ruta_imagen):
    verificar_opencv()
    import cv2
    
    # Leer la imagen en su formato original (a color)
    imagen = cv2.imread(ruta_imagen)

    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar el algoritmo de detección de bordes de Canny
    bordes_canny = cv2.Canny(imagen_gris, 100, 200)  # Umbral inferior y superior

    return bordes_canny
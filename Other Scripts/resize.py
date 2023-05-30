import cv2
import os


ruta_carpeta = 'C:/UPC-2023-01/TP1/SOURCE/images/'
archivos = os.listdir(ruta_carpeta)

for a in archivos:
    im = ruta_carpeta+a

    imagen = cv2.imread(im)
    
    imagen_redimensionada = cv2.resize(imagen, (500, 500))
    
    
    nombre_nueva_imagen = 'C:/UPC-2023-01/TP1/SOURCE/images proccessed/'+a
    cv2.imwrite(nombre_nueva_imagen, imagen_redimensionada)
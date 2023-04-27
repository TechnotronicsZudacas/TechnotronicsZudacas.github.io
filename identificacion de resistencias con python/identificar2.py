import cv2
import numpy as np

# Cargar la imagen de la resistencia
img = cv2.imread("resistencia.jpg")

# Definir los límites de los colores a detectar
lower = np.array([0, 0, 150])
upper = np.array([150, 150, 255])

# Filtrar los colores en la imagen
mask = cv2.inRange(img, lower, upper)

# Encontrar los contornos de los objetos en la imagen filtrada
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Ordenar los contornos de izquierda a derecha
contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

# Crear una lista para almacenar los colores
colors = []

# Identificar el código de colores de la resistencia
for contour in contours:
    # Obtener las coordenadas del contorno
    x, y, w, h = cv2.boundingRect(contour)
    # Recortar la sección de la imagen correspondiente al contorno
    roi = img[y:y+h, x:x+w]
    # Calcular el color predominante en la sección recortada
    color = np.mean(np.mean(roi, axis=0), axis=0)
    # Convertir el color a su correspondiente código de color en resistencias
    if color.tolist() == [0.0, 0.0, 255.0]:
        colors.append("Rojo")
    elif color.tolist() == [0.0, 255.0, 0.0]:
        colors.append("Verde")
    elif color.tolist() == [255.0, 255.0, 0.0]:
        colors.append("Amarillo")
    elif color.tolist() == [255.0, 165.0, 0.0]:
        colors.append("Naranja")
    elif color.tolist() == [255.0, 0.0, 0.0]:
        colors.append("Marrón")
    elif color.tolist() == [255.0, 255.0, 255.0]:
        colors.append("Blanco")
    elif color.tolist() == [0.0, 0.0, 0.0]:
        colors.append("Negro")
    elif color.tolist() == [128.0, 128.0, 128.0]:
        colors.append("Gris")
    elif color.tolist() == [186.0, 85.0, 211.0]:
        colors.append("Morado")
    elif color.tolist() == [255.0, 192.0, 203.0]:
        colors.append("Rosa")
    elif color.tolist() == [255.0, 215.0, 0.0]:
        colors.append("Oro")
    elif color.tolist() == [128.0, 128.0, 0.0]:
        colors.append("Café")

# Imprimir los colores identificados
print("Los colores de la resistencia son:", ", ".join(colors))

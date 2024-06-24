import cv2
import numpy as np

def nothing(x):
    pass

# Crear una ventana
cv2.namedWindow('HSV Selector')

# Crear los trackbars para los valores mínimos y máximos de HSV
cv2.createTrackbar('Hue Min', 'HSV Selector', 0, 179, nothing)
cv2.createTrackbar('Sat Min', 'HSV Selector', 0, 255, nothing)
cv2.createTrackbar('Val Min', 'HSV Selector', 0, 255, nothing)
cv2.createTrackbar('Hue Max', 'HSV Selector', 179, 179, nothing)
cv2.createTrackbar('Sat Max', 'HSV Selector', 255, 255, nothing)
cv2.createTrackbar('Val Max', 'HSV Selector', 255, 255, nothing)

while True:
    # Leer los valores de los trackbars
    hue_min = cv2.getTrackbarPos('Hue Min', 'HSV Selector')
    sat_min = cv2.getTrackbarPos('Sat Min', 'HSV Selector')
    val_min = cv2.getTrackbarPos('Val Min', 'HSV Selector')
    hue_max = cv2.getTrackbarPos('Hue Max', 'HSV Selector')
    sat_max = cv2.getTrackbarPos('Sat Max', 'HSV Selector')
    val_max = cv2.getTrackbarPos('Val Max', 'HSV Selector')

    # Crear una imagen en negro para mostrar los valores
    img = np.zeros((100, 600, 3), np.uint8)
    cv2.putText(img, f'Hue Min: {hue_min}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(img, f'Sat Min: {sat_min}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(img, f'Val Min: {val_min}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(img, f'Hue Max: {hue_max}', (310, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(img, f'Sat Max: {sat_max}', (310, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(img, f'Val Max: {val_max}', (310, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Mostrar la imagen
    cv2.imshow('HSV Selector', img)

    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cerrar todas las ventanas
cv2.destroyAllWindows()

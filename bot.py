import cv2
import pyautogui


def captura_pantalla(nombre_archivo):
    captura = pyautogui.screenshot()
    captura.save(nombre_archivo)
    return nombre_archivo

def seleccionar_roi(imagen):
    img = cv2.imread(imagen)
    roi = cv2.selectROI("Selecciona la ROI", img)
    cv2.destroyAllWindows()
    return roi
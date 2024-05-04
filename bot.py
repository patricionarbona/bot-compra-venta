import cv2
import pyautogui


def captura_pantalla(nombre_archivo):
    captura = pyautogui.screenshot()
    captura.save(nombre_archivo)

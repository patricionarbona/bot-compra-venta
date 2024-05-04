import cv2
import pyautogui
import time


def captura_pantalla(nombre_archivo):
    captura = pyautogui.screenshot()
    captura.save(nombre_archivo)
    return nombre_archivo

def seleccionar_roi(imagen):
    img = cv2.imread(imagen)
    roi = cv2.selectROI("Selecciona la ROI", img)
    cv2.destroyAllWindows()
    return roi

def detectar_elemento(imagen, confianza=0.9):
    return pyautogui.locateOnScreen(imagen, confidence=confianza)

def centro_elemento(region_elemento):
    return pyautogui.center(region_elemento)
 
def comprar():
    boton_compra = "botonCompra.png"
    region_boton_compra = detectar_elemento(boton_compra, 0.8)
    botonx, botony = centro_elemento(region_boton_compra)
    pyautogui.click(botonx, botony)

def detener_compra():
    boton_detener_compra = "botonDetenerCompra.png"
    region_boton_detener_compra = detectar_elemento(boton_detener_compra, 0.8)
    botonx, botony = centro_elemento(region_boton_detener_compra)
    pyautogui.click(botonx, botony)

def vender():
    boton_venta = "botonVenta.png"
    region_boton_venta = detectar_elemento(boton_venta, 0.8)
    botonx, botony = centro_elemento(region_boton_venta)
    pyautogui.click(botonx, botony)

def detener_venta():
    boton_detener_venta = "botonDetenerVenta.png"
    region_boton_detener_venta = detectar_elemento(boton_detener_venta, 0.8)
    botonx, botony = centro_elemento(region_boton_detener_venta)
    pyautogui.click(botonx, botony)

def mover_slider(region=[0,0]):
    slider = "circuloSlider.png"
    region_slider = detectar_elemento(slider, 0.8)
    botonx, botony = centro_elemento(region_slider)
    pyautogui.moveTo(botonx, botony, duration=0.1)
    pyautogui.mouseDown()
    pyautogui.move(1000,0)
    pyautogui.mouseUp()
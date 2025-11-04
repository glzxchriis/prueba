import RPi.GPIO as GPIO
import time

# --- Configuración GPIO ---
GPIO.setmode(GPIO.BCM)

# Pines conectados a los segmentos del display (a, b, c, d, e, f, g)
segmentos = [5, 6, 7, 8, 9, 10, 11]

# Configurar pines como salida
for pin in segmentos:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

# --- Números del 0 al 9 ---
# 1 = encendido, 0 = apagado
numeros = {
    0: [1,1,1,1,1,1,0],
    1: [0,1,1,0,0,0,0],
    2: [1,1,0,1,1,0,1],
    3: [1,1,1,1,0,0,1],
    4: [0,1,1,0,0,1,1],
    5: [1,0,1,1,0,1,1],
    6: [1,0,1,1,1,1,1],
    7: [1,1,1,0,0,0,0],
    8: [1,1,1,1,1,1,1],
    9: [1,1,1,1,0,1,1]
}

# --- Función para mostrar número ---
def mostrar_numero(num):
    for i, pin in enumerate(segmentos):
        GPIO.output(pin, numeros[num][i])

# --- Programa principal ---
try:
    while True:
        for n in range(10):  # del 0 al 9
            mostrar_numero(n)
            print(f"Mostrando: {n}")
            time.sleep(1)
        print("Reiniciando secuencia...\n")
except KeyboardInterrupt:
    print("\nPrueba interrumpida por el usuario.")
finally:
    GPIO.cleanup()

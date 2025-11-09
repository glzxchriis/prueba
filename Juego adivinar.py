import RPi.GPIO as GPIO
import time
import random

# --- Configuración GPIO ---
GPIO.setmode(GPIO.BCM)

# Pines del display (a, b, c, d, e, f, g)
segmentos = [5, 6, 7, 8, 9, 10, 11]
for pin in segmentos:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

# LEDs
LED_VERDE = 22
LED_ROJO = 23
GPIO.setup(LED_VERDE, GPIO.OUT)
GPIO.setup(LED_ROJO, GPIO.OUT)

# Botones
BTN_INC = 17
BTN_OK = 27
GPIO.setup(BTN_INC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_OK, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Números del 0–9
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

def mostrar_numero(num):
    for i, pin in enumerate(segmentos):
        GPIO.output(pin, numeros[num][i])

# --- Programa principal ---
try:
    numero_secreto = random.randint(0, 9)
    print(f"🔢 Número secreto (oculto): {numero_secreto}")

    numero_actual = 0
    mostrar_numero(numero_actual)

    while True:
        if GPIO.input(BTN_INC) == GPIO.LOW:
            numero_actual = (numero_actual + 1) % 10
            mostrar_numero(numero_actual)
            time.sleep(0.3)  # anti-rebote

        if GPIO.input(BTN_OK) == GPIO.LOW:
            if numero_actual == numero_secreto:
                GPIO.output(LED_VERDE, 1)
                GPIO.output(LED_ROJO, 0)
                print("✅ ¡Correcto!")
            else:
                GPIO.output(LED_VERDE, 0)
                GPIO.output(LED_ROJO, 1)
                print(f"❌ Incorrecto. Era {numero_secreto}")
            time.sleep(2)
            GPIO.output(LED_VERDE, 0)
            GPIO.output(LED_ROJO, 0)
            numero_secreto = random.randint(0, 9)
            print(f"Nuevo número secreto generado.")
            numero_actual = 0
            mostrar_numero(numero_actual)

except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario.")

finally:
    GPIO.cleanup()


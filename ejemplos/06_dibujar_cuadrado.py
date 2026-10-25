# Pluma: dibujar un cuadrado (herramienta: pluma)
import robot

# Dibuja un cuadrado de 100 mm con el portabolígrafos
MESA = -50    # Z de la mesa con la pluma (valor aproximado: mide el de tu robot)
ALTO = -30    # Z para desplazarse sin dibujar

robot.moveG0(-110, 240, ALTO)   # encima de la primera esquina
robot.moveG0(-110, 240, MESA)   # bajar la pluma: empieza el trazo

robot.moveG1(-10, 240, MESA)    # lado 1 (G1 = línea recta)
robot.moveG1(-10, 340, MESA)    # lado 2
robot.moveG1(-110, 340, MESA)   # lado 3
robot.moveG1(-110, 240, MESA)   # lado 4: cierra el cuadrado

robot.moveG0(-110, 240, ALTO)   # levantar la pluma
robot.goHome()
print("¡Cuadrado dibujado!")

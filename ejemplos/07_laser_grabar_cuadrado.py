# Láser: grabar un cuadrado (herramienta: láser)
import robot

# Graba un cuadrado de 60 mm con el módulo láser
# OJO: en el robot real el láser quema de verdad. Mismo cuidado que en el
# modo láser del programa Huenit: nunca lo apuntes a nadie y vigila la potencia.
MESA = -45    # Z de la mesa con el láser (valor aproximado: mide el de tu robot)
ALTO = -25    # Z para desplazarse sin grabar

robot.moveG0(-100, 260, ALTO)   # encima de la primera esquina
robot.laserOn()                 # encender el láser

robot.moveG0(-100, 260, MESA)   # bajar a la altura focal: empieza a grabar
robot.moveG1(-40, 260, MESA)
robot.moveG1(-40, 320, MESA)
robot.moveG1(-100, 320, MESA)
robot.moveG1(-100, 260, MESA)

robot.moveG0(-100, 260, ALTO)   # subir
robot.laserOff()                # apagar el láser
robot.goHome()
print("¡Cuadrado grabado!")

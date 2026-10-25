# Simulador Huenit

Simulador 3D del brazo robótico Huenit para aprender Python. Los alumnos escriben
código con la librería `robot` (la misma del programa Huenit), lo prueban en el
simulador sin el robot y después lo ejecutan igual en el brazo real.

## Contenido

| Archivo | Para qué sirve |
|---|---|
| `index.html` | El simulador completo. Ábrelo con doble clic en Chrome o Edge. |
| `ejemplos/` | Los siete ejemplos del simulador como archivos `.py`. |
| `referencia/robot.py` | La librería oficial que trae el programa Huenit (sacada de `resources/robot_blocks`). Solo como referencia: muestra qué comandos envía cada función. |

## Usarlo

1. Abre `index.html` en Chrome o Edge. Necesita internet la primera vez, porque
   carga el intérprete de Python (Skulpt), el motor 3D (Three.js) y el editor
   (CodeMirror) desde CDN.
2. Escribe el código, elige la herramienta (ventosa, pinza, pluma o láser) y pulsa **Ejecutar**
   (o Ctrl+Enter).
3. El código se guarda solo en el navegador de cada alumno.

## Controles manuales del brazo

Además de ejecutar programas de Python, la página permite manejar el brazo a mano:

- **Parada de emergencia** (botón rojo, arriba a la derecha): aborta el
  movimiento del brazo (comando `M410`, el mismo que usa el programa Huenit)
  y detiene el programa en marcha.
- **Mover** (panel bajo la escena 3D): cruceta para X/Y, botones Z+/Z− y
  botón de casa. También con el teclado: las flechas mueven en X/Y,
  Re Pág/Av Pág en Z e Inicio vuelve a casa. El selector **Paso** fija los
  milímetros de cada movimiento (1, 5, 10 o 25 mm) y el deslizador
  **Velocidad** lo hace más lento (en el robot conectado se intenta enviar
  como `M220`, si el firmware lo acepta).
- **Consola G-code** (pestaña «Comandos al robot»): escribe un comando y pulsa
  Enter para probarlo en la simulación y, si está conectado, en el brazo.
  Entiende `help` (lista de comandos) y `clear` (limpiar), y guarda el
  historial con las flechas ↑ ↓.
- **Teach & Play** (pestaña «Teach & Play»): enseña al brazo una secuencia
  paso a paso. Mueve el brazo con el panel «Mover» (o con un programa), pulsa
  **Añadir paso** para guardar la posición y ajusta en cada paso el modo de
  movimiento (arco/lineal/sin mover), la acción de la herramienta (ventosa o
  pinza) y una pausa T en segundos — el mismo modelo de macro del programa
  Huenit. **Reproducir** ejecuta la macro en la simulación y en el robot
  conectado a la vez (se puede parar con Detener o la parada de emergencia), y
  **Copiar G-code** exporta la macro como comandos listos para la consola del
  programa Huenit. La macro se guarda sola en el navegador.
- **Pluma** (selector de herramienta «Portabolígrafos»): cuando la punta toca
  la mesa el brazo dibuja en ella, con cualquier movimiento (programa,
  «Mover», consola o macro). El ejemplo «Pluma: dibujar un cuadrado» traza un
  cuadrado de 100 mm con `moveG1`. Su Z de mesa (≈ −50) es aproximada: mide
  la de tu robot, porque en el programa Huenit la profundidad de dibujo es
  configurable. **Reiniciar escena** borra también el dibujo.
- **Láser** (selector «Láser (grabado)»): `robot.laserOn()` / `robot.laserOff()`
  encienden y apagan el haz (comandos `M3` / `M5`); al pasar por la altura
  focal deja la marca de grabado en la mesa. El ejemplo «Láser: grabar un
  cuadrado» lo muestra. **El láser real quema: solo con el robot conectado y
  supervisado**, con el mismo cuidado que el modo láser del programa Huenit.
  Su Z de mesa (≈ −45) es aproximada: mide la de tu robot.

## Pasar al robot real

**Opción A (recomendada): programa Huenit**

1. Conecta el brazo a la PC con el cable USB-C (puerto de PC).
2. En el programa Huenit ve a **Código** y crea un proyecto de **Python**.
3. Pega el código, conecta el brazo y pulsa **Live**.

**Opción B: desde el navegador (Web Serial)**

El botón **Conectar robot** del simulador habla con el brazo por USB y ejecuta el
mismo programa en el robot y en la simulación a la vez. Funciona en Chrome o Edge
de escritorio cuando la página se abre desde un servidor `https://` o desde
`localhost`. Algunos navegadores lo bloquean si abres el archivo con doble clic.
Para probarlo en local:

```
cd simulador-huenit
python -m http.server 8000
```

Luego abre http://localhost:8000 en Chrome. Cierra antes el programa Huenit,
porque solo una aplicación puede usar el puerto USB a la vez.

Para que los alumnos tengan un enlace fijo y gratuito, sube la carpeta a un
repositorio de GitHub y activa **GitHub Pages**.

## Coordenadas

- Origen en el centro de la base. Mirando el brazo desde atrás: X hacia los
  lados, Y hacia adelante y Z hacia arriba. Todo en milímetros.
- Posición de casa: (0, 180, 0).
- Mesa: Z ≈ −60 con la ventosa y Z ≈ −20 con la pinza (valores de los ejemplos
  oficiales de Huenit). Mide la de tu robot y ajusta si hace falta.
- El alcance usa la misma fórmula que `checkXYZ()` de la librería oficial.

## Limitaciones conocidas

- El dibujo del brazo es aproximado: Huenit no publica las medidas de los
  eslabones. Las coordenadas y el alcance sí son los oficiales.
- `moveAngle()`, `move_conveyor()` y los comandos G-code que no sean G0 o G1 se
  envían al robot real, pero la simulación no los dibuja.
- `getDeg()` es aproximado en la simulación.
- El simulador usa Skulpt, que cubre casi todo el Python que se enseña en clase
  (variables, bucles, funciones, listas, f-strings), pero no todas las librerías.
- No se ha probado todavía con el robot físico. Haz los primeros movimientos
  lentos y lejos de objetos.

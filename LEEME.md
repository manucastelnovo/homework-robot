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
| `README.md` | Esta documentación en inglés. |

## Usarlo

1. Abre `index.html` en Chrome o Edge. Necesita internet la primera vez, porque
   carga el intérprete de Python (Skulpt), el motor 3D (Three.js) y el editor
   (CodeMirror) desde CDN.
2. Escribe el código y pulsa **Ejecutar** (o Ctrl+Enter). La herramienta
   (ventosa, pinza, pluma o láser) se elige en la barra lateral.
3. El código se guarda solo en el navegador de cada alumno.

## La interfaz

La página se divide en una barra lateral, una sección principal y, a la
derecha, la escena 3D con el panel de movimiento manual, que se ve en todas
las secciones excepto «Funciones» y «Robot». La barra lateral lleva la
navegación, el selector de herramienta, un botón de tema claro/oscuro y el
estado de la conexión. Se salta de sección con Ctrl+1…9 (Cmd+1…9 en Mac), en
este orden:

1. **Programar** — editor Python con los ejemplos y los botones Ejecutar / Detener / Reiniciar.
2. **Consola** — lo que imprime el programa, con botón Limpiar.
3. **Comandos al robot** — consola G-code interactiva.
4. **Teach & Play** — grabador de macros.
5. **Dibujar** — lienzo para dibujar a mano alzada y que el brazo reproduzca el trazo.
6. **Cámara** — vista en primera persona del brazo con detección de cubos por color.
7. **Escena** — posición de los objetos en la mesa.
8. **Funciones** — referencia de la librería `robot`.
9. **Robot** — ejecutar el mismo código en el brazo real y conexión por USB.

Al ejecutar un programa (o si salta un error) la vista cambia sola a
**Consola** para que se vea lo que pasa.

## Controles manuales del brazo

Además de ejecutar programas de Python, la página permite manejar el brazo a mano:

- **Parada de emergencia** (botón rojo, arriba a la derecha): aborta el
  movimiento del brazo (comando `M410`, el mismo que usa el programa Huenit)
  y detiene el programa en marcha.
- **Mover** (panel derecho, visible en todas las secciones salvo «Funciones» y
  «Robot»): cruceta para X/Y, botones Z+/Z− y
  botón de casa. También con el teclado: las flechas mueven en X/Y,
  Re Pág/Av Pág en Z e Inicio vuelve a casa. El selector **Paso** fija los
  milímetros de cada movimiento (1, 5, 10 o 25 mm) y el deslizador
  **Vel. flechas** ajusta la velocidad de esos desplazamientos. El deslizador
  **Velocidad** (parte superior del panel) fija la velocidad general del brazo
  en todos los movimientos (programas, dibujos, macros y desplazamientos); en
  el robot conectado se aplica en vivo como `M220`, si el firmware lo acepta.
- **Consola G-code** (sección «Comandos al robot»): escribe un comando y pulsa
  Enter para probarlo en la simulación y, si está conectado, en el brazo.
  Entiende `help` (lista de comandos) y `clear` (limpiar), y guarda el
  historial con las flechas ↑ ↓.
- **Teach & Play** (sección «Teach & Play»): enseña al brazo una secuencia
  paso a paso. Mueve el brazo con el panel «Mover» de la derecha (o con un programa), pulsa
  **Añadir paso** para guardar la posición y ajusta en cada paso el modo de
  movimiento (arco/lineal/sin mover), la acción de la herramienta (ventosa o
  pinza) y una pausa T en segundos — el mismo modelo de macro del programa
  Huenit. **Reproducir** ejecuta la macro en la simulación y en el robot
  conectado a la vez (se puede parar con Detener o la parada de emergencia), y
  **Copiar G-code** exporta la macro como comandos listos para la consola del
  programa Huenit. La macro se guarda sola en el navegador.
- **Dibujar** (sección «Dibujar»): dibuja con el mouse o el dedo en el lienzo
  y pulsa **Dibujar con el brazo**: el brazo reproduce cada trazo con la
  herramienta Pluma (se elige sola), bajando la pluma al empezar cada trazo y
  levantándola entre trazos. Con el robot conectado, dibuja de verdad.
  **Copiar Python** y **Copiar G-code** exportan el dibujo como programa o
  comandos listos para el programa Huenit. El lienzo se guarda solo en el
  navegador.
- **Cámara** (herramienta «Cámara (visión)» y sección «Cámara»): la sección
  muestra lo que ve la cámara del brazo en primera persona, con cajas de
  detección sobre los cubos visibles; el selector de color localiza un cubo y
  da sus coordenadas de mesa, **Foto** congela el frame y **Descargar PNG**
  guarda la imagen. En los programas, `robot.cameraObjects()` lista los cubos
  vistos y `robot.findColor("rojo")` da su posición (funciones del simulador:
  la cámara real se programa con `ai.py` dentro del módulo y no usa G-code).
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

El botón **Conectar robot** (sección «Robot») del simulador habla con el brazo por USB y ejecuta el
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

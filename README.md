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

1. Open `index.html` in Chrome or Edge. It needs internet the first time,
   because it loads the Python interpreter (Skulpt), the 3D engine (Three.js)
   and the editor (CodeMirror) from a CDN.
2. Write your code and press **Ejecutar** (Run, or Ctrl+Enter). The tool
   (suction cup, gripper, pen or laser) is selected in the sidebar.
3. Each student's code is saved automatically in their own browser.

## The interface

The page is divided into a sidebar, a main section and, on the right, the 3D
scene with the manual movement panel, which stays visible in every section
except «Funciones» (Functions) and «Robot». The sidebar holds the navigation,
the tool selector, a light/dark theme toggle and the connection status. You
jump between sections with Ctrl+1…7 (Cmd+1…7 on Mac), in this order:

1. **Programar** (Program) — Python editor with the examples and the Run / Stop / Reset buttons.
2. **Consola** (Console) — what the program prints, with a Clear button.
3. **Comandos al robot** (Commands to the robot) — interactive G-code console.
4. **Teach & Play** — macro recorder.
5. **Escena** (Scene) — position of the objects on the table.
6. **Funciones** (Functions) — `robot` library reference.
7. **Robot** — running the same code on the real arm and USB connection.

When you run a program (or an error occurs) the view switches automatically
to **Consola** so you can see what happens.

## Manual arm controls

Besides running Python programs, the page lets you drive the arm by hand:

- **Emergency stop** (red button, top right): aborts the arm's movement
  (command `M410`, the same one the Huenit program uses) and stops the
  running program.
- **Mover** (panel on the right, visible in every section except «Funciones»
  and «Robot»): X/Y crosspad, Z+/Z− buttons
  and a home button. Also from the keyboard: arrow keys move in X/Y,
  Page Down/Page Up in Z, and Home returns to the home position. The
  **Paso** (Step) selector sets the millimeters per move (1, 5, 10 or 25 mm)
  and the **Velocidad** (Speed) slider slows it down (with a connected robot
  it tries to send it as `M220`, if the firmware accepts it).
- **G-code console** (section «Comandos al robot»): type a command and press
  Enter to try it in the simulation and, if connected, on the arm. It
  understands `help` (command list) and `clear`, and keeps history with the
  ↑ ↓ arrow keys.
- **Teach & Play** (section «Teach & Play»): teach the arm a sequence step by
  step. Move the arm with the «Mover» panel on the right (or with a program), press
  **Añadir paso** (Add step) to save the position, and adjust each step's
  movement mode (arc/linear/no move), tool action (suction cup or gripper)
  and a T pause in seconds — the same macro model as the Huenit program.
  **Reproducir** (Play) runs the macro in the simulation and on the connected
  robot at the same time (it can be stopped with Detener or the emergency
  stop), and **Copiar G-code** exports the macro as commands ready for the
  Huenit program's console. The macro is saved automatically in the browser.
- **Pen** (tool selector «Portabolígrafos»): when the tip touches the table
  the arm draws on it, with any movement (program, «Mover», console or
  macro). The example «Pluma: dibujar un cuadrado» (Pen: draw a square)
  traces a 100 mm square with `moveG1`. Its table Z (≈ −50) is approximate:
  measure your robot's, because drawing depth is configurable in the Huenit
  program. **Reiniciar escena** (Reset scene) also erases the drawing.
- **Laser** (selector «Láser (grabado)»): `robot.laserOn()` / `robot.laserOff()`
  turn the beam on and off (commands `M3` / `M5`); passing through the focal
  height leaves an engraving mark on the table. The example «Láser: grabar un
  cuadrado» (Laser: engrave a square) shows it. **The real laser burns: use it
  only with the robot connected and supervised**, with the same care as the
  Huenit program's laser mode. Its table Z (≈ −45) is approximate: measure
  your robot's.

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

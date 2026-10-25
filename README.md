# Huenit Simulator

3D simulator of the Huenit robotic arm for learning Python. Students write
code with the `robot` library (the same one bundled with the Huenit program),
test it in the simulator without the robot, and then run the exact same code
on the real arm.

Spanish documentation: [LEEME.md](LEEME.md).

## Contents

| File | What it's for |
|---|---|
| `index.html` | The complete simulator. Open it with a double click in Chrome or Edge. |
| `ejemplos/` | The simulator's seven examples as `.py` files. |
| `referencia/robot.py` | The official library bundled with the Huenit program (taken from `resources/robot_blocks`). Reference only: shows which commands each function sends. |

## Using it

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
jump between sections with Ctrl+1…8 (Cmd+1…8 on Mac), in this order:

1. **Programar** (Program) — Python editor with the examples and the Run / Stop / Reset buttons.
2. **Consola** (Console) — what the program prints, with a Clear button.
3. **Comandos al robot** (Commands to the robot) — interactive G-code console.
4. **Teach & Play** — macro recorder.
5. **Dibujar** (Draw) — canvas for freehand drawing that the arm reproduces.
6. **Escena** (Scene) — position of the objects on the table.
7. **Funciones** (Functions) — `robot` library reference.
8. **Robot** — running the same code on the real arm and USB connection.

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
- **Dibujar** (Draw, section «Dibujar»): draw with the mouse or a finger on
  the canvas and press **Dibujar con el brazo** (Draw with the arm): the arm
  reproduces each stroke with the pen tool (selected automatically), lowering
  the pen at the start of each stroke and lifting it between strokes. With a
  connected robot, it draws for real. **Copiar Python** and **Copiar G-code**
  export the drawing as a program or as commands ready for the Huenit
  program. The canvas is saved automatically in the browser.
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

## Moving to the real robot

**Option A (recommended): Huenit program**

1. Connect the arm to the PC with the USB-C cable (PC port).
2. In the Huenit program go to **Código** (Code) and create a **Python** project.
3. Paste the code, connect the arm and press **Live**.

**Option B: from the browser (Web Serial)**

The **Conectar robot** (Connect robot) button (section «Robot») talks to the
arm over USB and runs the same program on the robot and in the simulation at
the same time. It works in desktop Chrome or Edge when the page is served
from `https://` or from `localhost`. Some browsers block it if you open the
file with a double click. To try it locally:

```
cd simulador-huenit
python -m http.server 8000
```

Then open http://localhost:8000 in Chrome. Close the Huenit program first,
because only one application can use the USB port at a time.

To give students a fixed, free link, upload the folder to a GitHub repository
and enable **GitHub Pages**.

## Coordinates

- Origin at the center of the base. Looking at the arm from behind: X to the
  sides, Y forward and Z up. Everything in millimeters.
- Home position: (0, 180, 0).
- Table: Z ≈ −60 with the suction cup and Z ≈ −20 with the gripper (values
  from Huenit's official examples). Measure your robot's and adjust if needed.
- Reachability uses the same formula as `checkXYZ()` from the official library.

## Known limitations

- The arm's drawing is approximate: Huenit doesn't publish the link
  measurements. Coordinates and reachability are the official ones.
- `moveAngle()`, `move_conveyor()` and G-code commands other than G0 or G1 are
  sent to the real robot, but the simulation doesn't animate them.
- `getDeg()` is approximate in the simulation.
- The simulator uses Skulpt, which covers almost all the Python taught in
  class (variables, loops, functions, lists, f-strings), but not all libraries.
- It hasn't been tested with the physical robot yet. Make the first movements
  slow and away from objects.

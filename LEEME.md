# Simulador Huenit

Simulador 3D del brazo robótico Huenit para aprender Python. Los alumnos escriben
código con la librería `robot` (la misma del programa Huenit), lo prueban en el
simulador sin el robot y después lo ejecutan igual en el brazo real.

## Contenido

| Archivo | Para qué sirve |
|---|---|
| `index.html` | El simulador completo. Ábrelo con doble clic en Chrome o Edge. |
| `ejemplos/` | Los cinco ejemplos del simulador como archivos `.py`. |
| `referencia/robot.py` | La librería oficial que trae el programa Huenit (sacada de `resources/robot_blocks`). Solo como referencia: muestra qué comandos envía cada función. |

## Usarlo

1. Abre `index.html` en Chrome o Edge. Necesita internet la primera vez, porque
   carga el intérprete de Python (Skulpt), el motor 3D (Three.js) y el editor
   (CodeMirror) desde CDN.
2. Escribe el código, elige la herramienta (ventosa o pinza) y pulsa **Ejecutar**
   (o Ctrl+Enter).
3. El código se guarda solo en el navegador de cada alumno.

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

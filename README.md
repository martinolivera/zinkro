# Zinkro: Calendario de 13 Meses / 13-Month Calendar

## Español

Zinkro es un proyecto open source que propone un calendario alternativo: 13 meses de 28 días cada uno, más uno o dos Días Fuera del Tiempo, alineado con el equinoccio de marzo. El objetivo es reconectar el tiempo humano con los ritmos naturales y cósmicos, y facilitar la planificación anual.

### Estructura del Proyecto

- `views/visual_grid.html`: Grilla visual interactiva del calendario (HTML/JS/CSS).
- `views/contexto.html` y `views/context.html`: Explicación y propuesta (español/inglés).
- `zinkro.py`: Lógica principal y utilidades de conversión de fechas.
- `convert.py`: Script CLI para convertir fechas entre gregoriano y Zinkro.
- `test_zinkro.py`: Pruebas unitarias.
- `.github/workflows/gh-pages.yml`: Deploy automático a GitHub Pages desde la carpeta views/.

### Cómo usar

- Visualiza el calendario: abre `views/visual_grid.html` en tu navegador o visita la URL de GitHub Pages tras el deploy.
- Convierte fechas desde la terminal:
  ```bash
  python3 convert.py g2z 2025-07-15
  python3 convert.py z2g 0 7 15
  ```
- Lee la propuesta completa en `views/contexto.html` o en inglés en `views/context.html`.

### Deploy

El deploy a GitHub Pages es automático desde la rama main. El contenido de `views/` se publica en la rama gh-pages.

---

## English

Zinkro is an open source project proposing an alternative calendar: 13 months of 28 days each, plus one or two Days Out of Time, aligned with the March equinox. The goal is to reconnect human time with natural and cosmic rhythms, and to simplify annual planning.

### Project Structure

- `views/visual_grid.html`: Interactive visual grid of the calendar (HTML/JS/CSS).
- `views/contexto.html` and `views/context.html`: Explanatory and proposal pages (Spanish/English).
- `zinkro.py`: Main logic and date conversion utilities.
- `convert.py`: CLI script to convert dates between Gregorian and Zinkro.
- `test_zinkro.py`: Unit tests.
- `.github/workflows/gh-pages.yml`: Automatic deploy to GitHub Pages from the views/ folder.

### How to use

- View the calendar: open `views/visual_grid.html` in your browser or visit the GitHub Pages URL after deploy.
- Convert dates from the terminal:
  ```bash
  python3 convert.py g2z 2025-07-15
  python3 convert.py z2g 0 7 15
  ```
- Read the full proposal in `views/context.html` (English) or `views/contexto.html` (Spanish).

### Deploy

Deploy to GitHub Pages is automatic from the main branch. The contents of `views/` are published to the gh-pages branch.

---

¿Listo para repensar el tiempo?

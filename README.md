# Thesis Project

I decided to create this repository to document the full development of my
undergraduate thesis, including code, data, results, and manuscript written in
Typst using the `cmarker` package. The main purpose of this is to improve my skills
in Git and Typst, and also to provide a kind of template for anyone interested in
doing something similar.

My thesis is written in Spanish, but the code and all other material are in English.
At the end of the project, I will translate the manuscript into English within this
same repository.

- **Original title (in Spanish)**: _Análisis Numérico-Estocástico del Impacto de la
  Variabilidad Espacial del Suelo de Cimentación en la Estabilidad Física y la
  Respuesta Sísmica de un Depósito de Relaves_
- **Authors**: Francesco F. (main researcher), Franklin O. & Denys P (mentors/advisors).
- **University**: National University of Engineering (Lima, Perú)

This research project was sponsored by the Civil Engineering Faculty Research Center
of the same university (IIFIC-UNI), and the authors deeply acknowledge its support.

## Structure

- `src/thesis/` — Thesis chapters in Typst.
- `src/thesis/main.typ` — Main file to compile using Typst.
- `src/code/` — Source code employed for analysis and simulations.
- `data/` — Input data, mainly laboratory and in-situ tests.
- `results/` — Figures and tables.
- `references.bib` — Citations in BibTeX.

## Build

```bash
make
```
Stochastic–Numerical Analysis of the Impact of Spatial Variability in Foundation
Soils on the Physical Stability and Seismic Response of a Tailings Storage Facility
© 2025 by Francesco Franco is licensed under CC BY-NC-SA 4.0. To view a copy of this
license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/

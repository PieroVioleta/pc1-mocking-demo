# PC 1 — Curso de Calidad de Software
## Mockeando un servicio externo en FastAPI

Este proyecto es una **demo educativa** que muestra cómo **mockear un servicio externo** en una API hecha con [FastAPI](https://fastapi.tiangolo.com/).
La idea principal es desacoplar el acceso a un proveedor de tasas de cambio usando un **puerto (interfaz)** y adaptadores intercambiables (ej. `FakeRatesAdapter`), lo que facilita:

- **Pruebas unitarias y de integración** sin depender de servicios externos.
- **Ejecución estable en demo/clases**, incluso si el proveedor real no está disponible.
- **Inyección de dependencias** para cambiar fácilmente entre adaptadores reales y mocks.

---

## Integrantes
- Piero Alexis Violeta Estrella — 20184065H
- Andrés Sebastián La Torre Vasquez — 20212100C
- Maxwel Paredes Lopez — 20191179E
- Franklin Espinoza Pari — 20210135D

---

## Requisitos
- Python **3.10–3.12**
- [Poetry](https://python-poetry.org/) instalado

---

## Instalación
Clonar el repositorio y luego:

```bash
poetry install
```

## Correr el proyecto

```bash
make run
```

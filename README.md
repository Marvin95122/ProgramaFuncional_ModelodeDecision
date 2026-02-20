# Proyecto de Ingeniería en Sistemas Computacionales

**Materia:** Sistemas de Soporte a la Decisión  
**Institución:** Instituto Tecnológico de Oaxaca  

## Colaboradores
* **Espinoza de la Rosa Uriel** - *Desarrollo de Lógica y Documentación*
* **Compañero 1** - *Interfaz de Usuario y Captura Dinámica*
* **Compañero 2** - *Interpretación de Resultados y Salida*
* **Espinoza de la Rosa Uriel** - *Desarrollo de Lógica y Documentación*

---

## Descripción del Proyecto
Este software es un Sistema de Soporte a la Decisión (DSS) diseñado para resolver problemas de optimización de producción. Basado en el modelo matemático propuesto por Efraim Turban en su capítulo sobre modelado y análisis, este sistema utiliza programación lineal para encontrar la combinación óptima de productos que maximiza la utilidad de una empresa.

El "cerebro" del sistema utiliza el algoritmo Simplex (vía la librería PuLP) para procesar variables incontrolables (presupuesto, mano de obra, demanda) y entregar una recomendación clara a nivel directivo.

---

## Tecnologías Utilizadas
* **Lenguaje:** Python 3.10+
* **Librería de Optimización:** PuLP
* **Entorno:** Multiplataforma (Windows/Linux/macOS)

---

## Instalación y Ejecución

**1- Clonar el repositorio:**
```bash
    git clone https://github.com/Marvin95122/ProgramaFuncional_ModelodeDecision.git
    cd ProgramaFuncional_ModelodeDecision
```
**2- Instalar dependencias:**
Este proyecto requiere la librería pulp. Puedes instalarla usando pip en tu terminal:
```bash
    pip install pulp
```
**3- Ejecutar el programa:**
```bash
    python main.py
```
---

## Guía de Uso e Interfaz
Al ejecutar el programa, el DSS te guiará por tres pasos críticos:

1. **Configuración de Rentabilidad:** Define cuánto gana la empresa por cada unidad de producto (CC-7 y CC-8).
2. **Restricciones de Recursos:** Ingresa los límites de días de labor y el presupuesto financiero total.
3. **Compromisos de Mercado:** Establece las cuotas mínimas que marketing exige producir.

### Ejemplo de Prueba:
Para validar el correcto funcionamiento del algoritmo, puedes ingresar los siguientes datos:

| Parámetro | Valor Sugerido |
| :--- | :--- |
| Utilidad CC-7 | 8000 |
| Utilidad CC-8 | 12000 |
| Límite Laboral | 250000 |
| Presupuesto Total | 10000000 |
| Min. CC-7 | 100 |
| Min. CC-8 | 200 |

---

## Lógica del Modelo
El sistema traduce el problema de negocio a una función objetivo matemática:

Z = c1(x1) + c2(x2)

**Sujeto a las siguientes restricciones:**
* a11(x1) + a12(x2) <= Labor Disponible
* a21(x1) + a22(x2) <= Presupuesto Disponible
* x1 >= Mínimo CC-7
* x2 >= Mínimo CC-8


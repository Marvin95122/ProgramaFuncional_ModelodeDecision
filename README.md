# Proyecto de Ingeniería en Sistemas Computacionales

**Materia:** Sistemas de Soporte a la Decisión  
**Institución:** Instituto Tecnológico de Oaxaca  

## Colaboradores
* **Cruz Sanchez Jhoan Marvin** - *Desarrollo de Lógica*
* **Jose Sebastian Jafet** - *Interfaz de Usuario y Captura Dinámica*
* **Nimsi** - *Interpretación de Resultados y Salida*
* **Espinoza de la Rosa Uriel** - *Desarrollo de README y Documentación*

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
Para la formulación del problema, se propone el desarrollo de un modelo estándar de programación lineal (PL). 

La estructura matemática de este modelo se divide en tres componentes principales:

**1. Variables de decisión:**
Representan los elementos del sistema que pueden ser controlados para alcanzar el objetivo deseado.
* $$X_1 = $$ Cantidad de unidades del producto CC-7 a producir.
* $$X_2 = $$ Cantidad de unidades del producto CC-8 a producir.
  
**2. Variable de resultado (Función Objetivo):**
Se define a $Z$ como el beneficio total esperado. El objetivo central del modelo es maximizar dicho beneficio, lo cual está dado por la siguiente función matemática:

**$$Z = 8,000X_1 + 12,000X_2$$**

**3. Variables no controlables (Restricciones del sistema):**
El modelo está sujeto a diversas limitaciones operativas y de mercado que restringen la capacidad de producción:
* Restricción de mano de obra: $300X_1 + 500X_2 \le 200,000$ (expresado en días laborables).
* Restricción de presupuesto: $10,000X_1 + 15,000X_2 \le 8,000,000$ (expresado en dólares).
* Requerimiento mínimo de mercado para CC-7: $X_1 \ge 100$ (expresado en unidades).
* Requerimiento mínimo de mercado para CC-8: $X_2 \ge 200$ (expresado en unidades).
  
**Consideraciones adicionales:**

Es importante destacar que el modelo contempla un cuarto componente de carácter implícito. Como es habitual en los modelos de programación lineal, existen variables intermedias internas que no se declaran de forma explícita en las ecuaciones principales, pero que interactúan en segundo plano con recursos como la mano de obra disponible.

# logic.py
# Responsabilidad: Motor matematico de optimizacion (Linear Programming Solver)

#Se importa las funciones necesarias de la libreria PuLP
#El LpMaximize Indica que queremos maximizar ganancias y no minimizar costos
#LpProblem es el contenedor del modelo matematico
#LpVariable este representa las Variables de Decisión queson X1, X2
from pulp import LpMaximize, LpProblem, LpVariable, value, PULP_CBC_CMD

def calcular_mezcla_optima(d):
    """
    Implementacion del modelo matematico de mezcla de productos de MBI.
    Utiliza el algoritmo Simplex para encontrar la solucion optima entre infinitas posibilidades.
    """
    #1.- DEFINICION DEL PROBLEMA
    #Creamos el objeto del modelo indicando que el objetivo es maximizar (LpMaximize)
    prob = LpProblem("Optimizacion_Ganancias_MBI", LpMaximize)
    #2.- Variables de desicion (X1 y X2)
    #Son las incognitas que el sistema debe resolver ¿Cusnto producir de cada una?
    #lowBound nos asegura que no produzcamos menos de lo que pide marketing.
    # cat=Continuous permite decimales y si se llegaran a requerir enteros, usa Integer).
    x1 = LpVariable("Unidades_CC7", lowBound=d['min_cc7'], cat='Continuous')
    x2 = LpVariable("Unidades_CC8", lowBound=d['min_cc8'], cat='Continuous')

    #3.- Funcion objectivo (Z)
    #Z = (Ganancia_CC7 * X1) + (Ganancia_CC8 * X2)
    #Esta es la meta matematica que el algoritmo intentara hacer lo más grande posible.
    prob += d['utilidad_cc7'] * x1 + d['utilidad_cc8'] * x2, "Ganancia_Total_Z"

    #4.- Restricciones
    #Representan las limitaciones del mundo real.
    #El algoritmo buscara valores para X1 y X2 que no violen estas ecuaciones.

    #Restricciom de mano de obra: (300 días * X1) + (500 días * X2) <= Disponibilidad Total
    prob += 300 * x1 + 500 * x2 <= d['limite_labor'], "Restriccion_Mano_de_Obra"
    
    #Restriccion de presupuesto: ($10,000 * X1) + ($15,000 * X2) <= Presupuesto Total
    prob += 10000 * x1 + 15000 * x2 <= d['limite_presupuesto'], "Restriccion_Presupuesto"

    #5.- solucion (ALGORITMO)
    #Ejecuta el solver interno para encontrar los valores optimos de X1 y X2
    #msg=0 oculta los logs tecnicos de la libreria para limpiar la consola
    prob.solve(PULP_CBC_CMD(msg=0))

    #6.- Retorno de resultados
    #Empaquetamos el estado de la solucion y los valores encontrados
    #para enviarlos al modulo de presentacion (outputs.py de Uriel).
    return {
        "status": prob.status,          #1 = optimo, -1 = Infactible
        "x1": value(x1),                #Cantidad optima de CC-7
        "x2": value(x2),                #Cantidad optima de CC-8
        "ganancia_total": value(prob.objective) #Valor maximo de Z
    }
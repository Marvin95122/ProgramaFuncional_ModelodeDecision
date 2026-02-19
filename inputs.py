# Interfaz de Usuario para la Captura de Datos Dinámicos
def capturar_datos_usuario():
    """Solicitamos al usuario los parámetros del modelo.
    Aquí definimos las variables incontrolables' y 
    los coeficientes que el dss no puede cambiar durante la ejecución,
    pero que especifican el escenario actual."""
    print("=== Configuración Dinámica del DSS (Modelo Turban 4.9) ===")
    datos = {}
    try:
        # coeficientes de la funcion objetivo, ganancia de cada unidad vendida
        print("\n--- PASO 1: Rentabilidad por Producto ---")
        datos['utilidad_cc7'] = float(input("Ingrese la utilidad por cada unidad CC-7 ($): "))
        datos['utilidad_cc8'] = float(input("Ingrese la utilidad por cada unidad CC-8 ($): "))
        
        # restricciones de recursos, límites físicos o financieros de la empresa
        print("\n--- PASO 2: Disponibilidad de Recursos (Restricciones) ---")
        datos['limite_labor'] = float(input("Ingrese el límite total de días de labor disponibles: "))
        datos['limite_presupuesto'] = float(input("Ingrese el presupuesto total de materiales ($): "))
        
        # requerimientos de mercado, restricciones de marketing que obligan a producir un mínimo
        print("\n--- PASO 3: Compromisos de Mercado ---")
        datos['min_cc7'] = float(input("Ingrese la demanda mínima obligatoria de CC-7: "))
        datos['min_cc8'] = float(input("Ingrese la demanda mínima obligatoria de CC-8: "))
        
        return datos
    except ValueError:
        # para evitar que el programa se rompa tenemos una gestion de errores basica
        print("Error: Por favor ingrese solo valores numéricos válidos.")
        return None
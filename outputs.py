# outputs.py
# RESPONSABILIDAD:
# Interpretación de resultados y generación de recomendaciones.



def mostrar_recomendacion_dss(resultados):
    """
    FUNCIÓN PRINCIPAL DE PRESENTACIÓN.

    Recibe un diccionario 'resultados' proveniente del motor lógico,
    el cual contiene:
        - status → estado del modelo (1 = óptimo, -1 = infactible)
        - x1 → unidades óptimas de CC-7
        - x2 → unidades óptimas de CC-8
        - ganancia_total → valor máximo de la función objetivo (Z)

    Su función es transformar números técnicos en información estratégica.
    """

   
    #1. ENCABEZADO DEL REPORTE DSS
    # Se imprime una estructura visual para claridad del usuario.
    
    print("\n" + "="*50)
    print("   SISTEMA DE SOPORTE A LA DECISION (DSS) - REPORTE")
    print("="*50)

    
    # 2. VERIFICACIÓN DEL ESTADO DEL MODELO
    # Status = 1 → Solución Óptima encontrada.
    # Cualquier otro valor → Modelo infactible o sin solución válida.
    
    if resultados['status'] == 1:

        print("ESTADO DEL MODELO: Solucion Optima Encontrada.\n")

        
        # 3. RECOMENDACIÓN ESTRATÉGICA
        # Presenta la combinación óptima de producción.
        
        print("--- RECOMENDACIÓN ESTRATEGICA ---")
        print("Basado en sus restricciones de presupuesto y mano de obra,")
        print("la producción sugerida para maximizar utilidades es:")

        # :,.2f → Formato con separador de miles y 2 decimales
        print(f"  > PRODUCIR: {resultados['x1']:,.2f} unidades del modelo CC-7")
        print(f"  > PRODUCIR: {resultados['x2']:,.2f} unidades del modelo CC-8")

        
        # 4. IMPACTO FINANCIERO
        # Se comunica el valor máximo alcanzado por la función Z.
        
        print("\n--- IMPACTO FINANCIERO ---")
        print(f"  > Utilidad Total Proyectada (Z): ${resultados['ganancia_total']:,.2f}")

        
        # 5. INTERPRETACIÓN GERENCIAL
        # Explicación conceptual del resultado óptimo.
        
        print("\n--- NOTA TECNICA ---")
        print("Esta combinación utiliza sus recursos de la manera más eficiente posible.")
        print("Cualquier cambio en la producción reduciría la ganancia")
        print("o violaría al menos una de las restricciones del modelo.")

    else:
        
        # 6. MANEJO DE ESCENARIOS SIN SOLUCIÓN (INFACTIBILIDAD)
        # Ocurre cuando las restricciones hacen imposible cumplir
        # con los mínimos obligatorios del mercado.
        
        print("ESTADO DEL MODELO: No se encontró solución (Infactible).")

        print("\nANALISIS DE CAUSA:")
        print("Las restricciones impuestas (presupuesto o mano de obra)")
        print("son insuficientes para cumplir con los mínimos de mercado exigidos.")

        print("RECOMENDACION:")
        print("Negocie menores mínimos de venta o incremente el presupuesto disponible.")

    
    print("="*50)
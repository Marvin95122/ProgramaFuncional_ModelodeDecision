import inputs
import logic
import outputs

def ejecutar_dss():
    # Paso 1: Interfaz de usuario
    datos_config = inputs.capturar_datos_usuario()
    
    if datos_config:
        # Paso 2: Ejecución del motor lógico
        res = logic.calcular_mezcla_optima(datos_config)
        
        # Paso 3: Entrega de resultados
        outputs.mostrar_recomendacion_dss(res)

if __name__ == "__main__":
    ejecutar_dss()
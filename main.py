# Costos del viaje
COSTO_VIAJE_ESTACION = 1  # Costo por estación intermedia
COSTO_TRANSFERENCIA = 3   # Costo por cambiar de línea

#-------------------------------------------------------------
# Listas de estaciones por línea
LINEAS_METRO = {
    "Línea 1": [
        "Propatria", "Pérez Bonalde", "Plaza Sucre", "Gato Negro", "Agua Salud", "Caño Amarillo", "Capitolio", "El Silencio",
        "La Hoyada", "Parque Carabobo", "Bellas Artes", "Colegio de Ingenieros", "Plaza Venezuela", "Sabana Grande", "Chacaíto",
        "Chacao", "Altamira", "Miranda", "Los Dos Caminos", "Los Cortijos", "La California", "Palo Verde"
    ],
    "Línea 2": [
        "El Silencio", "Capuchinos", "Maternidad", "Artigas", "La Paz", "La Yaguara", "Carapita",
        "Antímano", "Mamera", "Caricuao", "Ruiz Pineda", "Las Adjuntas", "Zoológico"
    ],
    "Línea 3": [
        "Plaza Venezuela", "Ciudad Universitaria", "Los Símbolos", "La Bandera", "El Valle",
        "Los Jardines", "Coche", "Mercado", "La Rinconada"
    ]
}

# Estaciones de transferencia
# (L1<->L2: El Silencio; L1<->L3: Plaza Venezuela)
ESTACIONES_TRANSFERENCIA = {
    ("Línea 1", "Línea 2"): "El Silencio",
    ("Línea 2", "Línea 1"): "El Silencio",
    ("Línea 1", "Línea 3"): "Plaza Venezuela",
    ("Línea 3", "Línea 1"): "Plaza Venezuela",
    ("Línea 2", "Línea 3"): "El Silencio", 
    ("Línea 3", "Línea 2"): "Plaza Venezuela",
}

#-------------------------------------------------------------
# Funciones de Utilidad

def obtener_datos_estacion(nombre_estacion: str) -> tuple[str | None, str | None]:
    estacion_normalizada = nombre_estacion.strip().title()
    for linea, estaciones in LINEAS_METRO.items():
        if estacion_normalizada in estaciones:
            return linea, estacion_normalizada
    return None, None

def calcular_trayecto(linea: str, inicio: str, destino: str) -> tuple[int, list[tuple[str, str]]]:
    estaciones_linea = LINEAS_METRO[linea]
    try:
        idx_i = estaciones_linea.index(inicio)
        idx_d = estaciones_linea.index(destino)
    except ValueError:
        return 0, []

    # El costo es la cantidad de segmentos (segmento = viaje entre 2 estaciones)
    num_segmentos = abs(idx_d - idx_i)
    costo = num_segmentos * COSTO_VIAJE_ESTACION

    # Determinar el orden de las estaciones para el trayecto
    if idx_i <= idx_d:
        estaciones_recorridas = estaciones_linea[idx_i : idx_d + 1]
    else:
        estaciones_recorridas = estaciones_linea[idx_d : idx_i + 1]
        estaciones_recorridas.reverse()

    # Formato del trayecto: Lista de Estación, Línea
    trayecto_detallado = [(e, linea) for e in estaciones_recorridas]
    
    return costo, trayecto_detallado

# Función Principal

def simular_viaje_metro():
    print("Viaje del Metro de Caracas (L1, L2, L3)")

    # Entrada y Validación de Estación de Inicio
    while True:
        entrada_i = input("¿Cuál es su estación de inicio? ")
        linea_i, estacion_i = obtener_datos_estacion(entrada_i)
        if linea_i:
            print(f"Se inicia en {estacion_i} ({linea_i}).")
            break
        else:
            print(f"Estación '{entrada_i}' no encontrada. Por favor, intente con el nombre correcto (ejemplo: Propatria).")

    # Entrada y Validación de Estación de Destino
    while True:
        entrada_d = input("¿Cuál es su estación de destino? ")
        linea_d, estacion_d = obtener_datos_estacion(entrada_d)
        if linea_d:
            print(f"El destino es {estacion_d} ({linea_d}).")
            break
        else:
            print(f"Estación '{entrada_d}' no encontrada. Por favor, intente con el nombre correcto (ejemplo: Palo Verde).")
            
    print("Calculando Costo y Ruta")

    costo_total = 0
    trayecto_final = []

    # En caso de ser el Mismo Viaje (Inicio = Destino)
    if estacion_i == estacion_d:
        costo_total = 0
        trayecto_final = [(estacion_i, linea_i)]
        print("Usted ya se encuentra en su destino")

    # Viaje en la Misma Línea
    elif linea_i == linea_d:
        costo_total, trayecto_final = calcular_trayecto(linea_i, estacion_i, estacion_d)
        print(f"Viaje directo en la {linea_i}.")

    # Viaje con Transferencia (Líneas Diferentes)
    else:
        # Encontrar la estación de transferencia
        llaves_transferencia = (linea_i, linea_d)
        estacion_transferencia = ESTACIONES_TRANSFERENCIA.get(llaves_transferencia)

        if estacion_transferencia:
            print(f"Se requiere transferencia en {estacion_transferencia}.")
            
            # Tramo 1: Inicio -> Transferencia (en Línea I)
            costo_tramo1, trayecto_tramo1 = calcular_trayecto(linea_i, estacion_i, estacion_transferencia)
            
            # Tramo 2: Transferencia -> Destino (en Línea D)
            costo_tramo2, trayecto_tramo2_completo = calcular_trayecto(linea_d, estacion_transferencia, estacion_d)
            
            # Ajuste de costos y ruta
            costo_transferencia_total = COSTO_TRANSFERENCIA
            costo_total = costo_tramo1 + costo_tramo2 + costo_transferencia_total
            
            # Unir los trayectos. Excluimos la estación de transferencia duplicada del inicio del Tramo 2.
            # El último elemento de trayecto_tramo1 es la estación de transferencia.
            # El primer elemento de trayecto_tramo2_completo es la estación de transferencia.
            trayecto_final = trayecto_tramo1 + trayecto_tramo2_completo[1:] 

    print(f"El costo total del viaje es: {costo_total} unidades.")
    print("La ruta detallada a recorrer es:")
    
    # Imprimir la ruta detallada
    for i, (estacion, linea) in enumerate(trayecto_final):
        if i == 0:
            print(f"INICIO: {estacion} ({linea})")
        elif i == len(trayecto_final) - 1:
            print(f"DESTINO: {estacion} ({linea})")
        else:
            # Verifica si hay cambio de línea para la transferencia
            if i > 0 and trayecto_final[i-1][1] != linea:
                 print(f"TRANSFERENCIA: {estacion} (Cambio a {linea})")
            else:
                 print(f"{estacion} ({linea})")

#-------------------------------------------------------------
# Ejecutar el programa
if __name__ == "__main__":
    simular_viaje_metro()
#-------------------------------------------------------------
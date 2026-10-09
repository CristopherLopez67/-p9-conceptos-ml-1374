# Cristopher Javier NC 1374 

import pandas as pd

# 1. Crear un dataset de ejemplo simular a un CSV
datos4 = {
    'distancia_km': [4.8, 1.0, 3.3, 6.5, 2.2],
    'trafico_nivel': [3, 1, 2, 3, 1],
    'edad_repartidor': [29, 24, 36, 41, 21],
    'tiempo_entrega_min': [45, 8, 28, 60, 15]
}

df = pd.DataFrame(datos4)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))


print("Cristopher Javier Nc 1374")
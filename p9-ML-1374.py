# Cristopher Javier NC 1374 

import pandas as pd

# 1. Crear un dataset de ejemplo simular a un CSV
datos12 = {
    'distancia_km': [3.2, 5.1, 1.5, 4.7, 2.0],
    'trafico_nivel': [3, 2, 1, 3, 2],
    'edad_repartidor': [30, 25, 38, 44, 22],
    'tiempo_entrega_min': [30, 42, 11, 48, 16]
}

df = pd.DataFrame(datos12)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))


print("Cristopher Javier Nc 1374")
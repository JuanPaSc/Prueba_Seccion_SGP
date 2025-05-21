
---

## 🧼 Limpieza y Preparación de Datos

- Se detectaron y corrigieron errores comunes al realizarse las agrupaciones:
  - Valores monetarios concatenados (`$1000$2000`)
  - Valores tipo `"YESYESYES"` convertidos a booleanos
- Se aplicaron funciones personalizadas para:
  - Agregación monetaria (`mean` o `sum`)
  - Conversión de cadenas a numérico

---

## 🏗️ Ingeniería de Features

- Agregación de transacciones por `client_id` y `mcc`
- Agregación de características de tarjetas por cliente
- Fusión de tablas con información de usuario
- Conversión de la variable `mcc` a categórica
- Variables utilizadas: edad, ingresos, límite de crédito, número de tarjetas, puntaje de crédito, entre otras.

---

## 🤖 Modelado
Se utilizó un modelo LightGBM de aprendizaje automático y regresión por su eficiencia y escalabilidad para grandes conjuntos de datos.

- Modelo: **LightGBMRegressor**
- Dataset: 75,330 registros luego del preprocesamiento
- Variables utilizadas: 15 features + objetivo (`total_spent`)
- División: 80% entrenamiento / 20% prueba

### 🧪 Resultados:

| Métrica             | Valor         |
|---------------------|---------------|
| RMSE                | 24,777.46     |
| R² (Coef. Determ.)  | 0.22          |
| RMSE Relativo       | 322.83%       |

> 🟡 El modelo explica solo el 22% de la varianza del gasto total. El error medio supera 3 veces el promedio real, indicando que el modelo es débil para predicción. Podría estar fallando el modelo por capturar variables que no representan de buena forma el gasto por cliente y MCC.
> Al realizarse la limpieza de datos se pudo alterar las columnas de forma no deseada o simplemente, falta de columnas relevantes para entrenar el modelo.

---


## 📌 Conclusiones

- El modelo **no es suficientemente preciso** para tareas de predicción individual.
- Variables como ingresos y edad explican parcialmente el comportamiento, pero no capturan toda la dinámica de gasto.
- Podría existir **información importante no disponible en la base de datos**, como:
  - Tiempo (estacionalidad)
  - Tipo de comercio (detalle de MCC)
  - Frecuencia y recencia de gasto

---

## 🔁 Recomendaciones y Próximos Pasos

1. Incluir **información temporal** (fecha de transacción, día de la semana, mes).
2. Explorar modelos alternativos como `CatBoost` o `RandomForest`.
3. Validar la calidad de datos de entrada y excluir los datos que no sean significativos para el modelo (¿hay campos con mucho ruido o errores sistemáticos?).
4. Considerar segmentar clientes por comportamiento y predecir por grupo (Clustering).

---

## 🛠️ Herramientas Utilizadas

- **Python** 3.x
- `pandas`, `numpy`, `scikit-learn`, `lightgbm`, `matplotlib`, `seaborn`
- Visual Studio Code
- Git

---


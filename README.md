# Prueba_Seccion_SGP
Repositorio creado con la única finalidad de desarrollar la prueba técnica de ciencia de datos para la vacante de Analítico (Junior) Sección Gestión Proveedores

# README

## Proyecto Analítico: Dataset de Transacciones Financieras

Este proyecto se centra en el análisis de un conjunto de datos de registros de transacciones, información del consumidor y datos de cartas de una institución bancaria durante la década de los 2010s.

---

Requisitos Previos

1. Crear un Ambiente Virtual

Se recomienda crear un entorno virtual para gestionar las dependencias. Siga los siguientes pasos:

python -m venv .venv
source .venv/bin/activate  # En Linux/MacOS
.venv\Scripts\activate    # En Windows

2. Instalar Dependencias

Las dependencias necesarias están especificadas en el archivo requirements.txt. Para instalarlas, ejecute:

pip install -r requirements.txt

3. Ubicación de los Datos

Los archivos CSV descargados desde Kaggle ejecutando (`download_df.py`), módulo encargado de descargar las bases de datos de Kaggle por primera vez en la ubicación:

data/raw/

```bash
python download_df.py
```

El archivo de registros de transacciones, información del consumidor y datos de cartas se llaman: `transactions_data.csv`, `users_data.csv` y `cards_data.csv`, respectivamente.
---

## Ejecución del Proyecto

El archivo principal de ciencia de datos (actividad 2) `2_modelo_opt.py` consolida todas las funcionalidades. Para ejecutarlo:

```bash
python 2_modelo_opt.py
```

Este archivo realiza las siguientes acciones:

1. Limpieza de datos.
2. Carga y preparación de archivos csv.
3. Ingeniería de características.
4. Entrenamiento del modelo LightGBM.
5. Métricas RMSE, R^2 y RMSE Relativo.

---

## Ejemplo de Uso

### Datos de Uso
 El conjunto de datos en el repositorio en Kaggle [este enlace](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets/data).

### Salida del Proyecto
- Modelo predictivo generado a partir de las características independientes:
    [
        "current_age",
        "retirement_age",
        "birth_year",
        "birth_month",
        "per_capita_income",
        "yearly_income",
        "total_debt",
        "credit_score",
        "num_credit_cards",
        "debt_to_income_ratio",
        "avg_credit_limit",
        "total_credit_limit",
        "total_cards_issued",
        "pct_chip_cards",
        "any_dark_web_card",
        "mcc",
    ]
- Característica Dependiente: ["total_spent"]
- Métricas para identificar la calidad del modelo generado y proponer alternativas.

---

## Estructura del Repositorio

```
├── .venv/ # Entorno virtual de Python
│
├── answers/ # Carpeta con respuestas y scripts SQL
│ ├── 1a_queries.sql
│ ├── 1b_queries.sql
│ ├── 1c_queries.sql
│ ├── 1d_optimization.md # Archivo .md con ideas o recomendaciones de mejora para el manejo de BigData con SQL
│ └── 2_modelo_opt.py # Script Python optimizado para entrenamiento
│
├── data/
│ ├── raw/ # Datos sin procesar
│ │ ├── cards_data.csv
│ │ ├── transactions_data.csv
│ │ ├── users_data.csv
│ │ ├── train_fraud_labels.json
│ │ └── __MACOSX/ # Carpeta generada por macOS (puede ser ignorada)
│
├── 0_download_df.py # Script auxiliar para descargar de Kaggle
├── new_data.zip # Archivo comprimido con nuevos datos
├── requirements.txt # Dependencias del proyecto (pip install -r)
├── README.md # Documentación principal del repositorio
├── report.md # Resultado y conclusiones del repositorio
```

---

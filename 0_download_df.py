import zipfile

import pandas as pd
import requests

# Extraer datos ( Una vez)
# Cargar el dataset de transacciones directamente desde la URL
url = "https://cdn.nuwe.io/challenges-ds-datasets/hackathon-caixabank-data-24/transactions_data.csv"

transactions_df = pd.read_csv(url)

# Export as CSV the df to transactions.csv.
transactions_df.to_csv("./data/raw/transactions_data.csv", index=False)

# URL del archivo ZIP - Cards_data.csv - Users_data.csv
url_2 = "https://cdn.nuwe.io/challenges-ds-datasets/hackathon-caixabank-data-24/new_data.zip"
zip_file = "new_data.zip"

# Descargar el archivo ZIP - Cards_data.csv - Users_data.csv
response = requests.get(url_2)

with open(zip_file, "wb") as f:
    f.write(response.content)

# Descomprimir el archivo
with zipfile.ZipFile(zip_file, "r") as zip_ref:
    zip_ref.extractall("./data/raw/")  # Carpeta donde se descomprimirán los archivos

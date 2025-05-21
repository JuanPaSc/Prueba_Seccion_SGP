# Buenas prácticas en consultas SQL sobre Big Data en el sector financiero

En el sector financiero el manejo de grandes conjuntos de datos es una actividad común.

Al realizar una query en SQL hay una serie de buenas prácticas para la manipulación de información en BigData y no terminar afectando el funcionamiento de la base de datos comunitaria (Siendo este caso la Landing Zone en Bancolombia).

## 1. Filtado de Columnas

- Seleccionar sólo las columnas necesarias (SELECT Columna1, Columna2,... en vez de SELECT *)

- Utilizar cláusulas WHERE para reducir el volumen de datos que se va a consultar, omitiendo los no necesarios.

**Ejemplo:**
```sql
SELECT nombre, saldo 
FROM cuentas 
WHERE saldo > 100000;

2. Uso de formatos de almacenamiento eficiente

- Utilizar formatos columnar como Parquet o ORC para reducir I/0 y Mejorar la compresión

3. Uso eficiente de las particiones

- Particionar tablas grandes por campos de alta cardinalidad o uso frecuente (ej. fecha de transacción, región, tipo de producto)

Ejemplo: 
SELECT * 
FROM transacciones 
WHERE fecha = '2025-05-01';

4. Evitar operaciones costosas innecesarias

- Minimizar uso de funciones agregadas complejas si no son necesarias.

5. Controlar el uso de DISTINCT y ORDER BY

- DISTINCT puede ser muy costoso en grandes volúmenes, solo se debería usar cuando sea realmente necesario.

- ORDER BY debe evitarse a menos que se necesite.
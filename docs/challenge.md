# Part I

## Bugs

### 1. Problema con sns.barplot

Se encontró un error en el uso de `sns.barplot` cuando no se especificaban las claves 'x' e 'y' en los datos pasados como argumentos. Este problema fue resuelto.

### 2. Ubicación incorrecta de data.csv en test_model.py

Se corrigió la ubicación del archivo `data.csv` en el archivo `test_model.py` para que los datos se carguen correctamente. No se modificó la lógica de las pruebas, solo se ajustó la ubicación del archivo.

## Elección del Modelo

### Comparación de Modelos

Se compararon dos modelos, Logistic Regression y XGBoost, en función de varias métricas:

- **Precisión**: Ambos modelos tienen una precisión bastante similar en la clase 1, con un valor de aproximadamente 0.25. Esto significa que alrededor del 25% de las predicciones positivas son correctas para ambos modelos.

- **Recuperación (Recall)**: La recuperación es también similar en ambos modelos para la clase 1, con un valor de alrededor del 0.69. Esto significa que ambos modelos identifican alrededor del 69% de los verdaderos casos de retraso.

- **Puntaje F1 (F1-Score)**: El puntaje F1, que es una métrica que combina precisión y recuperación, también es comparable en ambos modelos, con valores de aproximadamente 0.36 para Logistic Regression y 0.37 para XGBoost.

- **Exactitud (Accuracy)**: Ambos modelos tienen una precisión total de aproximadamente 0.55, lo que indica que el 55% de las predicciones son correctas en general.

### Elección de Logistic Regression

Se eligió Logistic Regression sobre XGBoost por los siguientes motivos:

- **Interpretabilidad**: Logistic Regression es un modelo más interpretable en comparación con XGBoost.

- **Eficiencia en tiempo real**: Logistic Regression tiende a ser más rápido en tiempo real, lo que puede ser beneficioso en aplicaciones en las que se requieren predicciones rápidas.

En resumen, aunque ambos modelos tienen un rendimiento similar en el conjunto de datos, se optó por Logistic Regression debido a su interpretabilidad y eficiencia en tiempo real.


# Part II
## Bugs

### 1. Problema con anyio
pip list me mostró que tenía instalado anyio version 4.0.0. Me generaba un error las pruebas: AttributeError: module 'anyio' has no attribute 'start_blocking_portal'.
Investigando, parece que anyio introdujo ciertos cambios en la version 4.0.0 que estaban causando los problemas con mi entorno de trabajo.
La solución fue hacer un version downgrade: pip install anyio==3.4.0.


# Part III
Se decide utilizar GCP. 
URL API: https://mlechallengeimage-3z6cfqfdaq-ue.a.run.app

Para probar los tests de stress tuve que isntalar una librería faltante que no se encontraba en requirements.txt: 
pip3 install locust
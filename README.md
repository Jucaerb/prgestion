# Análisis de Predicción del Riesgo de Enfermedades Cardiovasculares (CVD)

## Problema
El riesgo de enfermedades cardiovasculares (CVD) es una de las principales causas de muerte a nivel mundial. Predecir de manera precisa este riesgo a partir de factores de estilo de vida y salud general puede permitir la implementación de intervenciones preventivas personalizadas. Este análisis se enfoca en desarrollar un modelo predictivo utilizando datos de salud y estilo de vida de individuos con el objetivo de identificar aquellos en mayor riesgo de sufrir una CVD.

## Contenido del Repositorio
En este repositorio encontrarás los siguientes archivos:
- **Notebook de análisis y predicción**: Un notebook que realiza la limpieza de datos, el análisis exploratorio y la creación de un modelo predictivo para estimar el riesgo de CVD.
- **Notebook de conexión a BD con SQL**: Un notebook que realiza una transformación del dataset a BD y en el cual se realiza un CRUD sobre la misma para actualizar el tablero de Streamlite.
- **Archivos de entorno para Streamlite**: Un entorno virtual de Python en el cual están instaladas las librerías necesarias para el despliegue.
- **Dataset**: Un archivo CSV con los datos preprocesados utilizados en el análisis.
- **README.md**: Este archivo con la descripción del proyecto.
- **Gráficos y visualizaciones**: Visualizaciones clave generadas durante el análisis de los datos.
  
## Descripción de los Datos
Se utilizaron un total de **256341** registros en el dataset, que corresponden a información sobre la salud, estilo de vida y condiciones médicas de individuos. Cada registro contiene las siguientes **16 características**:
- **General_Health**: Estado general de salud (categórico).
- **Checkup**: Tiempo desde la última revisión médica (categórico).
- **Exercise**: Indicador de si la persona realiza ejercicio (binario).
- **Heart_Disease**, **Skin_Cancer**, **Other_Cancer**, **Depression**, **Diabetes**, **Arthritis**: Indicadores de varias condiciones médicas (binarios).
- **Sex**: Género del individuo (binario).
- **Age_Category**: Rango de edad del individuo (categórico).
- **Height_(cm)**, **Weight_(kg)**, **BMI**: Información física del individuo (numérico).
- **Smoking_History**, **Alcohol_Consumption**, **Fruit_Consumption**, **Green_Vegetables_Consumption**, **FriedPotato_Consumption**: Hábitos de vida y dieta (numérico y categórico).

## Descubrimientos en los Datos
El análisis exploratorio reveló varias correlaciones significativas entre los factores de estilo de vida, condiciones médicas y el riesgo de desarrollar una enfermedad cardiovascular. Por ejemplo:
- **El ejercicio regular** y una **dieta saludable** (alto consumo de frutas y vegetales) se asocian negativamente con el riesgo de CVD.
- Condiciones como la **diabetes**, **depresión** y el **historial de enfermedades cardíacas** aumentan significativamente el riesgo.
- **El índice de masa corporal (IMC)** alto también es un factor de riesgo crítico.

## Impacto Empresarial
El descubrimiento de patrones claros en los datos de salud puede ser valioso para empresas en sectores como:
- **Seguros de salud**: Ofrecer primas ajustadas basadas en el riesgo predictivo de CVD, lo que permite planes de seguros más personalizados.
- **Servicios de salud preventivos**: Identificar a individuos en alto riesgo y proporcionarles planes de prevención más dirigidos, mejorando la eficiencia de los programas de salud pública.
- **Wellness y fitness**: Crear productos y servicios que incentiven la adopción de hábitos más saludables en individuos con alto riesgo.

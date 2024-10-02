#!/usr/bin/env python
# coding: utf-8

# In[2]:

import os

# Mostrar información de streamlit
os.system('pip show streamlit')

# Instalar streamlit si es necesario
os.system('pip install streamlit')


# In[2]:

import pandas as pd

# Cargar el archivo CSV
file_path = './CVD_cleaned.csv'
df = pd.read_csv(file_path)

# Mostrar las primeras filas del DataFrame
df.head()


# In[3]:

import sqlite3

# Conectar a la base de datos SQLite (se creará si no existe)
conn = sqlite3.connect('CVD_data.db')

# Guardar el DataFrame en la base de datos
df.to_sql('health_data', conn, if_exists='replace', index=False)

# Confirmar que se ha guardado
print("DataFrame guardado en la base de datos SQLite.")

# Cerrar la conexión
conn.close()


# In[4]:

import streamlit as st
import pandas as pd
import sqlite3

# Función para conectarse a la base de datos SQLite
def connect_db():
    conn = sqlite3.connect('CVD_data.db')
    return conn

# Función para leer los datos de la base de datos
def leer_datos():
    conn = connect_db()
    df = pd.read_sql_query("SELECT * FROM health_data", conn)
    conn.close()
    return df

# Función para insertar nuevos registros
def insertar_dato(general_health, checkup, exercise, heart_disease, skin_cancer):
    conn = connect_db()
    query = """
    INSERT INTO health_data (General_Health, Checkup, Exercise, Heart_Disease, Skin_Cancer)
    VALUES (?, ?, ?, ?, ?)
    """
    conn.execute(query, (general_health, checkup, exercise, heart_disease, skin_cancer))
    conn.commit()
    conn.close()

# Función para actualizar un registro
def actualizar_dato(old_health, new_health):
    conn = connect_db()
    query = "UPDATE health_data SET General_Health = ? WHERE General_Health = ?"
    conn.execute(query, (new_health, old_health))
    conn.commit()
    conn.close()

# Función para eliminar un registro
def eliminar_dato(health_condition):
    conn = connect_db()
    query = "DELETE FROM health_data WHERE General_Health = ?"
    conn.execute(query, (health_condition,))
    conn.commit()
    conn.close()

# Título de la aplicación
st.title("Visualización de Datos de Salud - CVD")

# Mostrar los datos
st.subheader("Datos actuales")
df = leer_datos()
st.dataframe(df)

# Formulario para agregar nuevos datos
st.subheader("Agregar nuevo registro")
with st.form("Agregar nuevo"):
    general_health = st.selectbox("General Health", df['General_Health'].unique())
    checkup = st.selectbox("Checkup", df['Checkup'].unique())
    exercise = st.selectbox("Exercise", df['Exercise'].unique())
    heart_disease = st.selectbox("Heart Disease", df['Heart_Disease'].unique())  
    skin_cancer = st.selectbox("Skin Cancer", df['Skin_Cancer'].unique())
    submitted = st.form_submit_button("Agregar")
    
    if submitted:
        insertar_dato(general_health, checkup, exercise, heart_disease, skin_cancer)
        st.success("Registro agregado exitosamente")

# Formulario para actualizar datos
st.subheader("Actualizar registro")
with st.form("Actualizar"):
    old_health = st.selectbox("Seleccionar General Health", df['General_Health'].unique())
    new_health = st.text_input("Nuevo estado de salud")
    update_submitted = st.form_submit_button("Actualizar")
    
    if update_submitted:
        actualizar_dato(old_health, new_health)
        st.success("Registro actualizado exitosamente")

# Formulario para eliminar datos
st.subheader("Eliminar registro")
with st.form("Eliminar"):
    health_condition = st.selectbox("Seleccionar General Health a eliminar", df['General_Health'].unique())
    delete_submitted = st.form_submit_button("Eliminar")
    
    if delete_submitted:
        eliminar_dato(health_condition)
        st.success("Registro eliminado exitosamente")

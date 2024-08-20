import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Mi Primera Aplicación en Streamlit")

# Cargar un DataFrame
df = pd.DataFrame({
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
    'Edad': [24, 27, 22, 32],
    'Ciudad': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
})

# Mostrar la tabla de datos
st.write("Aquí están los datos:")
st.write(df)

# Gráfico simple
st.write("Gráfico de Edad:")
fig, ax = plt.subplots()
ax.bar(df['Nombre'], df['Edad'])
st.pyplot(fig)

# Interactividad con un widget
edad_minima = st.slider('Selecciona la edad mínima', min_value=20, max_value=40, value=25)
st.write(f"Usuarios con edad mayor o igual a {edad_minima}:")
st.write(df[df['Edad'] >= edad_minima])

import numpy as np 
import pandas as pd
import streamlit as st
pd.options.display.float_format = '{:,.3f}'.format
pd.set_option('display.max_columns', 100)
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

from ipywidgets import widgets
from ydata_profiling import ProfileReport
from ydata_profiling.utils.cache import cache_file



# ca_df = pd.read_parquet('https://easy-money-project-bucket.s3.eu-west-3.amazonaws.com/commercial_activity_df.parquet')

# prod_df = pd.read_parquet('https://easy-money-project-bucket.s3.eu-west-3.amazonaws.com/products_df.parquet')

# sdg_df = pd.read_parquet('https://easy-money-project-bucket.s3.eu-west-3.amazonaws.com/sociodemographic_df.parquet')
# carga del dataset completo
df_full = pd.read_parquet("/Users/claudiacastro/easy_money_project/df_completo.parquet")
# eliminamos columnas que no aportan información
df_full = df_full.drop(columns=['Unnamed: 0_x', 'Unnamed: 0_y', 'Unnamed: 0'], axis=1)
# eliminamos duplicados a partir de la columna pk_cid y nos quedamos con el primero
#df_full = df_full.drop_duplicates(subset=['pk_cid', "entry_date"], keep="first")


# df_1 = pd.merge(ca_df,prod_df, how="inner" ,on=['pk_cid','pk_partition'])

# df_2 = pd.merge(df_1,sdg_df, how="inner",on=['pk_cid','pk_partition'])

# df_2.to_parquet("/Users/claudiacastro/easy_money_project/df_completo.parquet")


# modificamos el tipo de dato de las columnas, SIMPLEMENTE CAMBIA EL TIPO DE DATO
df_full["pk_partition"] = pd.to_datetime(df_full["pk_partition"])
df_full["entry_date"] = pd.to_datetime(df_full["entry_date"], errors='coerce')
df_full["entry_channel"] = df_full["entry_channel"].astype('category')
df_full['active_customer'] = df_full['active_customer'].astype('int32')
df_full['segment'] = df_full['segment'].astype('category')
df_full['short_term_deposit'] = df_full['short_term_deposit'].astype('int32')
df_full['loans'] = df_full['loans'].astype('int32')
df_full['mortgage'] = df_full['mortgage'].astype('int32')
df_full['funds'] = df_full['funds'].astype('int32')
df_full['securities'] = df_full['securities'].astype('int32')
df_full['long_term_deposit'] = df_full['long_term_deposit'].astype('int32')
df_full['credit_card'] = df_full['credit_card'].astype('int32')
# df_full['payroll'] = df_full['payroll'].astype('int32')
# df_full['pension_plan'] = df_full['pension_plan'].astype('int32')
df_full['payroll_account'] = df_full['payroll_account'].astype('int32')
df_full['emc_account'] = df_full['emc_account'].astype('int32')
df_full['debit_card'] = df_full['debit_card'].astype('int32')
df_full['em_account_p'] = df_full['em_account_p'].astype('int32')
df_full['em_acount'] = df_full['em_acount'].astype('int32')
df_full["country_id"] = df_full["country_id"].astype('category')
df_full["region_code"] = df_full["region_code"].astype('category')
df_full["gender"] =  df_full["gender"].astype('category')
df_full["age"] = df_full["age"].astype('int32')
df_full["deceased"] = df_full["deceased"].astype('category')
# reporte del dataset
# profile = ProfileReport(df_full, title="Profiling Report Easy Money")
# profile.to_file("profiling_report_easyMoney.html")
# valores nulos en el dataset



new = df_full.groupby("active_customer")["pk_cid"].nunique()

# quiero el grafico en la derecha

st.write("Gráfico de Edad:")
fig, ax = plt.subplots( figsize=(10, 5), dpi=100, facecolor='w', edgecolor='k', linewidth=1,
                       )
ax.bar(new.index, new.values)

st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt

# Suponiendo que 'new' es el resultado del grupo por 'active_customer'
new = df_full.groupby("active_customer")["pk_cid"].nunique()

# Dividir el layout en tres columnas
col1, col2, col3 = st.columns(3)

# Gráfico en la columna izquierda (col1)
with col1:
    st.write("Gráfico a la Izquierda")
    fig_left, ax_left = plt.subplots(figsize=(5, 3), dpi=100)
    ax_left.bar(new.index, new.values, color='skyblue')
    st.pyplot(fig_left)

# Gráfico en la columna central (col2)
with col2:
    st.write("Gráfico en el Centro")
    fig_center, ax_center = plt.subplots(figsize=(5, 3), dpi=100)
    ax_center.bar(new.index, new.values, color='orange')
    st.pyplot(fig_center)

# Gráfico en la columna derecha (col3)
with col3:
    st.write("Gráfico a la Derecha")
    fig_right, ax_right = plt.subplots(figsize=(5, 3), dpi=100)
    ax_right.bar(new.index, new.values, color='green')
    st.pyplot(fig_right)


import streamlit as st
import matplotlib.pyplot as plt

# Suponiendo que 'new' es el resultado del grupo por 'active_customer'
new = df_full.groupby("active_customer")["pk_cid"].nunique()

# Dividir el layout en tres columnas con proporciones ajustadas
col1, col2, col3 = st.columns([1, 1, 1])  # Aquí 1, 1, 1 indica proporciones iguales

# Gráfico en la columna izquierda (col1)
with col1:
    st.write("Gráfico a la Izquierda")
    fig_left, ax_left = plt.subplots(figsize=(6, 4), dpi=100)  # Aumentar figsize para ocupar más espacio
    ax_left.bar(new.index, new.values, color='skyblue')
    st.pyplot(fig_left)

# Gráfico en la columna central (col2)
with col2:
    st.write("Gráfico en el Centro")
    fig_center, ax_center = plt.subplots(figsize=(6, 4), dpi=100)  # Aumentar figsize
    ax_center.bar(new.index, new.values, color='orange')
    st.pyplot(fig_center)

# Gráfico en la columna derecha (col3)
with col3:
    st.write("Gráfico a la Derecha")
    fig_right, ax_right = plt.subplots(figsize=(6, 4), dpi=100)  # Aumentar figsize
    ax_right.bar(new.index, new.values, color='green')
    st.pyplot(fig_right)


import streamlit as st
import matplotlib.pyplot as plt

# Suponiendo que 'new' es el resultado del grupo por 'active_customer'
new = df_full.groupby("active_customer")["pk_cid"].nunique()

# Crear un contenedor para los gráficos
with st.container():
    # Dividir el layout en tres columnas
    col1, col2, col3 = st.columns([1, 1, 1])

    # Gráfico en la columna izquierda (col1)
    with col1:
        st.write("Gráfico a la Izquierda")
        fig_left, ax_left = plt.subplots(figsize=(8, 6), dpi=100)
        ax_left.bar(new.index, new.values, color='skyblue')
        st.pyplot(fig_left)

    # Gráfico en la columna central (col2)
    with col2:
        st.write("Gráfico en el Centro")
        fig_center, ax_center = plt.subplots(figsize=(8, 6), dpi=100)
        ax_center.bar(new.index, new.values, color='orange')
        st.pyplot(fig_center)

    # Gráfico en la columna derecha (col3)
    with col3:
        st.write("Gráfico a la Derecha")
        fig_right, ax_right = plt.subplots(figsize=(8, 6), dpi=100)
        ax_right.bar(new.index, new.values, color='green')
        st.pyplot(fig_right)

st.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")   

import streamlit as st
import matplotlib.pyplot as plt

# Suponiendo que 'new' es el resultado del grupo por 'active_customer'
new = df_full.groupby("active_customer")["pk_cid"].nunique()

# Gráfico a pantalla completa (una sola columna)
st.write("Gráfico a pantalla completa")
fig, ax = plt.subplots(figsize=(15, 8), dpi=100)
ax.bar(new.index, new.values, color='skyblue')
st.pyplot(fig, use_container_width=True)



# Título principal del dashboard
st.title("Dashboard")

# Barra lateral de navegación
st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a:", ["Dashboard", "Data Annotation", "Model Training", "Model Tuning", "Data Extraction", "Settings"])

if page == "Dashboard":
    # Tarjetas de información al principio
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(label="Documents", value="10.5K", delta="125")
    with col2:
        st.metric(label="Annotations", value="510", delta="-2", delta_color="inverse")
    with col3:
        st.metric(label="Accuracy", value="87.9%", delta="0.1%")
    with col4:
        st.metric(label="Training Time", value="1.5 hours", delta="10 mins", delta_color="inverse")
    with col5:
        st.metric(label="Processing Time", value="3 seconds", delta="-0.1 seconds")

    # Sección de extracción de datos
    st.subheader("Data Extraction")
    data1 = np.random.randn(20, 3)
    fig1, ax1 = plt.subplots()
    ax1.plot(data1)
    st.pyplot(fig1)

    # Sección de entrenamiento de modelos y anotación de datos
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Model Training")
        data2 = np.random.randn(20, 3)
        fig2, ax2 = plt.subplots()
        ax2.bar(np.arange(20), np.random.randn(20))
        st.pyplot(fig2)
    
    with col2:
        st.subheader("Data Annotation")
        data3 = np.random.randn(20, 3)
        fig3, ax3 = plt.subplots()
        ax3.fill_between(np.arange(20), data3[:, 0], data3[:, 1], color="skyblue", alpha=0.4)
        ax3.fill_between(np.arange(20), data3[:, 1], data3[:, 2], color="red", alpha=0.4)
        st.pyplot(fig3)

elif page == "Data Annotation":
    st.header("Data Annotation Page")
    st.write("Aquí podrías agregar contenido específico para la anotación de datos.")

# Puedes seguir añadiendo más opciones para cada página seleccionada en la barra lateral
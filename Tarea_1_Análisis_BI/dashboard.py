import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pandas as pd
import plotly.express as px

# Configuración de la página de Streamlit
st.set_page_config(page_title="Easy Money Dashboard", page_icon=":moneybag:", layout="wide")

# Variable para el estado de la pantalla de bienvenida
if "welcome" not in st.session_state:
    st.session_state.welcome = True

if st.session_state.welcome:
    # Pantalla de bienvenida
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("https://easy-money-project-bucket.s3.eu-west-3.amazonaws.com/LOGO_EasyMoney.jpg", width=700)
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st.title("Bienvenido a Easy Money")
            st.write("Gestiona, analiza y optimiza tus datos financieros de manera efectiva.")
    
    # Botón para acceder al dashboard
            if st.button("Acceder al Dashboard"):
                st.session_state.welcome = False
else:
    # Barra lateral de navegación
    st.sidebar.title("DASHBOARD")
    st.sidebar.image("https://easy-money-project-bucket.s3.eu-west-3.amazonaws.com/LOGO_EasyMoney.jpg", width=300)

    st.sidebar.write("Navegación")
    page = st.sidebar.radio("Ir a:", ["Actividad Comercial", "Productos", "SocioDemográfico", 
                                      "Segmentación", "Recomendación", "Personalización",
                                     "Seguimiento", "Cooordinación"])

    if page == "Actividad Comercial":
        
        df_actividad_comercial = pd.read_parquet("https://easy-money-project-bucket.s3.eu-west-3.amazonaws.com/commercial_activity_df_clean.parquet")
        
        col1, col2, col3 = st.columns([3, 5, 1])
        with col2:
            st.title("Actividad Comercial")
        st.write("---")
        # Tarjetas de información al principio
        #col1, col2, col3, col4, col5 = st.columns(5)
        #with col1:
        #    st.metric(label="Documents", value="10.5K", delta="125")
        #with col2:
        #    st.metric(label="Annotations", value="510", delta="-2", delta_color="inverse")
        #with col3:
        #    st.metric(label="Accuracy", value="87.9%", delta="0.1%")
        #with col4:
        #    st.metric(label="Training Time", value="1.5 hours", delta="10 mins", delta_color="inverse")
        #with col5:
        #    st.metric(label="Processing Time", value="3 seconds", delta="-0.1 seconds")

        #---------------------------------------------------------------------------------------------------------------------
         # Gráfico de donut con tonos verdes
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            segment_distribution = df_actividad_comercial.groupby("segment")["pk_cid"].nunique().apply(lambda x: x / df_actividad_comercial["pk_cid"].nunique() * 100)
            fig, ax = plt.subplots(figsize=(6, 6))
            colors = plt.cm.Greens(np.linspace(0.3, 0.9, len(segment_distribution)))

            # Crear el gráfico de pastel (donut)
            wedges, texts, autotexts = ax.pie(segment_distribution, labels=segment_distribution.index, autopct='', 
                                            colors=colors, startangle=140)

            # Hacer el centro del gráfico de pastel vacío para crear el efecto de donut
            centre_circle = plt.Circle((0, 0), 0.70, fc='white')
            fig.gca().add_artist(centre_circle)

            # Añadir el valor total de clientes en el centro del gráfico
            total_clients = df_actividad_comercial["pk_cid"].nunique()
            ax.text(0, 0, f'{total_clients}', ha='center', va='center', fontsize=30, color='black', fontweight='bold', fontfamily='sans-serif')

            # Ajustar el aspecto del gráfico y mostrarlo en Streamlit
            ax.set_title('Distribución de segmentos de clientes')
            ax.axis('equal')  # Asegurar que el gráfico es circular

            # Colocar los valores de porcentaje fuera del gráfico
            for i, a in enumerate(wedges):
                ang = (a.theta2 - a.theta1) / 2. + a.theta1
                x = np.cos(np.deg2rad(ang))
                y = np.sin(np.deg2rad(ang))

                horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
                connectionstyle = "angle,angleA=0,angleB={}".format(ang)

                ax.annotate(f'{segment_distribution.iloc[i]:.2f}%', xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                            horizontalalignment=horizontalalignment, 
                            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1),
                            arrowprops=dict(arrowstyle="-", connectionstyle=connectionstyle))

            st.pyplot(fig)

        #---------------------------------------------------------------------------------------------------------------------
        # Contar la cantidad de clientes activos y no activos
        # Creando columnas
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Historial de Actividad Comercial")
            plt.figure(figsize=(10, 6))
            ax = sns.countplot(data=df_actividad_comercial, x="pk_partition", hue="active_customer", palette="viridis")

            # Rotar las etiquetas del eje X para mejorar la legibilidad
            plt.xticks(rotation=60)
            plt.xlabel("Fecha de Partición")
            plt.ylabel("Cantidad de Clientes")

            # Mostrar el gráfico en Streamlit
            st.pyplot(plt)

        with col2:
            st.subheader("Distribución de Canales de Entrada")
            viridis_palette = sns.color_palette("viridis", as_cmap=False)
            # Escoger un color de la paleta 'viridis'
            color = viridis_palette[3] # Verde
            fig, ax = plt.subplots(figsize=(10, 6))
            entry_channel_percentages = df_actividad_comercial["entry_channel"].value_counts().apply(lambda x: x / df_actividad_comercial["entry_channel"].count() * 100)
            entry_channel_percentages.plot(kind='bar', color=color, ax=ax)

            # Agregar las etiquetas con los porcentajes encima de las barras
            for i, v in enumerate(entry_channel_percentages):
                ax.text(i, v + 0.5, f"{v:.2f}%", ha='center')

            # Añadir título y etiquetas a los ejes
            ax.set_xlabel("Canal de Entrada")
            ax.set_ylabel("Porcentaje (%)")

            # Mostrar el gráfico en Streamlit
            st.pyplot(fig)
            
     
        #---------------------------------------------------------------------------------------------------------------------
        
        st.subheader("Cantidad de clientes según la fecha en que se realizó la primera contratación")
        # Agrupar los datos por 'entry_date' y contar el número de clientes únicos por día
        clientes_por_dia = df_actividad_comercial.groupby("entry_date")["pk_cid"].nunique().reset_index()

        # Crear un gráfico de línea interactivo con Plotly
        fig = px.line(clientes_por_dia, x='entry_date', y='pk_cid', labels={'pk_cid': 'Number of Customers', 'entry_date': 'Date'}, color_discrete_sequence=['#21918c'])

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)
      
        
        #---------------------------------------------------------------------------------------------------------------------
        
        st.subheader("Cantidad de clientes nuevos por partición")

        # Supongo que ca_df ya está cargado y contiene las columnas 'pk_partition' y 'pk_cid'

        # Ordenar los datos por 'pk_partition' y 'pk_cid'
        ca_df = df_actividad_comercial.sort_values(by=['pk_partition', 'pk_cid'])

        # Obtener una lista única de particiones ordenadas
        particiones = ca_df['pk_partition'].unique()

        # Crear un diccionario para almacenar el número de clientes en la primera partición y los nuevos clientes por cada partición
        clientes_por_particion = {}

        # Mantener un conjunto de todos los clientes vistos hasta la partición actual
        clientes_acumulados = set()

        # Iterar sobre las particiones
        for particion in particiones:
            # Obtener los clientes de la partición actual
            clientes_actuales = set(ca_df[ca_df['pk_partition'] == particion]['pk_cid'])
            
            # Identificar nuevos clientes en la partición actual excluyendo los ya vistos
            nuevos_en_particion_actual = clientes_actuales - clientes_acumulados
            
            # Almacenar el número de nuevos clientes en el diccionario
            clientes_por_particion[particion] = len(nuevos_en_particion_actual)
            
            # Actualizar el conjunto acumulado con los clientes actuales
            clientes_acumulados.update(clientes_actuales)

        # Convertir el diccionario en un DataFrame para su análisis
        df_clientes_por_particion = pd.DataFrame(list(clientes_por_particion.items()), columns=['pk_partition', 'num_clientes'])
        # Crear el gráfico de barras
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.bar(df_clientes_por_particion['pk_partition'], df_clientes_por_particion['num_clientes'], color=color)
        ax.set_title('Clientes nuevos por partición con respecto a la anterior')
        ax.set_xlabel('pk_partition')
        ax.set_ylabel('num_clientes')

        # Agregar etiquetas en cada barra
        for i in range(len(df_clientes_por_particion)):
            ax.text(i, df_clientes_por_particion['num_clientes'][i], df_clientes_por_particion['num_clientes'][i], ha='center', va='bottom')

        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)


    elif page != "Actividad Comercial":
        st.header("Data Page")
        st.write("Aquí se agrega contenido específico para cada Tarea.")

    # Puedes seguir añadiendo más opciones para cada página seleccionada en la barra lateral

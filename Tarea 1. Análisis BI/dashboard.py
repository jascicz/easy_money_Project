import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título principal del dashboard
st.title("Easy Money Dashboard")

# Barra lateral de navegación
st.sidebar.title("DASHBOARD")
st.sidebar.title("Easy Money").image("/Users/claudiacastro/easy_money_project/LOGO_EasyMoney.jpg", width=300)

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
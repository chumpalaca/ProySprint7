import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # Botón para el histograma
scatter_button = st.button('Construir gráfico de dispersión')  # Botón para el gráfico de dispersión

st.header('Venta de autos')

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: #si se hace clic en el botón para el gráfico de dispersión
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión de Odometer vs Precio")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

    #opción, cambiar botones por casillas de verificación
    import streamlit as st

# crear una casilla de verificación
#build_histogram = st.checkbox('Construir un histograma')

#if build_histogram: # si la casilla de verificación está seleccionada
    #st.write('Construir un histograma para la columna odómetro')
    #...
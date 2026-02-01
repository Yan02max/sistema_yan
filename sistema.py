import streamlit as st
import time

st.set_page_config(page_title="Sistema Vacacional YAN", layout="centered")
st.markdown("<h2 style='text-align:center'>🌴 Sistema Vacacional RVPI</h2>", unsafe_allow_html=True)

# Inicializar sesión
if "area_trabajo" not in st.session_state:
    st.session_state.area_trabajo = None
if "historial" not in st.session_state:
    st.session_state.historial = []

# Selección de área con botones grandes
st.subheader("Selecciona tu área de trabajo:")
col1, col2, col3 = st.columns([1,1,1])
button_style = "width:100%; padding:20px; font-size:18px;"

if col1.button("👩‍💼 Atención al cliente"):
    st.session_state.area_trabajo = "P12345"
if col2.button("🚚 Logística"):
    st.session_state.area_trabajo = "R12345"
if col3.button("💼 Gerencia"):
    st.session_state.area_trabajo = "V12345"

# Mostrar área seleccionada
if st.session_state.area_trabajo:
    area_nombre = {"P12345": "Atención al cliente",
                   "R12345": "Logística",
                   "V12345": "Gerencia"}
    st.info(f"Área seleccionada: **{area_nombre[st.session_state.area_trabajo]}**")

# Formulario de datos
with st.form("vacaciones_form"):
    nombre = st.text_input("Nombre completo:")
    tiempo = st.number_input("Tiempo en la empresa (años):", min_value=0.0, step=0.1)
    submitted = st.form_submit_button("Calcular Vacaciones")

# Mostrar resultado con animación mínima
if submitted:
    resultado = st.empty()  # Contenedor para animación
    if st.session_state.area_trabajo is None:
        resultado.error("⚠️ Por favor selecciona un área de trabajo primero.")
    elif not nombre:
        resultado.error("⚠️ Por favor ingresa tu nombre.")
    else:
        dias = 0
        area = st.session_state.area_trabajo

        if area == "P12345":  # Atención al cliente
            if 1 <= tiempo < 2: dias = 6
            elif 2 <= tiempo <= 6: dias = 14
            elif tiempo >= 7: dias = 20
        elif area == "R12345":  # Logística
            if 1 <= tiempo < 2: dias = 7
            elif 2 <= tiempo <= 6: dias = 15
            elif tiempo >= 7: dias = 22
        elif area == "V12345":  # Gerencia
            if 1 <= tiempo < 2: dias = 10
            elif 2 <= tiempo <= 6: dias = 20
            elif tiempo >= 7: dias = 30

        # Animación mínima
        for i in range(3):
            resultado.info("Calculando" + "."*i)
            time.sleep(0.5)

        if dias > 0:
            mensaje = f"Hola {nombre}, gracias por pertenecer a nuestra familia. 🎉\n\n" \
                      f"Correspondes a **{dias} días de vacaciones**. ¡Que las disfrutes! 🌴"
            resultado.success(mensaje)
        else:
            resultado.warning(f"Lo sentimos {nombre}, aún no cumples con los requisitos de la empresa. ❌\nNo tienes derecho a vacaciones.")

        # Guardar en historial
        st.session_state.historial.append({
            "nombre": nombre,
            "area": area_nombre[area],
            "años": tiempo,
            "dias": dias
        })

# Historial de cálculos
if st.session_state.historial:
    st.subheader("📜 Historial de cálculos")
    for item in reversed(st.session_state.historial[-5:]):  # últimos 5 cálculos
        st.write(f"**{item['nombre']}** - {item['area']} - {item['años']} años → {item['dias']} días")

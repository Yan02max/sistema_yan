import streamlit as st

st.set_page_config(page_title="Sistema Vacacional RVPI", layout="centered")
st.title("🌴 Sistema Vacacional RVPI")

# Inicializar variable de área en session_state
if "area_trabajo" not in st.session_state:
    st.session_state.area_trabajo = None

# Selección de área con botones
st.subheader("Selecciona tu área de trabajo:")

col1, col2, col3 = st.columns(3)

if col1.button("👩‍💼 Atención al cliente"):
    st.session_state.area_trabajo = "P12345"
if col2.button("🚚 Logística"):
    st.session_state.area_trabajo = "R12345"
if col3.button("💼 Gerencia"):
    st.session_state.area_trabajo = "V12345"

if st.session_state.area_trabajo:
    area_nombre = {"P12345": "Atención al cliente",
                   "R12345": "Logística",
                   "V12345": "Gerencia"}
    st.info(f"Área seleccionada: {area_nombre[st.session_state.area_trabajo]}")

# Formulario para nombre y tiempo en empresa
with st.form("vacaciones_form"):
    nombre = st.text_input("Nombre completo:")
    tiempo = st.number_input("Tiempo en la empresa (años):", min_value=0.0, step=0.1)
    submitted = st.form_submit_button("Calcular Vacaciones")

if submitted:
    if st.session_state.area_trabajo is None:
        st.error("⚠️ Por favor selecciona un área de trabajo primero.")
    elif not nombre:
        st.error("⚠️ Por favor ingresa tu nombre.")
    else:
        # Lógica de cálculo de vacaciones
        dias = 0
        area = st.session_state.area_trabajo

        if area == "P12345":  # Atención al cliente
            if 1 <= tiempo < 2:
                dias = 6
            elif 2 <= tiempo <= 6:
                dias = 14
            elif tiempo >= 7:
                dias = 20
        elif area == "R12345":  # Logística
            if 1 <= tiempo < 2:
                dias = 7
            elif 2 <= tiempo <= 6:
                dias = 15
            elif tiempo >= 7:
                dias = 22
        elif area == "V12345":  # Gerencia
            if 1 <= tiempo < 2:
                dias = 10
            elif 2 <= tiempo <= 6:
                dias = 20
            elif tiempo >= 7:
                dias = 30

        if dias > 0:
            st.success(f"Hola {nombre}, gracias por pertenecer a nuestra familia. 🎉")
            st.write(f"Correspondes a **{dias} días de vacaciones**. ¡Que las disfrutes! 🌴")
        else:
            st.warning(f"Lo sentimos {nombre}, aún no cumples con los requisitos de la empresa. ❌")
            st.write("No tienes derecho a vacaciones.")

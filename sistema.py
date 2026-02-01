import streamlit as st

st.set_page_config(page_title="Sistema Vacacional RVPI", layout="centered")

st.title("🌴 Sistema Vacacional RVPI")

# Inicializar variable de área en session_state
if "area_trabajo" not in st.session_state:
    st.session_state.area_trabajo = None

# Botones de selección de área
st.subheader("Selecciona tu área de trabajo:")

col1, col2, col3 = st.columns(3)

if col1.button("👩‍💼 Atención al cliente"):
    st.session_state.area_trabajo = "P12345"
if col2.button("🚚 Logística"):
    st.session_state.area_trabajo = "R12345"
if col3.button("💼 Gerencia"):
    st.session_state.area_trabajo = "V12345"

st.write(f"Área seleccionada: {st.session_state.area_trabajo}")

# Formulario
with st.form("vacaciones_form"):
    nombre = st.text_input("Nombre completo:")
    tiempo = st.number_input("Tiempo en la empresa (años):", min_value=0.0, step=0.1)
    submitted = st.form_submit_button("Calcular Vacaciones")

if submitted:
    if st.session_state.area_trabajo is None:
        st.error("⚠️ Por favor selecciona un área de trabajo primero.")
    else:
        # Aquí pones la lógica que ya tienes según área y tiempo
        st.success(f"¡Hola {nombre}! Área: {st.session_state.area_trabajo}, calculando vacaciones...")

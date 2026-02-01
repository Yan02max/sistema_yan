import streamlit as st

st.set_page_config(
    page_title="Sistema Vacacional RVPI",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================
# CSS para estilo app iPhone
# =========================
st.markdown("""
<style>
body {
    font-family: 'Helvetica', sans-serif;
    background-color: #f5f5f7;
    color: #111;
}

h1, h2, h3 {
    text-align: center;
}

.stButton>button {
    background-color: #007AFF;
    color: white;
    font-size: 20px;
    border-radius: 15px;
    padding: 15px;
    margin: 5px 0;
    width: 100%;
    transition: all 0.2s ease;
}
.stButton>button:hover {
    background-color: #005BB5;
}

.output-box {
    background-color: #e0f7fa;
    padding: 15px;
    border-radius: 15px;
    margin-top: 15px;
    animation: fadeIn 0.5s;
}

.history-box {
    background-color: #f0f0f0;
    padding: 12px;
    border-radius: 12px;
    margin-top: 10px;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

body[data-theme="dark"] {
    background-color: #1c1c1e;
    color: #f5f5f5;
}
body[data-theme="dark"] .output-box {
    background-color: #004d40;
    color: #f5f5f5;
}
body[data-theme="dark"] .history-box {
    background-color: #333;
    color: #f5f5f5;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Título con emoji
# =========================
st.markdown("## 🌴 Sistema Vacacional RVPI")

# =========================
# Inicializar historial
# =========================
if "historial" not in st.session_state:
    st.session_state.historial = []

# =========================
# Botones con íconos para áreas
# =========================
st.subheader("Selecciona tu área de trabajo:")

col1, col2, col3 = st.columns(3)
area_trabajo = None

if col1.button("👩‍💼 Atención al cliente"):
    area_trabajo = "P12345"
if col2.button("🚚 Logística"):
    area_trabajo = "R12345"
if col3.button("💼 Gerencia"):
    area_trabajo = "V12345"

# =========================
# Formulario de usuario
# =========================
with st.form("vacaciones_form", clear_on_submit=False):
    nombre = st.text_input("Nombre completo:")
    tiempo = st.number_input("Tiempo en la empresa (años):", min_value=0.0, step=0.1)
    submitted = st.form_submit_button("Calcular Vacaciones")

# =========================
# Lógica de cálculo
# =========================
if submitted:
    dias_vacaciones = None
    area_nombre = None

    if area_trabajo == "P12345":
        area_nombre = "Atención al cliente"
        if 1 <= tiempo < 2:
            dias_vacaciones = 6
        elif 2 <= tiempo <= 6:
            dias_vacaciones = 14
        elif tiempo >= 7:
            dias_vacaciones = 20

    elif area_trabajo == "R12345":
        area_nombre = "Logística"
        if 1 <= tiempo < 2:
            dias_vacaciones = 7
        elif 2 <= tiempo <= 6:
            dias_vacaciones = 15
        elif tiempo >= 7:
            dias_vacaciones = 22

    elif area_trabajo == "V12345":
        area_nombre = "Gerencia"
        if 1 <= tiempo < 2:
            dias_vacaciones = 10
        elif 2 <= tiempo <= 6:
            dias_vacaciones = 20
        elif tiempo >= 7:
            dias_vacaciones = 30

    # =========================
    # Mostrar resultados animados
    # =========================
    if area_nombre is None:
        st.error("⚠️ Por favor selecciona un área de trabajo.")
    elif dias_vacaciones is None:
        mensaje = f"Lo sentimos {nombre}, aún no cumples los requisitos. No tienes derecho a vacaciones."
        st.warning(mensaje)
        st.session_state.historial.append(mensaje)
    else:
        mensaje = f"Hola {nombre}! 🎉\nÁrea: {area_nombre}\nTe corresponden {dias_vacaciones} días de vacaciones. ¡Disfrútalos! 🌴"
        st.markdown(f"<div class='output-box'>{mensaje.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
        st.session_state.historial.append(mensaje)

# =========================
# Historial de consultas scrollable
# =========================
if st.session_state.historial:
    st.subheader("📜 Historial de consultas")
    st.markdown(
        "<div style='max-height:300px;overflow-y:auto;'>", unsafe_allow_html=True
    )
    for idx, h in enumerate(reversed(st.session_state.historial), 1):
        st.markdown(f"<div class='history-box'>{idx}. {h.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st

st.set_page_config(page_title="Sistema Vacacional RVPI", layout="centered")

# =========================
# CSS para estilo moderno
# =========================
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
    font-family: 'Arial', sans-serif;
}
h1 {
    color: #4CAF50;
    text-align: center;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px 20px;
    margin: 5px;
}
.stButton>button:hover {
    background-color: #45a049;
}
.output-box {
    background-color: #e8f5e9;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌴 Sistema Vacacional RVPI")

# =========================
# Formulario de usuario
# =========================
with st.form("vacaciones_form"):
    inf_trabajador = st.text_input("Coloca tu nombre completo:")
    inf_2 = st.text_input("Introduce la clave de área (P12345, R12345, V12345):")
    inf_3 = st.number_input("Introduce el tiempo que llevas con nosotros (años):", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("Calcular Vacaciones")

# =========================
# Lógica de cálculo
# =========================
if submitted:
    dias_vacaciones = None
    area_trabajo = None

    if inf_2 == "P12345":
        area_trabajo = "Atención al cliente"
        if 1 <= inf_3 < 2:
            dias_vacaciones = 6
        elif 2 <= inf_3 <= 6:
            dias_vacaciones = 14
        elif inf_3 >= 7:
            dias_vacaciones = 20

    elif inf_2 == "R12345":
        area_trabajo = "Logística"
        if 1 <= inf_3 < 2:
            dias_vacaciones = 7
        elif 2 <= inf_3 <= 6:
            dias_vacaciones = 15
        elif inf_3 >= 7:
            dias_vacaciones = 22

    elif inf_2 == "V12345":
        area_trabajo = "Gerencia"
        if 1 <= inf_3 < 2:
            dias_vacaciones = 10
        elif 2 <= inf_3 <= 6:
            dias_vacaciones = 20
        elif inf_3 >= 7:
            dias_vacaciones = 30

    # =========================
    # Resultados
    # =========================
    if area_trabajo is None:
        st.error("Área no registrada.")
    elif dias_vacaciones is None:
        st.warning(f"Lo sentimos {inf_trabajador}, aún no cumples con los requisitos de la empresa. No tienes derecho a vacaciones.")
    else:
        st.markdown(f"<div class='output-box'>"
                    f"<h3>Hola {inf_trabajador}</h3>"
                    f"<p>Área de trabajo: <b>{area_trabajo}</b></p>"
                    f"<p>Correspondes a <b>{dias_vacaciones} días de vacaciones</b>.</p>"
                    f"<p>¡Que disfrutes tus vacaciones! 🎉</p>"
                    f"</div>", unsafe_allow_html=True)

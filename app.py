import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Fraud Detection App", layout="centered")


# Carregamento do modelo

@st.cache_resource
def load_model():
    return joblib.load("models/fraud_model_pipeline_vLATEST.joblib")

model = load_model()


# Interface

st.title(" Detecção de Fraude – Simulador")
st.markdown(
    """
    Esta aplicação simula o **uso de um modelo de fraude em produção**.
    Insira os dados de uma transação e obtenha:
    - Probabilidade de fraude
    - Decisão automática com base em threshold operacional
    """
)

st.subheader("Entrada da Transação")

# Exemplo genérico: vetor numérico
num_features = model.named_steps['model'].coef_.shape[1]
input_data = []

for i in range(num_features):
    val = st.number_input(f"Feature {i+1}", value=0.0)
    input_data.append(val)

X_input = np.array(input_data).reshape(1, -1)


# Predição

st.subheader("📊 Resultado")

threshold = st.slider("Threshold de decisão", 0.0, 1.0, 0.5, 0.01)

if st.button("Avaliar Transação"):
    prob_fraude = model.predict_proba(X_input)[0, 1]
    decisao = " FRAUDE" if prob_fraude >= threshold else "✅ LEGÍTIMA"

    st.metric("Probabilidade de Fraude", f"{prob_fraude:.2%}")
    st.write(f"Decisão: **{decisao}**")

st.markdown("---")
st.caption("Modelo de Fraude – Projeto de Portfólio | Ana Paula")

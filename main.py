import streamlit as st
import openai

st.set_page_config(page_title="Synapso - Droits des salariés", layout="centered")

st.title("\U0001F4D8 Synapso - Assistant Droit du Travail \U0001F1EB\U0001F1F7")

openai.api_key = st.secrets.get("OPENAI_API_KEY")

question = st.text_input("Pose ta question (arrêt maladie, licenciement, congés, salaire, etc.)")

if question:
    with st.spinner("Synapso réfléchit..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Tu es un assistant expert en droit du travail français. Réponds de manière simple, claire et concrète aux salariés."},
                    {"role": "user", "content": question}
                ]
            )
            st.success("\u2705 Réponse de Synapso :")
            st.markdown(response["choices"][0]["message"]["content"])
        except Exception as e:
            st.error("\u274C Une erreur est survenue.")

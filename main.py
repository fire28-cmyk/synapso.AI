
import streamlit as st
import requests
from legifrance import get_token

st.set_page_config(page_title="Synapso - Droit du travail", layout="centered")

st.title("📘 Synapso - Assistant Droit du Travail 🇫🇷")

token = get_token()

if not token:
    st.error("❌ Impossible d'obtenir le token d'accès à l'API Légifrance.")
else:
    st.success("✅ Connexion API Légifrance réussie.")

    article_id = st.text_input("Entrez l'identifiant d'un article Légifrance (ex: LEGITEXT000006072050):")

    if article_id:
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        payload = {
            "id": article_id
        }

        url = "https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app/consult/getArticle"
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            st.subheader("📄 Contenu de l'article :")
            st.json(response.json())
        else:
            st.error(f"Erreur API : {response.status_code}")

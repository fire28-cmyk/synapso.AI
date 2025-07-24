# -*- coding: utf-8 -*-
import streamlit as st
from openai import OpenAI
from supabase import create_client, Client

# --- Clés API depuis secrets Streamlit ---
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# --- Connexion clients ---
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
client = OpenAI(api_key=OPENAI_API_KEY)

# --- Interface utilisateur ---
st.set_page_config(page_title="Synapso - Droit du Travail FR")
st.title("📘 Synapso - Assistant Droit du Travail")

# --- Authentification ---
email = st.text_input("Ton adresse e-mail")

if st.button("Se connecter"):
    try:
        supabase.auth.sign_in_with_otp({"email": email})
        st.success("Un e-mail de connexion a ete envoye.")
    except Exception as e:
        st.error(f"Erreur d'envoi : {e}")

user = supabase.auth.get_user()
user_id = user.user.id if user and user.user else None

if user_id:
    question = st.text_input("Pose ta question sur le droit du travail")

    if st.button("Envoyer"):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Tu es un assistant en droit du travail francais."},
                    {"role": "user", "content": question}
                ]
            )

            reponse_texte = response.choices[0].message.content
            st.success("Reponse de Synapso :")
            st.markdown(reponse_texte)

            # Enregistrement dans Supabase
            data = {
                "user_id": user_id,
                "question": question,
                "answer": reponse_texte
            }
            supabase.table("conversations").insert(data).execute()

        except Exception as e:
            st.error(f"Erreur OpenAI ou Supabase : {e}")
else:
    st.info("Connecte toi pour utiliser Synapso.")
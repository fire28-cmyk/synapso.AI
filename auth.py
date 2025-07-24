# ✅ auth.py
import streamlit as st
from supabase import create_client
from supabase_client import get_supabase_client

supabase = get_supabase_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

def login():
    st.sidebar.subheader("🔐 Connexion / Inscription")
    email = st.sidebar.text_input("Adresse mail", key="email")
    if st.sidebar.button("Se connecter / S'inscrire") and email:
        try:
            supabase.auth.sign_in_with_otp({
                "email": email,
                "options": {
                    "emailRedirectTo": "https://synapso-ai.streamlit.app"
                }
            })
            st.sidebar.success("📩 Un lien de connexion a été envoyé à votre adresse email.")
        except Exception as e:
            st.sidebar.error(f"Erreur d'envoi : {e}")

def get_user():
    user = supabase.auth.get_user()
    if not user.user:
        supabase.auth.refresh_session()
        user = supabase.auth.get_user()
    return user.user

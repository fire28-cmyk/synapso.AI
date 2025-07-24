import streamlit as st
from supabase import create_client

def login():
    st.session_state.authenticated = False
    email = st.text_input("📧 Entrez votre email :", key="email_login")
    if st.button("🔐 Se connecter / S'inscrire"):
        if email:
            supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
            supabase.auth.sign_in_with_otp({"email": email})
            st.success("📩 Un lien de connexion a été envoyé à votre adresse email.")
        else:
            st.warning("❗ Veuillez entrer une adresse email valide.")

def get_user():
    supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
    session = supabase.auth.get_session()
    user = session.user if session and session.user else None
    return user

import streamlit as st
from supabase import create_client

# Connexion à Supabase
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def login():
    st.sidebar.subheader("🔐 Connexion / Inscription")
    email = st.sidebar.text_input("Adresse e-mail", key="email")
    if st.sidebar.button("📩 Recevoir un lien de connexion"):
        res = supabase.auth.sign_in_with_otp({"email": email})
        st.sidebar.success("📬 Lien de connexion envoyé ! Vérifie ta boîte mail.")

def get_user():
    return supabase.auth.get_user().user

import streamlit as st

def login():
    if "user_email" not in st.session_state:
        st.session_state.user_email = st.text_input("✉️ Adresse e-mail")
        if st.button("🔐 Se connecter"):
            st.success(f"Connecté comme {st.session_state.user_email}")

def get_user():
    if "user_email" in st.session_state:
        return {"id": st.session_state.user_email}
    return None

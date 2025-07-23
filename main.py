import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Synapso - IA de conversation", layout="centered")
st.title("🤖 Synapso - Votre Assistant IA")

# Sélection du niveau d'accès utilisateur
user_type = st.sidebar.radio("Choisissez votre accès :", ["Gratuit (GPT-3.5)", "Premium (GPT-4)"])

with st.sidebar:
    st.markdown("---")
    st.markdown("### ✨ Avantages Premium")
    st.markdown("""
- Accès à GPT-4 🤖
- Réponses plus rapides ⚡
- Historique illimité 🧠
- Aucune limite de messages ⛔️
- Support vocal (à venir) 🎤
""")

# Sélection du modèle
if user_type == "Gratuit (GPT-3.5)":
    selected_model = "gpt-3.5-turbo"
else:
    selected_model = "gpt-4"
    st.markdown("### 🔐 Connexion ou création de compte requise pour le mode Premium")
    mode_connexion = st.radio("Choisissez une option :", ["Se connecter", "Créer un compte"])
    email = st.text_input("Adresse e-mail :")
    password = st.text_input("Mot de passe :", type="password")
    if not email or not password:
        st.warning("Veuillez remplir tous les champs pour continuer.")
        st.stop()
    else:
        if mode_connexion == "Se connecter":
            st.success(f"Connecté en tant que : {email}")
        else:
            st.success(f"Compte créé avec succès pour : {email}")

# Historique
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "Tu es une IA polie, amicale et efficace."}]

# Affichage des anciens messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Saisie utilisateur
if prompt := st.chat_input("Posez votre question à Synapso..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = client.chat.completions.create(
            model=selected_model,
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Erreur API : {e}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)


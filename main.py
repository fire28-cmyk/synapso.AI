import streamlit as st
import openai

# Configuration de la clé API OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Titre et configuration de page
st.set_page_config(page_title="Synapso - IA de conversation", layout="centered")
st.title("🤖 Synapso - Votre Assistant IA")

# Choix du type d'accès
user_type = st.sidebar.radio("Choisissez votre accès :", ["Gratuit (GPT-3.5)", "Premium (GPT-4)"])

# Affichage des avantages premium
with st.sidebar:
    st.markdown("---")
    st.markdown("### ✨ Avantages Premium")
    st.markdown("""
- Accès à GPT-4 🤖
- Réponses plus rapides ⚡
- Historique illimité 🧠
- Aucune limite de message ⛔️
- Support vocal à venir 🎤
""")

# Configuration du modèle
model = "gpt-3.5-turbo" if user_type == "Gratuit (GPT-3.5)" else "gpt-4"

# Historique
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Tu es une IA utile, polie, amicale et professionnelle."}
    ]

# Affichage des anciens messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrée utilisateur
if prompt := st.chat_input("Posez votre question à Synapso..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Erreur API : {e}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)

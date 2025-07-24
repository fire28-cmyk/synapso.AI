import streamlit as st
from openai import OpenAI
from auth import login, get_user
from supabase import create_client

# 🔐 Connexion à Supabase
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ✅ Connexion utilisateur
login()
user = get_user()

# ⛔ Accès restreint
if not user:
    st.warning("🛑 Veuillez vous connecter avec votre adresse e-mail pour utiliser Synapso.")
    st.stop()

# ✅ Clé OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 🧠 Interface
st.set_page_config(page_title="Synapso", page_icon="📘")
st.title("📘 Synapso - Assistant Droit du Travail 🇫🇷")
st.markdown("Pose ta question (arrêt maladie, licenciement, congés, etc.)")

mode = st.sidebar.radio("Mode :", ["💬 GPT-3.5", "🔥 GPT-4 Premium"])
st.sidebar.markdown("---")

question = st.text_area("✍️ Votre question ici :")

# Initialiser l'historique
if "historique" not in st.session_state:
    st.session_state.historique = []

if st.button("💬 Envoyer à Synapso"):
    if question.strip() == "":
        st.warning("Merci de poser une question.")
    else:
        model = "gpt-4" if mode == "🔥 GPT-4 Premium" else "gpt-3.5-turbo"

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Tu es un assistant juridique français, mais tu peux répondre aussi à des questions générales avec bienveillance."},
                    {"role": "user", "content": question}
                ]
            )
            reponse_texte = response.choices[0].message.content
            st.session_state.historique.append((question, reponse_texte))
            st.success("✅ Réponse de Synapso :")
            st.markdown(reponse_texte)

            # 💾 Enregistrement Supabase
            try:
                supabase.table("conversations").insert({
                    "user_id": user["id"],
                    "question": question,
                    "answer": reponse_texte
                }).execute()
            except Exception as db_error:
                st.warning("⚠️ Erreur lors de l'enregistrement dans la base.")

        except Exception as e:
            st.error(f"❌ Erreur : {e}")

# 📜 Historique
if st.session_state.historique:
    st.subheader("📜 Historique")
    for i, (q, r) in enumerate(reversed(st.session_state.historique), 1):
        st.markdown(f"**{i}. Question :** {q}")
        st.markdown(f"**Réponse :** {r}")
        st.markdown("---")

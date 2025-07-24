import streamlit as st
from openai import OpenAI
from auth import login, get_user
from supabase_client import get_supabase_client

# 🔌 Connexion Supabase
supabase = get_supabase_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# 🔐 Authentification
login()
user = get_user()

# 🛑 Arrête si pas connecté
if not user:
    st.warning("🛡️ Merci de vous connecter pour utiliser Synapso.")
    st.stop()

# ✅ Clé OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ⚙️ Page
st.set_page_config(
    page_title="Synapso - Assistant Droit du Travail 🇫🇷",
    page_icon="📘",
    layout="wide"
)

# 🔧 Barre latérale
st.sidebar.title("⚙️ Paramètres Synapso")
mode = st.sidebar.radio("Choisissez un mode :", ["💬 GPT-3.5 Gratuit", "🔥 GPT-4 Premium"])
st.sidebar.markdown("---")

# 🧾 Infos mode
if mode == "🔥 GPT-4 Premium":
    st.sidebar.success("✅ **Avantages Premium** :\n\n- GPT-4 Turbo\n- Réponses plus détaillées\n- Moins de limitations\n- Accès prioritaire")
else:
    st.sidebar.info("🆓 **Version Gratuite (GPT-3.5)** :\n\n- Réponses standards\n- Accès limité")

# 🧠 Titre principal
st.title("📘 Synapso - Assistant Droit du Travail 🇫🇷")
st.markdown("Pose ta question (arrêt maladie, licenciement, congés, salaire, etc.)")

# 🧾 Zone texte
question = st.text_area("✍️ Votre question ici :")

# 💬 Historique
if "historique" not in st.session_state:
    st.session_state.historique = []

# 🗑️ Bouton effacer historique
if st.button("🗑️ Effacer l'historique"):
    st.session_state.historique = []

# ▶️ Bouton envoyer
if st.button("💬 Envoyer à Synapso"):
    if question.strip() == "":
        st.warning("❗ Merci de poser une vraie question.")
    else:
        try:
            model = "gpt-4" if mode == "🔥 GPT-4 Premium" else "gpt-3.5-turbo"

            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Tu es un assistant juridique spécialisé en droit du travail français, mais tu peux aussi répondre à des questions générales. Réponds de manière simple et concrète."},
                    {"role": "user", "content": question}
                ]
            )

            reponse_texte = response.choices[0].message.content
            st.session_state.historique.append((question, reponse_texte))

            # ✅ Enregistrer dans Supabase
            supabase.table("conversations").insert({
                "user_id": user["id"],
                "question": question,
                "answer": reponse_texte
            }).execute()

        except Exception as e:
            st.error(f"❌ Une erreur est survenue : {e}")

# 📜 Affichage de l’historique
if st.session_state.historique:
    st.subheader("📜 Historique des réponses")
    for i, (q, r) in enumerate(reversed(st.session_state.historique), 1):
        st.markdown(f"**{i}. Question :** {q}")
        st.markdown(f"**Réponse :** {r}")
        st.markdown("---")

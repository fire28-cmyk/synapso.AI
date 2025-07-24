import streamlit as st
from openai import OpenAI
from auth import login, get_user
from supabase_client import get_supabase_client

# ✅ Initialisation Supabase
supabase = get_supabase_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# 🔐 Connexion utilisateur obligatoire
login()
user = get_user()
if not user:
    st.stop()

# ✅ Clé API OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ⚙️ Configuration de la page
st.set_page_config(
    page_title="Synapso - Assistant Droit du Travail 🇫🇷",
    page_icon="📘",
    layout="wide"
)

# 🔧 Barre latérale
st.sidebar.title("⚙️ Paramètres Synapso")
mode = st.sidebar.radio("Choisissez un mode :", ["💬 GPT-3.5 Gratuit", "🔥 GPT-4 Premium"])
st.sidebar.markdown("---")

# 🧾 Avantages affichés selon le mode
if mode == "🔥 GPT-4 Premium":
    st.sidebar.success("✅ **Avantages Premium** :\n\n- GPT-4 Turbo\n- Réponses plus détaillées\n- Moins de limitations\n- Accès prioritaire")
else:
    st.sidebar.info("🆓 **Version Gratuite (GPT-3.5)** :\n\n- Réponses standards\n- Accès limité")

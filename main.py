import streamlit as st
import openai

# 💡 Mets ta vraie clé OpenAI ici
openai.api_key = "import streamlit as st
import openai

# 💡 Mets ta vraie clé OpenAI ici
openai.api_key = "import streamlit as st
import openai

# 💡 Mets ta vraie clé OpenAI ici
openai.api_key = "import streamlit as st
import openai

# 💡 Mets ta vraie clé OpenAI ici
openai.api_key = "sk-votre_clé_openai_ici"

# ⚙️ Configuration générale de la page
st.set_page_config(
    page_title="Synapso - Assistant Droit du Travail 🇫🇷",
    page_icon="📘",
    layout="wide"
)

# 🔧 Barre latérale
st.sidebar.title("⚙️ Paramètres Synapso")
mode = st.sidebar.radio("Choisissez un mode :", ["💬 GPT-3.5 Gratuit", "🔥 GPT-4 Premium"])
st.sidebar.markdown("---")

# 🧾 Affichage des avantages selon le mode
if mode == "🔥 GPT-4 Premium":
    st.sidebar.success("✅ **Avantages Premium** :\n\n- GPT-4 Turbo\n- Réponses plus détaillées\n- Moins de limitations\n- Accès prioritaire")
else:
    st.sidebar.info("🆓 **Version Gratuite (GPT-3.5)** :\n\n- Réponses standards\n- Accès limité")

# 🧠 Titre principal
st.title("📘 Synapso - Assistant Droit du Travail 🇫🇷")
st.markdown("Pose ta question (arrêt maladie, licenciement, congés, salaire, etc.)")

# 🗨️ Zone de question
question = st.text_area("✍️ Votre question ici :")

# ▶️ Bouton d'envoi
if st.button("💬 Envoyer à Synapso"):
    if question.strip() == "":
        st.warning("❗ Merci de poser une vraie question.")
    else:
        try:
            model = "gpt-4" if mode == "🔥 GPT-4 Premium" else "gpt-3.5-turbo"

            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Tu es un assistant juridique spécialisé en droit du travail français. Réponds de manière simple et concrète aux salariés."},
                    {"role": "user", "content": question}
                ]
            )

            # ✅ Affichage de la réponse
            st.success("✅ Réponse de Synapso :")
            st.markdown(response["choices"][0]["message"]["content"])

        except Exception as e:
            st.error(f"❌ Une erreur est survenue : {e}")
"

# ⚙️ Configuration générale de la page
st.set_page_config(
    page_title="Synapso - Assistant Droit du Travail 🇫🇷",
    page_icon="📘",
    layout="wide"
)

# 🔧 Barre latérale
st.sidebar.title("⚙️ Paramètres Synapso")
mode = st.sidebar.radio("Choisissez un mode :", ["💬 GPT-3.5 Gratuit", "🔥 GPT-4 Premium"])
st.sidebar.markdown("---")

# 🧾 Affichage des avantages selon le mode
if mode == "🔥 GPT-4 Premium":
    st.sidebar.success("✅ **Avantages Premium** :\n\n- GPT-4 Turbo\n- Réponses plus détaillées\n- Moins de limitations\n- Accès prioritaire")
else:
    st.sidebar.info("🆓 **Version Gratuite (GPT-3.5)** :\n\n- Réponses standards\n- Accès limité")

# 🧠 Titre principal
st.title("📘 Synapso - Assistant Droit du Travail 🇫🇷")
st.markdown("Pose ta question (arrêt maladie, licenciement, congés, salaire, etc.)")

# 🗨️ Zone de question
question = st.text_area("✍️ Votre question ici :")

# ▶️ Bouton d'envoi
if st.button("💬 Envoyer à Synapso"):
    if question.strip() == "":
        st.warning("❗ Merci de poser une vraie question.")
    else:
        try:
            model = "gpt-4" if mode == "🔥 GPT-4 Premium" else "gpt-3.5-turbo"

            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Tu es un assistant juridique spécialisé en droit du travail français. Réponds de manière simple et concrète aux salariés."},
                    {"role": "user", "content": question}
                ]
            )

            # ✅ Affichage de la réponse
            st.success("✅ Réponse de Synapso :")
            st.markdown(response["choices"][0]["message"]["content"])

        except Exception as e:
            st.error(f"❌ Une erreur est survenue : {e}")
"

# ⚙️ Configuration générale de la page
st.set_page_config(
    page_title="Synapso - Assistant Droit du Travail 🇫🇷",
    page_icon="📘",
    layout="wide"
)

# 🔧 Barre latérale
st.sidebar.title("⚙️ Paramètres Synapso")
mode = st.sidebar.radio("Choisissez un mode :", ["💬 GPT-3.5 Gratuit", "🔥 GPT-4 Premium"])
st.sidebar.markdown("---")

# 🧾 Affichage des avantages selon le mode
if mode == "🔥 GPT-4 Premium":
    st.sidebar.success("✅ **Avantages Premium** :\n\n- GPT-4 Turbo\n- Réponses plus détaillées\n- Moins de limitations\n- Accès prioritaire")
else:
    st.sidebar.info("🆓 **Version Gratuite (GPT-3.5)** :\n\n- Réponses standards\n- Accès limité")

# 🧠 Titre principal
st.title("📘 Synapso - Assistant Droit du Travail 🇫🇷")
st.markdown("Pose ta question (arrêt maladie, licenciement, congés, salaire, etc.)")

# 🗨️ Zone de question
question = st.text_area("✍️ Votre question ici :")

# ▶️ Bouton d'envoi
if st.button("💬 Envoyer à Synapso"):
    if question.strip() == "":
        st.warning("❗ Merci de poser une vraie question.")
    else:
        try:
            model = "gpt-4" if mode == "🔥 GPT-4 Premium" else "gpt-3.5-turbo"

            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Tu es un assistant juridique spécialisé en droit du travail français. Réponds de manière simple et concrète aux salariés."},
                    {"role": "user", "content": question}
                ]
            )

            # ✅ Affichage de la réponse
            st.success("✅ Réponse de Synapso :")
            st.markdown(response["choices"][0]["message"]["content"])

        except Exception as e:
            st.error(f"❌ Une erreur est survenue : {e}")
"

# ⚙️ Configuration générale de la page
st.set_page_config(
    page_title="Synapso - Assistant Droit du Travail 🇫🇷",
    page_icon="📘",
    layout="wide"
)

# 🔧 Barre latérale
st.sidebar.title("⚙️ Paramètres Synapso")
mode = st.sidebar.radio("Choisissez un mode :", ["💬 GPT-3.5 Gratuit", "🔥 GPT-4 Premium"])
st.sidebar.markdown("---")

# 🧾 Affichage des avantages selon le mode
if mode == "🔥 GPT-4 Premium":
    st.sidebar.success("✅ **Avantages Premium** :\n\n- GPT-4 Turbo\n- Réponses plus détaillées\n- Moins de limitations\n- Accès prioritaire")
else:
    st.sidebar.info("🆓 **Version Gratuite (GPT-3.5)** :\n\n- Réponses standards\n- Accès limité")

# 🧠 Titre principal
st.title("📘 Synapso - Assistant Droit du Travail 🇫🇷")
st.markdown("Pose ta question (arrêt maladie, licenciement, congés, salaire, etc.)")

# 🗨️ Zone de question
question = st.text_area("✍️ Votre question ici :")

# ▶️ Bouton d'envoi
if st.button("💬 Envoyer à Synapso"):
    if question.strip() == "":
        st.warning("❗ Merci de poser une vraie question.")
    else:
        try:
            model = "gpt-4" if mode == "🔥 GPT-4 Premium" else "gpt-3.5-turbo"

            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Tu es un assistant juridique spécialisé en droit du travail français. Réponds de manière simple et concrète aux salariés."},
                    {"role": "user", "content": question}
                ]
            )

            # ✅ Affichage de la réponse
            st.success("✅ Réponse de Synapso :")
            st.markdown(response["choices"][0]["message"]["content"])

        except Exception as e:
            st.error(f"❌ Une erreur est survenue : {e}")

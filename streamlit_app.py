
import streamlit as st
from openai import OpenAI
from supabase import create_client, Client

# --- API keys from secrets ---
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# --- Create clients ---
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
client = OpenAI(api_key=OPENAI_API_KEY)

# --- UI ---
st.set_page_config(page_title="Synapso - Droit du Travail")
st.title("Synapso - Assistant Droit du Travail")

# --- Authentication ---
email = st.text_input("Ton adresse email")

if st.button("Se connecter"):
    try:
        supabase.auth.sign_in_with_otp({"email": email})
        st.success("Mail de connexion envoye")
    except Exception as e:
        error_msg = str(e).encode("ascii", errors="ignore").decode()
        st.error("Erreur envoi : {}".format(error_msg))

user = supabase.auth.get_user()
user_id = user.user.id if user and user.user else None

if user_id:
    question = st.text_input("Pose ta question")

    if st.button("Envoyer"):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Tu es un assistant en droit du travail francais"},
                    {"role": "user", "content": question}
                ]
            )

            reponse_texte = response.choices[0].message.content
            st.success("Reponse :")
            st.markdown(reponse_texte)

            data = {
                "user_id": user_id,
                "question": question,
                "answer": reponse_texte
            }
            supabase.table("conversations").insert(data).execute()

        except Exception as e:
            error_msg = str(e).encode("ascii", errors="ignore").decode()
            st.error("Erreur OpenAI ou Supabase : {}".format(error_msg))
else:
    st.info("Connecte toi pour utiliser Synapso")

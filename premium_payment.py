import streamlit as st
import stripe

# Configuration Stripe (test)
stripe.api_key = st.secrets["STRIPE_SECRET_KEY"]
STRIPE_PUBLIC_KEY = st.secrets["STRIPE_PUBLIC_KEY"]

def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': 'Abonnement Synapso Premium',
                    },
                    'unit_amount': 1000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8501?payment=success',
            cancel_url='http://localhost:8501?payment=cancel',
        )
        return checkout_session.url
    except Exception as e:
        st.error(f"Erreur Stripe : {e}")
        return None

st.set_page_config(page_title="Paiement Synapso Premium")
st.title("🔐 Passer à Synapso Premium")

st.markdown("""
### Profitez de tous les avantages :
- GPT-4 🤖  
- Réponses rapides ⚡  
- Historique illimité 🧠  
- Aucun quota de messages ⛔️  
- Support vocal à venir 🎤
""")

if st.button("💳 Payer 10€ et débloquer Premium"):
    checkout_url = create_checkout_session()
    if checkout_url:
        st.success("Redirection vers Stripe...")
        st.markdown(f"[Cliquez ici si rien ne se passe]({checkout_url})", unsafe_allow_html=True)

query = st.query_params
if query.get("payment") == ["success"]:
    st.success("✅ Paiement validé. Vous êtes maintenant Premium.")
elif query.get("payment") == ["cancel"]:
    st.warning("❌ Paiement annulé.")

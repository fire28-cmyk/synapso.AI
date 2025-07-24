from supabase import create_client

# ✅ Fonction pour retourner un client Supabase sans créer une boucle infinie
def get_supabase_client(url, key):
    return create_client(url, key)

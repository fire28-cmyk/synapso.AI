from supabase import create_client as supabase_create

def get_supabase_client(url, key):
    return supabase_create(url, key)

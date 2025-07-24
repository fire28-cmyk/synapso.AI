from supabase import create_client as supabase_create

def create_client(url, key):
    return supabase_create(url, key)

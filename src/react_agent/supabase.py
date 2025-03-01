import os
from dotenv import load_dotenv
from supabase import create_client
from langchain_google_genai import GoogleGenerativeAIEmbeddings
load_dotenv(dotenv_path=".env")
# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase_client = create_client(supabase_url, supabase_key)
# Initialize Gemini embeddings
gemini_embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY"))

async def search_dresses(query, match_count=3):
    """
    Search for dresses using similarity search with Gemini embeddings
    
    Args:
        query (str): Search query
        match_count (int): Number of matches to return
        
    Returns:
        list: List of matching dress items
    """
    # Generate embedding for the search query
    query_embedding = gemini_embeddings.embed_query(query)
    
    # Perform similarity search using Supabase's pgvector extension
    response = supabase_client.rpc(
        'viva_match_dresses',
        {
            'query_embedding': query_embedding,
            'match_threshold': 0.5,  # Adjust this threshold as needed
            'match_count': match_count
        }
    ).execute()
    
    return response.data
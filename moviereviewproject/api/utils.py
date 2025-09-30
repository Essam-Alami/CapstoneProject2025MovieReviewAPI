import requests

TMDB_API_KEY = "YOUR_TMDB_API_KEY"
TMDB_BASE_URL = "https://api.themoviedb.org/3"

def fetch_movies(query="popular", page=1):
    """
    Fetch movies from TMDB.
    query can be "popular", "top_rated", "now_playing", etc.
    """
    url = f"{TMDB_BASE_URL}/movie/{query}?api_key={TMDB_API_KEY}&language=en-US&page={page}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []

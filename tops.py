import spotipy
from spotipy.oauth2 import SpotifyOAuth

# using dotenv, create environment variables from the local .env file
# access those environment variables with dotenv_values 
from dotenv import dotenv_values
ENV_VARS = dotenv_values()
SPOTIPY_CLIENT_ID = ENV_VARS['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = ENV_VARS['SPOTIPY_CLIENT_SECRET']
REDIRECT_URI = ENV_VARS['REDIRECT_URI']

def print_User_Top_Artists():
    results = sp.current_user_top_artists(offset=0, time_range='long_term')
    for idx, artist in enumerate(results['items']):
        artist_name = artist['name']
        print(f"{idx+1}: {artist_name}")

def main():
    print_User_Top_Artists()

if __name__ == '__main__':
    scope_top = "user-top-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIPY_CLIENT_ID,
                                               SPOTIPY_CLIENT_SECRET,
                                               REDIRECT_URI,
                                              scope=scope_top))
    main()

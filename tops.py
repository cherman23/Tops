import spotipy
from spotipy.oauth2 import SpotifyOAuth

# using dotenv, create environment variables from the local .env file
# access those environment variables with dotenv_values 
from dotenv import dotenv_values
ENV_VARS = dotenv_values()
SPOTIPY_CLIENT_ID = ENV_VARS['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = ENV_VARS['SPOTIPY_CLIENT_SECRET']
REDIRECT_URI = ENV_VARS['REDIRECT_URI']

def print_User_Top_Artists(term):
    results = sp.current_user_top_artists(offset=0, time_range=term)
    for idx, artist in enumerate(results['items']):
        artist_name = artist['name']
        print(f"{idx+1}: {artist_name}")

def print_User_Top_Tracks(term):
    tracks = sp.current_user_top_tracks(offset=0, time_range=term)
    for idx, track in enumerate(tracks['items']):
        track_name = track['name']
        print(f"{idx+1}: {track_name}")

def getTerm():
    term = input("Would you prefer short, medium, or long term results? (S , M, or L): ")
    if term.lower() == "s": return 'short_term'
    elif term.lower() == "m": return 'medium_term'
    elif term.lower() == "l": return 'long_term'
    else:
        print("Please enter a valid response.")
        getTerm()

def main():
    Text = input("Would you like to see your top tracks or artists? (T or A): ")
    Artists = "a"
    Tracks = "t"
    term = getTerm()
    if Text.lower() == Tracks:
        print_User_Top_Tracks(term)
    elif  Text.lower() == Artists:
        print_User_Top_Artists(term)
    else:
        print("Please enter a valid response.")
        main()


if __name__ == '__main__':
    scope_top = "user-top-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIPY_CLIENT_ID,
                                                    SPOTIPY_CLIENT_SECRET,
                                                    REDIRECT_URI,
                                                    scope=scope_top))
    main()

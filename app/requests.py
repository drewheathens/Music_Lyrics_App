import urllib.request, json
from .models import Artist

# Getting api key
api_key = None
# Getting the lyrics base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['LYRICS_API_KEY']
    base_url = app.config['LYRICS_API_BASE_URL']

def search_artist(artist_name, track_name):
    search_artist_url = 'https://orion.apiseeds.com/api/music/lyric/artist{}/track{}?api_key={}'.format(api_key,artist_name,track_name)
    with urllib.request.urlopen(search_artist_url) as url:
        search_artist_data = url.read()
        search_artist_response = json.loads(search_artist_data)

        search_artist_results = None

        if search_artist_response['results']:
            search_artist_list = search_artist_response['results']
            search_artist_results = process_results(search_artist_list)


    return search_artist_results  
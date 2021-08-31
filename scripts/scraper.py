import json

import spotipy
from lyricsgenius import Genius
from requests.exceptions import HTTPError, Timeout
from spotipy.oauth2 import SpotifyClientCredentials

from schlag.config import (
    DATA_DIR,
    GENIUS_TOKEN,
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET,
)

genius = Genius(GENIUS_TOKEN)
genius.skip_non_songs = True
genius.timeout = 10
genius.retries = 3

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
    )
)


def scrape_genius_artist(artist_name, artist_id=None, num_songs=7):
    try:
        artist = genius.search_artist(
            artist_name,
            max_songs=num_songs,
            artist_id=artist_id,
            include_features=False,
            get_full_info=False,
        )

        raw_dir = DATA_DIR / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)

        for song in artist.songs:
            song.save_lyrics(
                str(raw_dir / str(song.id)), sanitize=False, overwrite=True
            )
    except HTTPError as e:
        print(e)
    except Timeout:
        print("Timeout")
    except Exception as e:
        print(e)


def scrape_spotify_playlist(playlist_id):
    play = sp.playlist(playlist_id)

    songs = []
    for item in play["tracks"]["items"]:
        if not item["track"]["track"]:
            continue
        songs.append(
            {
                "artists": [artist["name"] for artist in item["track"]["artists"]],
                "name": item["track"]["name"],
            }
        )

    return songs


def main():
    # Scrape playlists
    playlists = [
        "1UcU4Ch2OMiZwvtTacewwZ",
        "0GL84sYMUkLQDZVgA4Nw2G",
        "1J2vYkrZaRh9mPoRAiVVmU",
        "36MEiH6qLMCAE0uDH8WnjZ",
    ]
    songs = []
    for playlist_id in playlists:
        songs.extend(scrape_spotify_playlist(playlist_id))

    # Scrape songs from artists
    artist_id_pairs = {  # Needed for artists which aren't easily found on Genius
        "Pur": 124102,
        "Fantasy": 133347,
        "Neon": 2565624,
        "Nockis": 376822,
        "Henry Valentino": 348494,
    }

    artists = {  # A starting set of artists from which we want to include songs
        "Michelle & Matthias Reim",
        "Helene Fischer",
        "Andreas Gabalier",
        "Kerstin Ott",
        "Mickie Krause",
        "Markus Becker",
        "Peter Wackel",
        "Tobee",
        "Lorenz Büffel",
        "Ikke Hüftgold",
        "Tommy Tellerlift & Die Fangzauner Schneebrunzer",
        "Ute Freudenberg",
    }
    artists_skip = {  # Not all artists are found on Genius
        "Michelle",
        "Max Weidner",
        "Jenice",
        "Feuerland",
        "Nicole",
        "Andreas Fulterer",
        "Anton",
        "Lyane Hegemann",
        "Daniela Dilow",
        "Heinz Koch",
        "Pat",
        "EAZY CHRIZ",
        "Frank Lukas",
        "Loona",
        "J. P. Love",
        "Mike Bauhaus",
        "Ute Freudenberg & Christian Lais",
        "The Baseballs",
        "Buddy",
    }

    # Artists we already know we want songs from
    for artist_name in artists:
        print()
        print(artist_name)
        scrape_genius_artist(artist_name, num_songs=15)

    # Artists pulled from playlists
    artists = {song["artists"][0] for song in songs} - artists
    print(artists)
    print("Number of artists", len(artists))
    for artist_name in artists:
        print()
        print(artist_name)
        if artist_name in artist_id_pairs or artist_name in artists_skip:
            print("Skipping", artist_name)
            continue
        scrape_genius_artist(artist_name)

    # Weird mapping in genius
    for artist_name, artist_id in artist_id_pairs.items():
        print()
        print(artist_name)
        scrape_genius_artist(artist_name, artist_id=artist_id)


if __name__ == "__main__":
    main()

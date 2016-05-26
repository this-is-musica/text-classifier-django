import os
import django
import json
import pprint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'text_classifier.settings')
django.setup()

from money_maker.models import Song


print(os.path.isdir("../data/music"))


def read_lyrics(music_folder="../data/music/"):
    genre_folders = os.listdir(music_folder)
    ided_songs = []
    for folder in genre_folders:
        with open(os.path.join(music_folder, folder, '1-20.json')) as jsonfile20:
            genre20 = json.load(jsonfile20)
            for song_data in genre20['results']:
                song_lyrics = []
                for lyrics in song_data['collection1']:
                    song_lyrics.append(lyrics['SongLyric'])
                this_song = {}
                this_song['lyrics'] = '\n'.join(song_lyrics)
                this_song['genre'] = folder
                ided_songs.append(this_song)
        with open(os.path.join(music_folder, folder, '21-100.json')) as jsonfile80:
            genre80 = json.load(jsonfile80)
            for song_data in genre80['results']:
                song_lyrics = []
                for lyrics in song_data['collection1']:
                    song_lyrics.append(lyrics['SongLyric'])
                this_song = {}
                this_song['lyrics'] = '\n'.join(song_lyrics)
                this_song['genre'] = folder
                ided_songs.append(this_song)
    return ided_songs

def create_entries():
    ided_songs = read_lyrics()
    for item in ided_songs:
        print(item)
        _, created = Song.objects.get_or_create(
            genre=item['genre'],
            lyrics=item['lyrics'],
        )


create_entries()

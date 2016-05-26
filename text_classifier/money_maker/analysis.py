from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
# from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import os
import functools


@functools.lru_cache(maxsize=2)
def _make_classifier_and_counter(music_folder="../data/music/"):
    genre_folders = os.listdir(music_folder)
    ided_songs = []
    for folder in genre_folders:
        genre20 = pd.read_json(os.path.join(music_folder, folder, '1-20.json'))
        for song_data in genre20.results:
            song_lyrics = []
            for lyrics in song_data['collection1']:
                song_lyrics.append(lyrics['SongLyric'])
            this_song = {}
            this_song['lyrics'] = '\n'.join(song_lyrics)
            this_song['genre'] = folder
            ided_songs.append(this_song)
        genre80 = pd.read_json(os.path.join(music_folder, folder, '21-100.json'))
        for song_data in genre80.results:
            song_lyrics = []
            for lyrics in song_data['collection1']:
                song_lyrics.append(lyrics['SongLyric'])
            this_song = {}
            this_song['lyrics'] = '\n'.join(song_lyrics)
            this_song['genre'] = folder
            ided_songs.append(this_song)
    song_list = [song['lyrics'] for song in ided_songs]
    genre_list = [song['genre'] for song in ided_songs]
    word_counter = TfidfVectorizer()
    counted_by_words = word_counter.fit_transform(song_list)
    # classifier_by_words = MultinomialNB()
    forest_classifier = RandomForestClassifier(n_estimators=50)
    forest_classifier.fit(counted_by_words, genre_list)
    # classifier_by_words.fit(counted_by_words, genre_list)
    # print(word_counter.get_feature_names())
    return (forest_classifier, word_counter)


def classify_lyrics(lyrics):
    classifier, counter = _make_classifier_and_counter()
    return str(classifier.predict(counter.transform([lyrics])))

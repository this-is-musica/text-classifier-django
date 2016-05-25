from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import os
# songs = [{"lyrics": """You can taste the dishonesty
# It's all over your breath as you pass it off so cavalier
# But even that's a test
# Constantly aware of it all
# My lonely ear
# Pressed against the walls of your world
#
# Prayin' to catch you whispering
# I'm prayin' you catch me listening
# I'm prayin' to catch you whispering
# I'm prayin' you catch me
# I'm prayin' to catch you whispering
# I'm prayin' you catch me listening
# I'm prayin' you catch me
#
# Nothing else ever seems to hurt like the smile on your face
# When it's only in my memory
# It don't hit me quite the same
# Maybe it's a cause for concern
# But I'm not at ease
# Keeping my head to the curb
#
# Prayin' to catch you whispering
# I'm prayin' you catch me listening
# I'm prayin' to catch you whispering
# I'm prayin' you catch me
# I'm prayin' you catch me
# I'm prayin' you catch me
# I'm prayin' you catch me""", "artist": "BEYONCE KNOWLES"},
#          {"lyrics": """Yee-haw
# Oh, oh, oh
# Texas, Texas (oh, oh, oh) Texas
#
# Came into this world
# Daddy's little girl
# And daddy made a soldier out of me
# Oh, oh, oh
# Daddy made me dance
# And daddy held my hand
# Oh, oh, oh
# And daddy liked his whisky with his tea
# And we rode motorcycles
# Blackjack, classic vinyl
# Tough girl is what I had to be
#
# He said take care of your mother
# Watch out for your sister
# Oh, and that's when he gave to me...
#
# With his gun, with his head held high
# He told me not to cry
# Oh, my daddy said shoot
# Oh, my daddy said shoot
# With his right hand on his rifle
# He swore it on the bible
# My daddy said shoot
# Oh, my daddy said shoot
# He held me in his arms
# And he taught me to be strong
# He told me when he's gone
# Here's what you do
# When trouble comes to town
# And men like me come around
# Oh, my daddy said shoot
# Oh, my daddy said shoot
# Oh, oh, oh
#
# Daddy made me fight
# It wasn't always right
# But he said girl it's your second amendment, oh, oh, oh
# He always played it cool
# But daddy was no fool
# And right before he died he said remember...
#
# He said take care of your mother
# Watch out for your sister
# And that's when daddy looked at me...
#
# With his gun, with his head held high
# He told me not to cry
# Oh, my daddy said shoot
# Oh, my daddy said shoot
# With his right hand on his rifle
# He swore it on the bible
# My daddy said shoot
# Oh, my daddy said shoot
# He held me in his arms
# And he taught me to be strong
# He told me when he's gone
# Here's what you do
# When trouble comes to town
# And men like me come around
# Oh, my daddy said shoot
# Oh, my daddy said shoot
# Oh, oh, oh
# Oh, oh, oh
#
# My daddy warned me about men like you
# He said baby girl he's playing you
# He's playing you
# My daddy warned me about men like you
# He said baby girl he's playing you
# He's playing you
# Cause when trouble comes in town
# And men like me come around
# Oh, my daddy said shoot
# Oh, my daddy said shoot
# Cause when trouble comes to town
# And men like me come around
# Oh, my daddy said shoot
# Oh, my daddy said shoot
# (Good job Bey, hahaha)""", "artist": "BEYONCE KNOWLES"},
#          {"lyrics": """Stay in the shadows
# Cheer at the gallows
# This is a round up
#
# This is a low flying panic attack
# Sing a song on the jukebox that goes
#
# Burn the witch
# Burn the witch
# We know where you live
#
# Red crosses on wooden doors
# And if you float you burn
# Loose talk around tables
# Abandon all reason
# Avoid all eye contact
# Do not react
# Shoot the messengers
#
# This is a low flying panic attack
# Sing the song of sixpence that goes
#
# Burn the witch
# Burn the witch
# We know where you live
# We know where you live""", "artist": "RADIOHEAD"}]
#
# sample = """She don't gotta give it up, she professional
# She mixing up that Ace with that Hennessy
# She love the way it tastes, that's her recipe
# Rushing through her veins like it's ecstasy, oh no
# She already made enough but she'll never leave"""
#
# sample2 = """This is a low flying panic attack
# Sing a song on the jukebox that goes
#
# Burn the witch
# Burn the witch
# We know where you live
# """


music_folder = "../data/music/"
genre_folders = os.listdir(music_folder)
ided_songs = []
for folder in genre_folders:
    print(folder)
    try:
        genre20 = pd.read_json(os.path.join(music_folder, folder, '1-20.json'))
        for song_data in genre20.results:
            song_lyrics = []
            for lyrics in song_data['collection1']:
                song_lyrics.append(lyrics['SongLyric'])
            this_song = {}
            this_song['lyrics'] = '\n'.join(song_lyrics)
            this_song['genre'] = folder
            ided_songs.append(this_song)
    except TypeError:
        pass
    try:
        genre80 = pd.read_json(os.path.join(music_folder, folder, '21-100.json'))
        for song_data in genre80.results:
            song_lyrics = []
            for lyrics in song_data['collection1']:
                song_lyrics.append(lyrics['SongLyric'])
            this_song = {}
            this_song['lyrics'] = '\n'.join(song_lyrics)
            this_song['genre'] = folder
            ided_songs.append(this_song)
    except  TypeError:
        pass
print(ided_songs)
print(len(ided_songs))
        # print(i['collection1'])
#     song_list = []
#     for i in songs.results:
#         this_song = []
#         for j in i['collection1']:
#             this_song.append(j["property2"])
#         song_list.append(''.join(this_song[1:]))
#
# disney =  [0] * 20
# disney[6] = 1
# disney[16] = 1
# disney[19] = 1
# # print(song_list)
#
# word_counter = TfidfVectorizer()
# counted_by_words = word_counter.fit_transform(song_list)
# classifier_by_words = MultinomialNB()
#
# classifier_by_words.fit(counted_by_words, disney)
# # print(classifier_by_words.score(counted_by_words, disney))
#
# out = word_counter.transform([""" a flight on my chopper, cause I slay\nDrop him off at the mall, let him buy some J's, let him shop up, cause I slay\nI might get your song ""","""cry to the blue corn moon\nFor whether we are white or copper skinned\nWe need to sing with all the voices of the mountains\nWe need to paint with all the colors of the windYou can own the Earth and still\nAll you'll own is Earth until\nYou can paint with all the colors of the wind""","Princess"])
# print(classifier_by_words.predict_proba(out))
# # print(out.shape)
# #
# # print(out[0,:].tolist())
# for i in out:
#     for j in i:
#         for k in j:
#             pass
#             # print(k)

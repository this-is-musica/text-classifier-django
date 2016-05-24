from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

songs = [{"lyrics": """You can taste the dishonesty
It's all over your breath as you pass it off so cavalier
But even that's a test
Constantly aware of it all
My lonely ear
Pressed against the walls of your world

Prayin' to catch you whispering
I'm prayin' you catch me listening
I'm prayin' to catch you whispering
I'm prayin' you catch me
I'm prayin' to catch you whispering
I'm prayin' you catch me listening
I'm prayin' you catch me

Nothing else ever seems to hurt like the smile on your face
When it's only in my memory
It don't hit me quite the same
Maybe it's a cause for concern
But I'm not at ease
Keeping my head to the curb

Prayin' to catch you whispering
I'm prayin' you catch me listening
I'm prayin' to catch you whispering
I'm prayin' you catch me
I'm prayin' you catch me
I'm prayin' you catch me
I'm prayin' you catch me""", "artist": "BEYONCE KNOWLES"},
         {"lyrics": """Yee-haw
Oh, oh, oh
Texas, Texas (oh, oh, oh) Texas

Came into this world
Daddy's little girl
And daddy made a soldier out of me
Oh, oh, oh
Daddy made me dance
And daddy held my hand
Oh, oh, oh
And daddy liked his whisky with his tea
And we rode motorcycles
Blackjack, classic vinyl
Tough girl is what I had to be

He said take care of your mother
Watch out for your sister
Oh, and that's when he gave to me...

With his gun, with his head held high
He told me not to cry
Oh, my daddy said shoot
Oh, my daddy said shoot
With his right hand on his rifle
He swore it on the bible
My daddy said shoot
Oh, my daddy said shoot
He held me in his arms
And he taught me to be strong
He told me when he's gone
Here's what you do
When trouble comes to town
And men like me come around
Oh, my daddy said shoot
Oh, my daddy said shoot
Oh, oh, oh

Daddy made me fight
It wasn't always right
But he said girl it's your second amendment, oh, oh, oh
He always played it cool
But daddy was no fool
And right before he died he said remember...

He said take care of your mother
Watch out for your sister
And that's when daddy looked at me...

With his gun, with his head held high
He told me not to cry
Oh, my daddy said shoot
Oh, my daddy said shoot
With his right hand on his rifle
He swore it on the bible
My daddy said shoot
Oh, my daddy said shoot
He held me in his arms
And he taught me to be strong
He told me when he's gone
Here's what you do
When trouble comes to town
And men like me come around
Oh, my daddy said shoot
Oh, my daddy said shoot
Oh, oh, oh
Oh, oh, oh

My daddy warned me about men like you
He said baby girl he's playing you
He's playing you
My daddy warned me about men like you
He said baby girl he's playing you
He's playing you
Cause when trouble comes in town
And men like me come around
Oh, my daddy said shoot
Oh, my daddy said shoot
Cause when trouble comes to town
And men like me come around
Oh, my daddy said shoot
Oh, my daddy said shoot
(Good job Bey, hahaha)""", "artist": "BEYONCE KNOWLES"},
         {"lyrics": """Stay in the shadows
Cheer at the gallows
This is a round up

This is a low flying panic attack
Sing a song on the jukebox that goes

Burn the witch
Burn the witch
We know where you live

Red crosses on wooden doors
And if you float you burn
Loose talk around tables
Abandon all reason
Avoid all eye contact
Do not react
Shoot the messengers

This is a low flying panic attack
Sing the song of sixpence that goes

Burn the witch
Burn the witch
We know where you live
We know where you live""", "artist": "RADIOHEAD"}]

sample = """She don't gotta give it up, she professional
She mixing up that Ace with that Hennessy
She love the way it tastes, that's her recipe
Rushing through her veins like it's ecstasy, oh no
She already made enough but she'll never leave"""

sample2 = """This is a low flying panic attack
Sing a song on the jukebox that goes

Burn the witch
Burn the witch
We know where you live
"""

word_counter = TfidfVectorizer()
counted_by_words = word_counter.fit_transform([song['lyrics'] for song in songs])
classifier_by_words = MultinomialNB()

classifier_by_words.fit(counted_by_words, [song['artist'] for song in songs])
print(classifier_by_words.score(counted_by_words, [song['artist'] for song in songs]))

print(classifier_by_words.predict(word_counter.transform([sample,sample2])))

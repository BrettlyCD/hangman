#pip install random-word
#pip intall pyyaml

from random_word import RandomWords
r = RandomWords()

wordList = r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minLength=4, maxLength=12, limit=100)

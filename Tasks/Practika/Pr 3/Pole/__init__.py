import sys
import os

sys.path.append(os.path.dirname(__file__))

from .Game import *
from .File import *
from .New_game import *

words = get_words()
while True:
    word = find_word(words)
    record = play(word)
    new_record(record)
    if not con_game(words):
        break
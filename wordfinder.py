"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    ...

    def __init__(self, words):
        word_file = open(words)
        self.list = self.parse(word_file)
        print(f"{len(self.list)} words read")

    def parse(self, word_file):
        return [word.strip() for word in word_file]

    def random(self):
        return random.choice(self.list)

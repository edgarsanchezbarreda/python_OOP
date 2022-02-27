import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        file_path = open(path)
        self.words = self.parse(file_path)

        print(f"{len(self.words)} words read!")
        """Reads the file that is passed in, and print the number of lines that were read"""
    
    def parse(self, file_path):
        """Returns all lines from the file that is passed in without the 'new line' character"""
        return [word.strip() for word in file_path]

    def random(self):
        """Returns a random word from the file"""
        return random.choice(self.words)

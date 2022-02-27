from wordfinder import WordFinder
"""Imports the WordFinder class"""

class SpecialWordFinder(WordFinder):
    """Creates a new instance of WordFinder class"""
    def __init__(self, path):
        super().__init__(path)

    def parse(self, file_path):
        """Selects all lines from file that is passed in that do not contain '#' or are empty strings"""
        return [word.strip() for word in file_path if word.strip() and not word.startswith('#')]
class SerialGenerator:
    """
    A class that generates any number that is passed in, and contains methods to increment and reset the number.

    Attributes
    -----------
    start: The starting number that is passed in.

    count: A counter that is incremented by 1 when the 'generate' method is called.
    """
    def __init__(self, start):
        self.start = start
        self.count = 0

    def __repr__(self):
        """Displays attributes"""
        print(f"<SerialGenerator start = {self.start}>")

    def generate(self):
        """A method that increments the counter variable by 1, and is added to the initial start parameter"""
        print(self.start + self.count)
        self.count += 1
        
    def reset(self):
        """A method that subtracts the current "start" variable by the current "count" variable, and returns the original "start" variable """
        self.start - self.count
        self.count = 0
        print(self.start)



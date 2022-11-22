"""Band class"""


class Band:
    """Band class"""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of band"""
        musicians_string = [str(musician) for musician in self.musicians]
        musicians_string = ", ".join(musicians_string)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Append musician to members"""
        self.musicians.append(musician)

    def play(self):
        """Make each member in members play"""
        playing_musicians = [musician.play() for musician in self.musicians]
        playing_musicians = "\n".join(playing_musicians)
        return playing_musicians

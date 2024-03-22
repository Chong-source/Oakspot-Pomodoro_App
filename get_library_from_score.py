class Libraries:
    """A data class that stores the scores of each """
    quiet: int
    bright: int
    charger: int
    crowdedness: int

    def __init__(self, quiet, bright, charger, crowdedness) -> None:
        self.quiet = quiet
        self.bright = bright
        self.charger = charger
        self.crowdedness = crowdedness

    def get_score(self, quiet_score, bright_score, charger_score, crowdedness_score) -> float:
        """Calculates the difference between this library's ratings and the user's """


class User:
    """"""
    quiet: int
    bright: int
    charger: int
    crowdedness: int
    libraries: list[Libraries]

    def __init__(self, quiet, bright, charger, crowdedness, libraries) -> None:
        self.quiet = quiet
        self.bright = bright
        self.charger = charger
        self.crowdedness = crowdedness
        self.libraries = libraries
    def get_best_library(self):

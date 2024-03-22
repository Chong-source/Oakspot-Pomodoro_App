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


def load() -> dict[str, Libraries]:
    """ reads csv file with library ratings and stores them in a variable"""
    libraries = {}
    
    with open(book_names_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            libraries[row[0]] = library(row[1], row[2], row[3], row[4])

    return libraries

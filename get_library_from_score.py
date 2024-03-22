class Libraries:
    """A data class that stores the scores of each """
    name: str
    quiet: int
    bright: int
    charger: int
    crowdedness: int

    def __init__(self, name, quiet, bright, charger, crowdedness) -> None:
        self.name = name
        self.quiet = quiet
        self.bright = bright
        self.charger = charger
        self.crowdedness = crowdedness

    def get_score(self, quiet_score, bright_score, charger_score, crowdedness_score) -> float:
        """Calculates the difference between this library's ratings and the user's """
        s1 = abs(self.quiet - quiet_score)
        s2 = abs(self.bright - bright_score)
        s3 = abs(self.charger - charger_score)
        s4 = abs(self.crowdedness - crowdedness_socre)
        return s1 + s2 + s3 + s4


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
    def get_best_library(self, limit:int):
        l = []
        for library in self.libraries:
            l.append((library.name, library.get_score(self.quiet, self.bright, self.charger, self.crowdedness)))
        l.sort(key=lambda key: key[1], reverse=True)

        result, count = [], 0
        while count < limit:
            result.append(l[count][0])
            count += 1
        return result
            

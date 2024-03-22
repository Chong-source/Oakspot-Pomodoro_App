import csv


class Library:
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
        gap = abs(self.quiet - quiet_score)
        gap += abs(self.bright - bright_score)
        gap += abs(self.charger - charger_score)
        gap += abs(self.crowdedness - crowdedness_score)

        return gap


class User:
    """"""
    quiet: int
    bright: int
    charger: int
    crowdedness: int
    libraries: list[Library]

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
        


def load() -> dict[str, Library]:
    """ reads csv file with library ratings and stores them in a variable"""
    libraries = {}

    with open('library_scores.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            libraries[row[0]] = Library(row[1], row[2], row[3], row[4])
    return libraries

if __name__ == '__main__':
    quiet = input("Quietness Preference: ")
    bright = input("Brightness, Aesthetic Preference: ")
    charger = input("Charger Availability Preference: ")
    crowdedness = input("Crowdedness Preference: ")

import csv


class Library:
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

    def get_best_library(self, limit: int):
        """Gets the best library based on the user's inputs"""
        l = []
        for library in self.libraries:
            l.append((library.name, library.get_score(self.quiet, self.bright, self.charger, self.crowdedness)))
        l.sort(key=lambda key: key[1], reverse=True)

        result, count = [], 0
        while count < limit:
            result.append(l[count][0])
            count += 1
        return result


def load(file_name: str) -> list[Library]:
    """ reads csv file with library ratings and stores them in a variable"""
    libraries = []

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            libraries.append(Library(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))
    return libraries


if __name__ == '__main__':
    quiet = int(input("Quietness Preference: "))
    bright = int(input("Brightness, Aesthetic Preference: "))
    charger = int(input("Charger Availability Preference: "))
    crowdedness = int(input("Crowdedness Preference: "))
    libraries = load('library_scores.csv')
    user = User(quiet, bright, charger, crowdedness, libraries)
    print(f'Here are the top 3 libraries matching your choice: {user.get_best_library(3)}')

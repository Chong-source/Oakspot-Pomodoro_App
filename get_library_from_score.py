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
    """
    User information
    """
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
            libraries.append(Library(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])))
    return libraries



class _Vertex:
    item: Any
    kind: str
    neighbours: set[_Vertex]

    def __init__(self, item: Any, kind: str) -> None:
        self.item = item
        self.kind = kind
        self.neighbours = set()

    def similarity_score(self, other: _Vertex) -> float:
        x = self.neighbours
        y = other.neighbours
        if self.degree() == 0 or other.degree() == 0:
            return 0
        else:
            common = 0
            a = 0
            for vertex in x:
                if vertex in y:
                    common += 1
                    a += 1
                else:
                    a += 1
            for vertex in y:
                if vertex in x:
                    pass
                else:
                    a += 1
            return common / a


class Graph:
    _vertices: dict[Any, _Vertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def get_similarity_score(self, item1: Any, item2: Any) -> float:
        if item1 or item2 not in self._vertices:
            Raise ValueError
        else:
            return self._vertices[item1].similarity_score(self._vertices[item2])

        def recommend_books(self, book: str, limit: int) -> list[str]:
        
        similarity_scores = {}

        # Step 1: Calculate similarity scores
        for other_book in self._vertices:
            if other_book != book:
                similarity_scores[other_book] = self.get_similarity_score(book, other_book)

        # Step 2: Filter out unwanted books
        recommended_books = [other_book for other_book, score in similarity_scores.items()
                             if score > 0 and self._vertices[other_book].kind == 'book']

        # Step 3: Sort by similarity score and book title
        recommended_books.sort(key=lambda x: (-similarity_scores[x], x))

        # Step 4: Return top limit recommended books
        return recommended_books[:limit]



if __name__ == '__main__':
    quiet = int(input("Quietness Preference: "))
    bright = int(input("Brightness, Aesthetic Preference: "))
    charger = int(input("Charger Availability Preference: "))
    crowdedness = int(input("Crowdedness Preference: "))
    libraries = load('library_scores.csv')
    user = User(quiet, bright, charger, crowdedness, libraries)
    print(f'Here are the top 3 libraries matching your choice: {user.get_best_library(3)}')

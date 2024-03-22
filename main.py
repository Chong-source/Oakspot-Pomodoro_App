from __future__ import annotations
from typing import Any, Optional


class _LocationVertex:
    """A vertex in a graph.

    Instance Attributes:
        - item: The data stored in this vertex.
        - neighbours: The vertices that are adjacent to this vertex.

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
    """
    item: Any
    neighbours: set[_LocationVertex]

    def __init__(self, item: Any, neighbours: set[_LocationVertex]) -> None:
        """Initialize a new vertex with the given item and neighbours."""
        self.item = item
        self.neighbours = neighbours

    def check_connected(self, target_item: Any, visited: set[_LocationVertex]) -> bool:
        """Return whether this vertex is connected to a vertex corresponding to the target_item,
        WITHOUT using any of the vertices in visited.

        Preconditions:
            - self not in visited
        """
        if self.item == target_item:
            # Our base case: the target_item is the current vertex
            return True
        else:
            visited.add(self)         # Add self to the set of visited vertices
            for u in self.neighbours:
                if u not in visited:  # Only recurse on vertices that haven't been visited
                    if u.check_connected(target_item, visited):
                        return True

            return False


# The recommend book algorithm
def recommend_books(self, book: str, limit: int) -> list[str]:
    books_reverse_alp = [vertex for vertex in self._vertices
                         if self._vertices[vertex].kind == 'book']
    books_reverse_alp.remove(book)
    books_reverse_alp.sort(reverse=True)
    simlrity_scr_map = []
    # create a tuple for every book
    for book2 in books_reverse_alp:
        simlrity_scr_map.append((book2, self.get_similarity_score(book, book2)))
    # sort the list in terms of similarity score
    simlrity_scr_map.sort(key=lambda key: key[1], reverse=True)
    # now add them to the result in a while loop
    result, count, current_pair = [], 0, simlrity_scr_map.pop(0)
    while count < limit and current_pair[1] != 0.0:
        if all(pair[0] != current_pair[1] for pair in result):
            result.append(current_pair[0])
            current_pair = simlrity_scr_map.pop(0)
            count += 1
    return result

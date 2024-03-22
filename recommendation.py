from __future__ import annotations
from typing import Any, Optional


class _Vertex:
    item: Any
    kind: str
    neighbours: set[_Vertex]

    def __init__(self, item: Any, kind: str) -> None:
        self.item = item
        self.kind = kind
        self.neighbours = set()

    def degree(self) -> int:
        return len(self.neighbours)

    def similarity_score(self, other: _Vertex) -> float:
        x = self.neighbours
        y = other.neighbours
        intersection = len(self.neighbours.intersection(other.neighbours))
        union = len(self.neighbours.union(other.neighbours))
        return


class Graph:
    _vertices: dict[Any, _Vertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def get_similarity_score(self, item1: Any, item2: Any) -> float:
        if item1 or item2 not in self._vertices:
            raise ValueError
        else:
            return self._vertices[item1].similarity_score(self._vertices[item2])

    def recommend_locations(self, location: str, limit: int) -> list[str]:
        locations_reverse_alp = [vertex for vertex in self._vertices
                             if self._vertices[vertex].kind == 'location']
        locations_reverse_alp.remove(location)
        locations_reverse_alp.sort(reverse=True)
        simlrity_scr_map = []
        # create a tuple for every location
        for location2 in locations_reverse_alp:
            simlrity_scr_map.append((location2, self.get_similarity_score(location, location2)))
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

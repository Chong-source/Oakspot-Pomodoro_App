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

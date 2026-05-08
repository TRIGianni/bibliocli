from models.Book import Book
from typing import List, Optional
 
class Library:
    def __init__(self):
        self._books: List[Book] = []
 
    def add_book(self, book: Book) -> None:
        self._books.append(book)
 
    def list_books(self) -> List[Book]:
        """Retourne la liste des livres."""
        return list(self._books)
 
    def search_by_title(self, keyword: str) -> List[Book]:
        keyword = keyword.lower()
        return [b for b in self._books if keyword in b.title.lower()]
 
    def find_book(self, title: str) -> Optional[Book]:
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def sort_books(self, by: str = "title") -> List[Book]:
        if by not in ("title", "year"):
            raise ValueError(f"Critère de tri invalide : {by!r}. Utiliser 'title' ou 'year'.")
        key = (lambda b: b.title.lower()) if by == "title" else (lambda b: b.year)
        return sorted(self._books, key=key)
    
    def search_by_author(self, keyword: str) -> List[Book]:
        """Recherche les livres dont l'auteur contient le mot-clé."""
        keyword = keyword.lower()
        return [b for b in self._books if keyword in b.author.lower()]
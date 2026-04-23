class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title        = title
        self.author       = author
        self.year         = year
        self.is_available = True
 
    def __repr__(self) -> str:
        status = "disponible" if self.is_available else "emprunté"
        return f"{self.title} ({self.author}, {self.year}) [{status}]"

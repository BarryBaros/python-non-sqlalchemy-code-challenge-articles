class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name
    

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        if not isinstance(title, str) or not(5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title
    
if __name__ == "__main__":
    try:
        author1 = Author("John Doe")
        magazine1 = Magazine("Tech Today", "Technology")
        article1 = Article(author1, magazine1, "The Rise of AI")
        print(article1.title)  # Should print: The Rise of AI
        
        article2 = Article(author1, magazine1, "Short")  # Should raise a ValueError
    except ValueError as e:
        print(e)
    
    try:
        article3 = Article(author1, magazine1, "This is a very long title that exceeds fifty characters in length")  # Should raise a ValueError
    except ValueError as e:
        print(e)  
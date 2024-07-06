class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []  # Initialize an empty list to store articles

    @property
    def name(self):
        return self._name

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles

    def topic_areas(self):
        if not self._articles:
            return None
        
        unique_topics = set()
        for article in self._articles:
            unique_topics.add(article.magazine.category)
        
        return list(unique_topics)
    

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        
        self._name = name
        self._category = category
        self._articles = []  # Initialize an empty list to store articles
        
        Magazine._all_magazines.append(self)

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        
        top_magazine = None
        max_articles = -1
        
        for magazine in cls._all_magazines:
            article_count = len(magazine._articles)
            if article_count > max_articles:
                max_articles = article_count
                top_magazine = magazine
        
        return top_magazine

    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category

    def article_titles(self):
        if not self._articles:
            return None
        
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        
        author_counts = {}
        
        # Count articles per author
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        
        # Filter authors with more than 2 articles
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        
        if not contributing_authors:
            return None
        
        return contributing_authors

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article


class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author  
        self.magazine = magazine  
        self.title = title  
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        self._magazine = value

if __name__ == "__main__":
    try:
        # Create authors
        author1 = Author("John Doe")
        author2 = Author("Jane Smith")
        
        # Create magazines
        magazine1 = Magazine("Tech Today", "Technology")
        magazine2 = Magazine("Science Weekly", "Science")
        
        # Add articles
        article1 = author1.add_article(magazine1, "Python Programming Essentials")
        article2 = author1.add_article(magazine2, "The Future of Quantum Computing")
        article3 = author2.add_article(magazine1, "Artificial Intelligence in Healthcare")
        
        # Output article details
        print(f"Article 1: {article1.title}, Author: {article1.author.name}, Magazine: {article1.magazine.name}")
        print(f"Article 2: {article2.title}, Author: {article2.author.name}, Magazine: {article2.magazine.name}")
        print(f"Article 3: {article3.title}, Author: {article3.author.name}, Magazine: {article3.magazine.name}")
        
        # Get top publisher
        top_magazine = Magazine.top_publisher()
        if top_magazine:
            print(f"Top Publisher: {top_magazine.name}")
        else:
            print("No magazines available")
        
        # Print topics for each author
        print(f"{author1.name} Topics: {author1.topic_areas()}")
        print(f"{author2.name} Topics: {author2.topic_areas()}")
        
        # Print article titles for each magazine
        print(f"{magazine1.name} Articles: {magazine1.article_titles()}")
        print(f"{magazine2.name} Articles: {magazine2.article_titles()}")
        
        # Print contributing authors for each magazine
        print(f"{magazine1.name} Contributing Authors: {magazine1.contributing_authors()}")
        print(f"{magazine2.name} Contributing Authors: {magazine2.contributing_authors()}")
    
    except ValueError as e:
        print(e)
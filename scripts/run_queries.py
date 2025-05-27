from lib.models import Author, Magazine, Article
from lib.db import seed_data

def main():
    # Setup sample data
    seed_data()
    
    # Query 1: Get all articles by an author
    author = Author.find_by_name("John Doe")
    print(f"Articles by {author.name}:")
    for article in author.articles():
        print(f"- {article.title}")
    
    # Query 2: Find magazines contributed by author
    print("\nMagazines contributed to:")
    for magazine in author.magazines():
        print(f"- {magazine.name} ({magazine.category})")
    
    # Query 3: Authors in a magazine
    magazine = Magazine.find_by_name("Tech Today")
    print("\nAuthors in Tech Today:")
    for contributor in magazine.contributors():
        print(f"- {contributor.name}")
    
    # Query 4: Magazines with >=2 authors
    print("\nMagazines with multiple authors:")
    for magazine in Magazine.find_with_multiple_authors():
        print(f"- {magazine.name}")
    
    # Query 5: Article counts per magazine
    print("\nArticle counts:")
    for name, count in Magazine.article_counts().items():
        print(f"- {name}: {count} articles")
    
    # Query 6: Most published author
    prolific = Author.most_published()
    print(f"\nMost published author: {prolific.name}")

if __name__ == "__main__":
    main()
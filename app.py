class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added: {new_book}")

    def show_all_books(self):
        if not self.books:
            print("The library is currently empty.")
        else:
            print("\n--- Library Collection ---")
            for book in self.books:
                print(book)

def main():
    # Simple Logic for DevOps Automation Test
    my_library = Library()
    
    # Adding some dummy data
    my_library.add_book("DevOps Handbook", "Gene Kim")
    my_library.add_book("Clean Code", "Robert C. Martin")
    my_library.add_book("Jira Automation Guide", "Daud Idrees")

    # Displaying results
    my_library.show_all_books()

if __name__ == "__main__":
    main()

class BookService:
    def __init__(self, repo, storage):
        self.repo = repo
        self.storage = storage

    def insert_book(self, book):
        return self.repo.insert_book(book)

    def select_book(self, column, value):
        rows = self.repo.select_book(column, value)
        print(rows)
        return [
            {
                "id": row[0],
                "isbn": row[1],
                "book_title": row[2],
                "author_name": row[3],
                "publication_year": row[4],
                "page_count": row[5],
                "genre": row[6],
                "book_status": row[7],
                "physical_version": row[8],
                "digital_version": row[9],
                "count": row[10],
            }
            for row in rows
        ]

    def update_book(self, column, value, updates):
        return self.repo.update_book(column, value, updates)

    def delete_book(self, column, value):
        return self.repo.delete_book(column, value)

    def loan_book(self, book_search, member_search):
        return self.repo.loan_book(
            book_search[0],
            book_search[1],
            member_search[0],
            member_search[1]
        )
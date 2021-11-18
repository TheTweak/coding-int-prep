'''
Design data structures for an online book reader system.

1) do we need authentication/user registration ?
2) can we search books?
3) can we add new books?
4) do we need to buy a book before it can be read?
5) do we keep a progress of a read book?
6) can we move to a random page, or only page forward/backward?
7) books have only text or pictures too?

improvements:
- cache popular books/pages
'''

class BookContent:
    def __init__(self, content: bytes, pagesize: int):
        self.content = content
        self.pagesize = pagesize

    def get_pages(self, start: int, end: int) -> list[str]:
        '''
        Returns decoded pages text from start to end as a list of str.
        One item is one page.
        '''
        pass


class Book:
    def __init__(self, id: str, title: str, author: str, num_pages: int, content: BookContent):
        self.id = id
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.content = content


class User:
    def __init__(self, username: str):
        self.username = username
        self.bookmarks: dict[str:int] = {}


class ReaderService:
    def __init__(self):
        self.books: dict[str:Book] = {}

    def add_book(self, book: Book) -> None:
        self.books[book.id] = book

    def resume_or_start_book(self, book_id: str, user: User) -> (str, str):
        return self.__get_pages(book_id, user, 0)

    def get_prev_pages(self, book: Book, user: User) -> (str, str):
        return self.__get_pages(book_id, user, -1)

    def get_next_pages(self, book: Book, user: User) -> (str, str):
        return self.__get_pages(book_id, user, 1)

    def __get_pages(self, book_id: str, user: User, offset: int) -> (str, str):
        assert book.id in self.books
        book = self.books[book.id]
        current_page = user.bookmarks.get(book.id, -1)
        new_page = max(0, current_page + offset)
        pages = book.content.get_pages(new_page, new_page+1)
        user.bookmarks[book.id] = new_page
        return pages[0], pages[1]

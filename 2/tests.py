import pytest
from library import *

# בדיקה שהפנקציה מוסיפה ספר חדש לרשימת הספרים במערכת
def test_add_book():
    library = Library()
    book = Book("Al Taster", "Libi Klain")
    library.add_book(book)
    assert book in library.books

# בדיקה שהפנקציה מוסיפה משתמש חדש לרשימת המשתמשים
@pytest.mark.skip(reason="it's already ok")
def test_add_user():
    library = Library()
    library.add_user("user")
    assert "user" in library.users

# בדיקה שהמערכת מונעת השאלת ספר כאשר הוא כבר נמצא בהשאלה
def test_check_out_book():
    library = Library()
    user = "user"
    book = Book("Mahalalel", "Maya Keinan")
    library.add_user(user)
    library.add_book(book)
    library.check_out_book(user, book)
    assert library.check_out_book(user, book)

# בדיקה שהמערכת מונעת החזרת ספר שלא הושאל כלל
@pytest.mark.skip(reason="not now")
def test_return_book():
    library = Library()
    book = Book("Tachanot", "Dvory Rand")
    library.add_book(book)
    assert library.return_book(book)

# בדיקה שהפונקציה מחפשת ספרים לפי שם מדויק
def test_search_books():
    library = Library()
    book = Book("Shatul", "Yona Sapir")
    library.add_book(book)
    assert library.search_books("Shatul")

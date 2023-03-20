# how would I test Barky?
# First, I wouldn't test barky, I would test the reusable modules barky relies on:
# commands.py and database.py

# we will use pytest: https://docs.pytest.org/en/stable/index.html

# should we test quit? No, its behavior is self-evident and not logic dependent
# okay, should I test the other commands?
# not really, they are tighly coupled with sqlite3 and its use in the database.py module
import pytest
from commands import AddBookmarkCommand, DeleteBookmarkCommand, EditBookmarkCommand, ListBookmarksCommand
from database import DatabaseManager

db = DatabaseManager("bookmarks.db")


@pytest.fixture
def db_man() -> DatabaseManager:
    filename = "bookmarks.db"
    dbm = DatabaseManager(filename)
    yield dbm
    dbm.__del__()
    os.remove(filename)

 # Test the adding of a new bookmark


def test_new_bookmark():
    expected_result = 'Bookmark added!'

    result = AddBookmarkCommand.execute(
        db_man, {'title': 'New Bookmark', 'url': 'https://thecoachs.com'})

    assert result == expected_result


def test_list_bookmarks():

    db_man.order_by = "title"
    result = ListBookmarksCommand.execute(db_man)

    pass


def test_del_bookmarks():
    expected_result = 'Bookmark deleted!'

    result = DeleteBookmarkCommand.execute(
        db_man, 1)

    assert result == expected_result

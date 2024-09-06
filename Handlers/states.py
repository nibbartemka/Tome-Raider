import enum


@enum.unique
class ReadingState(enum.StrEnum):
    SELECT_PAGE = 'reading_select_page'
    NEXT_PAGE = 'reading_next_page'
    PREVIOUS_PAGE = 'reading_previous_page'
    RETURN = 'reading_return'


@enum.unique
class DetailState(enum.StrEnum):
    START_READ = 'detail_start_read'
    RATE = 'detail_rate'
    RETURN = 'detail_return'


@enum.unique
class StartState(enum.StrEnum):
    GO_TO_BOOKS = 'start_books'
    GO_TO_BOOKMARKS = 'start_bookmarks'

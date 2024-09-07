# from .DataBase import SQLiteDataBase, DataBaseProtocol


# database: DataBaseProtocol = SQLiteDataBase()


# # @database.execute_SQL
# # def create_user_table() -> str:
# #     '''
# #     Raw query for creating user table

# #     Args:

# #     Returns:
# #         str: raw SQL-query for safe-creating user table
# #     '''

# #     return (
# #         '''
# #             CREATE TABLE IF NOT EXISTS user (
# #                 user_id BIGINT PRIMARY KEY
# #             );
# #         '''
# #     )


# @database.execute_SQL
# def create_author_table() -> str:
#     '''
#     Raw query for creating author table

#     Args:

#     Returns:
#         str: raw SQL-query for safe-creating author table
#     '''

#     return (
#         '''
#             CREATE TABLE IF NOT EXISTS author (
#                 author_id BIGINT PRIMARY KEY,
#                 author_name VARCHAR(50) NOT NULL
#             );
#         '''
#     )


# @database.execute_SQL
# def create_genre_table() -> str:
#     '''
#     Raw query for creating genre table

#     Args:

#     Returns:
#         str: raw SQL-query for safe-creating genre table
#     '''

#     return (
#         '''
#             CREATE TABLE IF NOT EXISTS genre (
#                 genre_id BIGINT PRIMARY KEY,
#                 genre_name VARCHAR(50) NOT NULL
#             );
#         '''
#     )


# # @database.execute_SQL
# # def create_book_table() -> str:
# #     '''
# #     Raw query for creating book table

# #     Args:

# #     Returns:
# #         str: raw SQL-query for safe-creating book table
# #     '''

# #     return (
# #         '''
# #             CREATE TABLE IF NOT EXISTS book (
# #                 book_id BIGINT PRIMARY KEY,
# #                 book_title VARCHAR(50) NOT NULL,
# #                 genre_id BIGINT NOT NULL,
# #                 object_link VARCHAR(50) NOT NULL,

# #                 FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
# #             );
# #         '''
# #     )


# # @database.perform_SQL()
# # def create_

# def database_init():
#     create_author_table()

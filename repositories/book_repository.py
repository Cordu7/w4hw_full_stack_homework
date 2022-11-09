import repositories.author_repository as author_repository
from db.run_sql import run_sql
# from models.book import Book


def save(book):
    sql = "INSERT INTO books (title, genre, author) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id= id
    return book


# def save(task):
#     sql = "INSERT INTO tasks (description, user_id, duration, completed) VALUES (%s, %s, %s, %s) RETURNING *"
#     values = [task.description, task.user.id, task.duration, task.completed]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     task.id = id
#     return task

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)

# def select_all():
#     books =[]
#     sql= "SELECT * FROM books"
#     results = run_sql(sql)
#     for row in results:
#         author = author_repository.select(row['author_id'])
#         book = Book(row['title'], row['genre'], author, row['id'])
#         books.append(book)
#     return books


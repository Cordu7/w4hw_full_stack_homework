from db.run_sql import run_sql

from models.author import Author


def save(author):
    sql = "INSERT INTO authors (f_name, l_name) VALUES (%s, %s) RETURNING *"
    values = [author.f_name, author.l_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)

# def select_all():
#     authors= []
#     sql= "SELECT * FROM authors"
#     results = run_sql(sql)
#     for row in results:
#         author = Author(row['f_name'], row['l_name'])
#         authors.append(author)
#     return authors
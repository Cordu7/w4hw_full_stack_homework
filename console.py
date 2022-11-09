import pdb

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository
from models.author import Author
from models.book import Book

author_repository.delete_all()
book_repository.delete_all()

author1= Author('Jason', 'Stanley')
author2 = Author('Jeff', 'Kinney')


author_repository.save(author1)

author_repository.save(author2)

book1= Book('How Propaganda Works', 'Philosophy', author1)
book2= Book('How Fascism Works', 'Philosophy', author1)
book3= Book('Diary of a Wimpy Kid', "Children's Comic", author2)
book4= Book('Diary of a Wimpy Kid Rodrick Rules', "Children's Comic", author2)


book_repository.save(book1)
book_repository.save(book2)
book_repository.save(book3)
book_repository.save(book4)



pdb.set_trace()
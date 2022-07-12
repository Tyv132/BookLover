import pandas as pd

class BookLover:

    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'rating':[]})

    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre

    def add_book(self, book_name, rating):

        new_book = pd.DataFrame({'book_name': [book_name], 'rating': [rating]})
        if book_name not in list(self.book_list['book_name']):
            if rating in [1,2,3,4,5]: 
                self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
                self.book_list['rating'] = self.book_list['rating'].astype('int64')
                self.num_books += 1 
            else:
                print('The book rating must be an integer from 1 to 5')
        else:
            print('This book is already in the list.')

    def has_read(self, book_name):
        if book_name in list(self.book_list['book_name']):
            return True
        else: 
            return False

    def num_book_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list.loc[self.book_list['rating'] > 3]


# End of booklover.py


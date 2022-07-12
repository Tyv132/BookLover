import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
       # Create instance
       user = BookLover('John Smith', 'jsmith@virginia.edu','Fantasy')
       # Add book
       user.add_book('Harry Potter', 4)
       # Check
       actual = user.book_list
       expected = pd.DataFrame({'book_name':['Harry Potter'], 'rating':[4]})
       pd.testing.assert_frame_equal(actual, expected) 
       # I needed to use this function for the DataFrame objects. 

    def test_2_add_book(self):
       # Create instance
       user = BookLover('John Smith', 'jsmith@virginia.edu','Fantasy')
       # Add same book twice
       user.add_book('Harry Potter', 4)
       user.add_book('Harry Potter', 4)
       # Check
       actual = user.book_list
       expected = pd.DataFrame({'book_name':['Harry Potter'], 'rating':[4]})
       pd.testing.assert_frame_equal(actual, expected) 
       # I needed to use this function for the DataFrame objects. 

    def test_3_has_read(self): 
       # Create instance
       user = BookLover('John Smith', 'jsmith@virginia.edu','Fantasy')
       # Add book 
       user.add_book('Harry Potter', 4)
       # Check
       actual = user.has_read('Harry Potter')
       message = "Test value is not True."
       self.assertTrue(actual, message) 

    def test_4_has_read(self): 
       # Create instance
       user = BookLover('John Smith', 'jsmith@virginia.edu','Fantasy')
       # Add book
       user.add_book('Harry Potter', 4)
       # Check
       actual = user.has_read('The Hobbit')
       message = "Test value is not False."
       self.assertFalse(actual, message) 

    def test_5_num_books_read(self): 
       # Create instance
       user = BookLover('John Smith', 'jsmith@virginia.edu','Fantasy')
       # Add book
       user.add_book('Harry Potter', 5)
       user.add_book('Alice in Wonderland', 3)
       user.add_book('Dune', 4)
       user.add_book('Lord of the Rings', 2)
       # Check
       actual = user.num_book_read()
       expected = 4
       self.assertEqual(actual, expected)

    def test_6_fav_books(self):
       # Create instance
       user = BookLover('John Smith', 'jsmith@virginia.edu','Fantasy')
       # Add book
       user.add_book('Harry Potter', 5)
       user.add_book('Moby Dick', 2)
       user.add_book('Alice in Wonderland', 4)
       user.add_book('The Hunger Games', 3)
       # Check
       actual = all(i >= 3 for i in user.fav_books()['rating'])
       message = "Test value is not true."
       self.assertTrue(actual, message)

if __name__ == '__main__':
   unittest.main(verbosity=3)

# End of booklover_test.py


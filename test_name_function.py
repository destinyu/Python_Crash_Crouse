import unittest
from name_fucation import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_Name(self):
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')


unittest.main()
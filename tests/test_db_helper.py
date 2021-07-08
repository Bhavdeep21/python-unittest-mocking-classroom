from unittest import TestCase
from unittest.mock import patch
from src.db_helper import  DbHelper
class Testdb(TestCase):
    def setUp(self):
        self.dbr = DbHelper()
    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self, MockDB):
        db=MockDB()
        db.get_maximum_salary.return_value=10
        max=db.get_maximum_salary()
        db.get_minimum_salary.return_value=1
        min=db.get_minimum_salary()
        self.assertGreater(max,min,"Min is greater than max")
        
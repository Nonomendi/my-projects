import unittest
import mastermind
from unittest.mock import patch 
from io import StringIO
import sys

class mytestcase(unittest.TestCase):
    def test_create_code(self):
        code=mastermind.create_code()
        for i in range(100):
            self.assertEqual(4,len(code))
            self.assertNotIn(9,code)
            self.assertNotIn(0,code)
    @patch("sys.stdin",StringIO("12\n12345\ndsfa\n0000\n1234\n"))
    def test_get_user_input(self):
        self.assertEqual(mastermind.get_user_input(),"1234")
        
    @patch("sys.stdin",StringIO("2345\n1837\n8135\n1234\n"))
    def test_take_turn(self):
        mock_code=[1,8,3,7]
        self.assertEqual(mastermind.take_turn(mock_code),(0,1))
        self.assertEqual(mastermind.take_turn(mock_code),(4,0))
        self.assertNotEqual(mastermind.take_turn(mock_code),(1,1))
        self.assertNotEqual(mastermind.take_turn(mock_code),(3,0))

    def test_check_correctness(self):
        turns=2
        looser=3
        winner=4
        self.assertTrue(mastermind.check_correctness(turns,winner))
        self.assertFalse(mastermind.check_correctness(turns,looser))


    sys.stdout=StringIO()
if __name__ == "__main__":
    unittest.main()

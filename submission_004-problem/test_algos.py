import unittest
import super_algos
from io import StringIO
import sys

class TestSuperAlgos(unittest.TestCase):

    def test_find_min(self):
        # element = [1,2,3,4]
        # super_algos.find_min(element)
        self.assertEqual(super_algos.find_min([1,2,3,4]),1)
        self.assertEqual(super_algos.find_min([3,4,-6,-8]),-8)
        self.assertEqual(super_algos.find_min([12,"a",1,1.7,3]),-1)
        self.assertEqual(super_algos.find_min([]),-1)

    def test_sum_all(self):
         self.assertTrue(type(super_algos.sum_all([1,2,3,4])),10)
         self.assertTrue(type(super_algos.sum_all([1,1.2,3,"q"])),-1)
         self.assertTrue(type(super_algos.sum_all([6])),6)
         self.assertTrue(type(super_algos.sum_all([])),-1)
         self.assertTrue(type(super_algos.sum_all([-1,-2,-3])),-6)

    def test_find_possible_strings(self):
        self.assertEqual(["a","b","c","d"], super_algos.find_possible_strings(["a","b","c","d"],1))
        self.assertEqual(["a","b"],super_algos.find_possible_strings(["a","b"],3))
        self.assertEqual([],super_algos.find_possible_strings([],3))

    def possible_string(self):
        self.assertEqual([1,2,3,4],super_algos.possible_stringsRec([1,2,3,4],3))
        self.assertEqual(type(super_algos.possible_stringsRec([1,2,3,4])),[])

    unittest.main()
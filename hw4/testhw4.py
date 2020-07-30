# ----------------------------------------------------------------------
# Name:    homework7
# Purpose: Test cases for homework4
#
# Author(s): Haitao Huang, Duong Cao
# ----------------------------------------------------------------------

"""
Implement 5 test cases for the 5 functions in Homework 4:
Q1: top_students
Q2: final_grade
Q3: boost_grade
Q4: word_lengths
Q5: geometric_sum
"""

import unittest
import homework4 as hw4


class TestQ1(unittest.TestCase):
    """
    Test case for the top_students function
    """

    def setUp(self):
        """
        Create dictionaries
        """
        self.empty = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_top_students_empty_dict(self):
        """
        Test the function with empty students name list
        """

        self.assertEqual(hw4.top_students(self.empty, 6), [])

    def test_top_students_original_dict(self):
        """
        Test the function with the original dictionary
        """
        self.assertEqual(self.cs122, {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100})

    def test_top_students_default(self):
        """
        Test the function with default number of top students and original dictionary
        """
        self.assertEqual(hw4.top_students(self.cs122), ['Anna', 'Alex', 'Zoe'])

    def test_top_students_of_2(self):
        """
        Test the function with the wanted number of top students is 2
        """

        self.assertEqual(hw4.top_students(self.cs122, 2), ['Anna', 'Alex'])

    def test_top_students_of_10(self):
        """
        Test the function with the wanted number of top students is 10
        """
        self.assertEqual(hw4.top_students(self.cs122, 10), ['Anna', 'Alex', 'Zoe', 'Dan'])


class TestQ2(unittest.TestCase):
    """
    Test case for the final_grade function
    """

    def setUp(self):
        """
        Create dictionaries
        """
        self.empty = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_the_original_dict(self):
        """
        Test the function with the original dictionary
        """
        self.assertEqual(self.cs122,
                         {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100})

    def test_final_grade_empty_dict(self):
        """
        Test the function with empty dictionary
        """
        self.assertEqual(hw4.final_grade(self.empty, 5), {})

    def test_final_grade_default(self):
        """
        Test the function with original dictionary and default number of extra credit
        """
        self.assertEqual(hw4.final_grade(self.cs122),
                         {'Zoe': 91, 'Alex': 94, 'Dan': 80, 'Anna': 101})

    def test_final_grade_2_credit(self):
        """
        Test the function with 2 extra credit points to the student's grade
        """
        self.assertEqual(hw4.final_grade(self.cs122, 2),
                         {'Zoe': 92, 'Alex': 95, 'Dan': 81, 'Anna': 102})


class TestQ3(unittest.TestCase):
    """
    Test case for the boost_grade function
    """

    def setUp(self):
        """
        Create dictionaries
        """
        self.iclicker = {'Zoe': 46, 'Alex': 121, 'Ryan': 100, 'Anna': 110,
                         'Bryan': 2, 'Andrea': 110}
        self.exam = {'Dan': 89, 'Ryan': 89, 'Alex': 95, 'Anna': 64,
                     'Bryan': 95, 'Andrea': 86}

    def test_boost_grade_default(self):
        """
        Test the function with default dictionaries
        """
        self.assertEqual(hw4.boost_grade(self.iclicker, self.exam),
                         {'Bryan': 95, 'Zoe': 0, 'Anna': 65, 'Alex': 96, 'Ryan': 90,
                          'Andrea': 87, 'Dan': 89})

    def test_boost_grade_non_iclicker(self):
        """
        Test the function with empty iclicker dictionary
        """
        self.assertEqual(hw4.boost_grade({}, self.exam),
                         {'Ryan': 89, 'Andrea': 86, 'Bryan': 95, 'Anna': 64,
                          'Dan': 89, 'Alex': 95})

    def test_boost_grade_non_exam(self):
        """
        Test the function with empty exam dictionary
        """
        self.assertEqual(hw4.boost_grade(self.iclicker, {}),
                         {'Ryan': 1, 'Andrea': 1, 'Bryan': 0, 'Zoe': 0, 'Anna': 1,
                          'Alex': 1})

    def test_boost_grade_empty(self):
        """
        Test the function with empty dictionaries
        """
        self.assertEqual(hw4.boost_grade({}, {}), {})


class TestQ4(unittest.TestCase):
    """
    Test case for the word_lengths function
    """

    def setUp(self):
        """
        Create dictionaries
        """
        self.p1 = '''Simple is better than     complex, and flat 
                 IS BETTER than nested!?!'''
        self.p2 = 'PYTHON       is Fun!!>!!!'

    def test_word_lengths_empty(self):
        """
        Test the function with empty dictionary
        """
        self.assertEqual(hw4.word_lengths(''), {})

    def test_word_lengths_phrase1(self):
        """
        Test the function with dictionary p1
        """
        self.assertEqual(hw4.word_lengths(self.p1),
                         {'simple': 6, 'is': 2, 'better': 6, 'than': 4, 'complex': 7,
                          'and': 3, 'flat': 4, 'nested': 6})

    def test_word_lengths_phrase2(self):
        """
        Test the function with dictionary p2
        """
        self.assertEqual(hw4.word_lengths(self.p2),
                         {'python': 6, 'is': 2, 'fun': 3})


class TestQ5(unittest.TestCase):
    """
    Test case for the geometric_sum function
    """

    def test_geometric_sum_negative(self):
        """
        Test the function with negative number
        """
        self.assertEqual(hw4.geometric_sum(-5), 0)

    def test_geometric_sum_zero(self):
        """
        Test the function with 0 number
        """
        self.assertEqual(hw4.geometric_sum(0), 0)

    def test_geometric_sum_1(self):
        """
        Test the function with n=1
        """
        self.assertEqual(hw4.geometric_sum(1), 0.5)

    def test_geometric_sum_2(self):
        """
        Test the function with n = 2
        """
        self.assertEqual(hw4.geometric_sum(2), 0.75)

    def test_geometric_sum_3(self):
        """
        Test the function with n = 3
        """
        self.assertEqual(hw4.geometric_sum(3), 0.875)

    def test_geometric_sum_4(self):
        """
        Test the function with n = 4
        """
        self.assertEqual(hw4.geometric_sum(4), 0.9375)

    def test_geometric_sum_30(self):
        """
        Test the function with n = 30
        """
        self.assertEqual(hw4.geometric_sum(30), 0.9999999990686774)


if __name__ == "__main__":
    unittest.main(verbosity=2)

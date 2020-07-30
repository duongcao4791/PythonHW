import unittest
import hw5 as hw5


class TestQ1(unittest.TestCase):
    def setUp(self):
        self.empty = {}
        self.cs122 = {'Zoe': [90, 100, 75], 'Alex': [86, 90, 96],
                      'Dan': [90, 60, 70], 'Anna': [60, 80, 100],
                      'Ryan': [100, 95, 80], 'Bella': [79, 70, 99]}

    def test_top_midterm_empty(self):
        self.assertIsNone(hw5.top_midterm(self.empty))

    def test_top_midterm_non_empty(self):
        self.assertEqual(hw5.top_midterm(self.cs122), 'Anna')
        self.assertEqual(self.cs122, {'Zoe': [90, 100, 75], 'Alex': [86, 90, 96],
                                      'Dan': [90, 60, 70], 'Anna': [60, 80, 100],
                                      'Ryan': [100, 95, 80], 'Bella': [79, 70, 99]})


class TestQ2(unittest.TestCase):
    def test_longest_sequence_no_arg(self):
        self.assertEqual(hw5.longest_sequence(), 0)

    def test_longest_sequence_1_arg(self):
        self.assertEqual(hw5.longest_sequence(60), 1)

    def test_longest_sequence_4_args(self):
        self.assertEqual(hw5.longest_sequence(100, 202, 5, 2), 1)

    def test_longest_sequence_long(self):
        self.assertEqual(hw5.longest_sequence(4, 10, 8, 3, 2, 11, 9, 40, 7, 7, 8, 4, 12), 6)


class TestQ3(unittest.TestCase):
    def setUp(self):
        """
        Create some decorated functions for testing. """

        @hw5.encrypt
        def greet(name):
            """
            Return a personalized hello message. :param name: (string)
            :return: (string)
            """

            return f'Hello {name}'

        @hw5.encrypt
        def repeat(phrase, n):
            """
            Repeat the specified string n times
            with a space character in between.
            :param phrase: (string)
            :param n: number of times the phrase will be repeated :return: (string)
            """

            words = phrase.split()
            return ' '.join(n * words)

        self.greet = greet
        self.repeat = repeat

    def test_decorated_greet(self):
        self.assertEqual(self.greet('Spatans'), 'sapatansa hllo')

    def test_decorated_repeat(self):
        self.assertEqual(self.repeat("Special cases aren't special enough to break the rules", 2),
                         "rulsa th brak to nough sapcial arn't casasa sapcial "
                         "rulsa th brak to nough sapcial arn't casasa sapcial")

    def test_encrypt_empty_string(self):
        self.assertEqual(self.repeat("", 10), "")


class TestQ4(unittest.TestCase):
    def setUp(self):
        self.baby = hw5.babble('spider.txt', 5)
        self.beatles = hw5.babble('yesterday.txt')
        self.shakespeare = hw5.babble('hamlet.txt', 10)

    def test_baby(self):
        self.assertEqual(next(self.baby), 'went up all the itsy')
        self.assertEqual(next(self.baby), 'washed the water spout down')
        self.assertEqual(next(self.baby), 'dried up the spider out')
        self.assertEqual(next(self.baby), 'spout again water spout down')
        self.assertEqual(next(self.baby), 'water spout again sun dried')
        self.assertEqual(next(self.baby), 'out came the itsy bitsy')

    def test_beatles(self):
        self.assertEqual(next(self.beatles), "it looks as though they're here to be")
        self.assertEqual(next(self.beatles), 'me oh i believe in yesterday all my')
        self.assertEqual(next(self.beatles), "suddenly i'm not half the man i need")
        self.assertEqual(next(self.beatles), 'not half the man i said something wrong')
        self.assertEqual(next(self.beatles), "looks as though they're here to go i")
        self.assertEqual(next(self.beatles), "looks as though they're here to stay oh")
        self.assertEqual(next(self.beatles), 'something wrong now i need a place to')
        self.assertEqual(next(self.beatles), "a place to be there's a place to")
        self.assertEqual(next(self.beatles), 'game to hide away now it looks as')
        self.assertEqual(next(self.beatles), 'troubles seemed so far away oh yesterday why')

    def test_shakespeare(self):
        self.assertEqual(next(self.shakespeare), 'grapple i once the thing my lord they may sweep')
        self.assertEqual(next(self.shakespeare), 'garments heavy nor stands who by very cunning of us')
        self.assertEqual(next(self.shakespeare), 'yea and i tell us where is but that live')
        self.assertEqual(next(self.shakespeare), 'haunt this hamlet there’s the rugged pyrrhus stood and his')
        self.assertEqual(next(self.shakespeare), 'whine to the players shall and shows his father’s person')


if __name__ == "__main__":
    unittest.main(verbosity=2)

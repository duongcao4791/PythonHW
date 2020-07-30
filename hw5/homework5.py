# # ----------------------------------------------------------------------
# # Name:    homework5
# # Purpose: Practice working with Python functions and files
# #
# # Author(s): Haitao Huang, Duong Cao
# # ----------------------------------------------------------------------
# """
# Implement various functions
#
# Q1: top_midterm
# Q2: longest_sequence
# Q3: encrypt decorator
# Q4: learn
# Q5: babble
# """
# import string
# import random
#
#
# # Enter your 5 function definitions here
# def top_midterm(grades):
#     """
#     Find the student with the highest midterm grade.
#     :param grades: (dictionary) containing student names and grades
#     :return: (string) name of one student with the highest midterm grade
#     """
#     if grades:
#         return max(grades, key=lambda student: grades[student][2])
#     else:
#         return None
#
#
# def longest_sequence(*args):
#     """
#     Find the length of the longest consecutive sequence of integers.
#     :param args: (number) 0 or more integers
#     :return: (number) length of the longest consecutive sequence of
#                       integers
#     """
#     if args:
#         sorted_list = sorted(set(args))
#         if len(sorted_list) > 1:
#             longest = 1
#             tmp_longest = 1
#             for i in range(1, len(sorted_list)):
#                 if sorted_list[i] == sorted_list[i - 1] + 1:
#                     tmp_longest = tmp_longest + 1
#                 else:
#                     if tmp_longest > longest:
#                         longest = tmp_longest
#                     tmp_longest = 1
#             return longest
#         else:
#             return 1
#     else:
#         return 0
#
#
# def encrypt(function):
#     """
#     Decorate another function that returns a string by removing all 'e',
#     adding an 'a' after each 's', reversing the order of the words in
#     the string and converting it to lower case.
#     :param function: (function) a function that returns a string
#     :return: (function) a new function
#     """
#
#     def wrapper(*args):
#         str = function(*args).lower()
#         chars_list = [c for c in str if c != 'e']
#         i = 0
#         while i < len(chars_list):
#             if chars_list[i] == 's':
#                 chars_list.insert(i + 1, 'a')
#                 i = i + 1
#             i = i + 1
#         words = ''.join(chars_list).split()
#         words.reverse()
#         return ' '.join(words)
#
#     return wrapper
#
#
# @encrypt
# def greet(name):
#     """
#     Return a personalized hello message.
#     :param name: (string)
#     :return: (string)
#     """
#     return f'Hello {name}'
#
#
# @encrypt
# def repeat(phrase, n):
#     """
#     Repeat the specified string n times
#     with a space character in between.
#     :param phrase: (string)
#     :param n: number of times the phrase will be repeated
#     :return:
#     """
#     words = phrase.split()
#     return ' '.join(n * words)
#

# def learn(fn):
#     """
#     Create a dictionary where each word is mapped to a list of all the
#     words that immediately follow it in the input file.
#     :param fn: (string) a filename
#     :return: (dictionary) a dictionary based on the file's content
#     """
#     with open(fn, 'r', encoding='UTF-8') as input_file:
#         content_lines = input_file.readlines()
#     file_dict = {}
#     last_word = None
#     for each_line in content_lines:
#         for each_word in each_line.lower().split():
#             stripped_word = each_word.strip(string.punctuation)
#             if stripped_word != '':
#                 if stripped_word not in file_dict:
#                     file_dict[stripped_word] = []
#                 if last_word:
#                     file_dict[last_word].append(stripped_word)
#                 last_word = stripped_word
#     return file_dict
#

# # Include the statement below at the top of the babble definition
# # random.seed(100)
#
# def babble(fn, n=8):
#     """
#     Create an infinite random sentence generator that generates
#     nonsensical sentences of a given length, loosely modeled after a
#     specified text file.
#     :param fn: (string) a filename
#     :param n: (number) number of words in the sentence
#     :yield: a sentence of n words
#     """
#     random.seed(100)
#     words = learn(fn)
#     all_keys = list(words)
#     while True:
#         new_word = random.choice(all_keys)
#         str = new_word
#         for i in range(0, n - 1):
#             if words[new_word]:
#                 new_word = random.choice(words[new_word])
#             else:
#                 new_word = random.choice(all_keys)
#             str = str + ' ' + new_word
#         yield str
#

# def main():
#     # You may use the main function to test your function definitions.
#     print('>>>>>>Question 1<<<<<<')
#     empty_class = {}
#     cs122 = {'Zoe': [90, 100, 75], 'Alex': [86, 90, 96],
#              'Dan': [90, 60, 70], 'Anna': [60, 80, 100],
#              'Ryan': [100, 95, 80], 'Bella': [79, 70, 99]}
#     print(top_midterm(cs122))  # Anna
#     print(top_midterm(empty_class))  # None
#     print(cs122)  # cs 122 is unchanged
#
#     print('')
#     print('>>>>>>Question 2<<<<<<')
#     print(longest_sequence(4, 10, 8, 3, 2, 11, 9, 40, 7, 7, 8, 4, 12))
#     # 6
#     print(longest_sequence())  # 0
#     print(longest_sequence(100, 202, 5, 2))  # 1
#     print(longest_sequence(60))  # 1
#
#     print('')
#     print('>>>>>>Question 3<<<<<<')
#     print(greet('Spartans'))  # sapartansa hllo
#     print(repeat("Special cases aren't special enough to break the rules", 2))
#     # rulsa th brak to nough sapcial arn't casasa sapcial rulsa th
#     # brak to nough sapcial arn't casasa sapcial
#
#     print('')
#     print('>>>>>>Question 4<<<<<<')
#     print('dictionary of spider.txt:')
#     print(learn("spider.txt"))
#
#     print('')
#     print('>>>>>>Question 5<<<<<<')
#     baby = babble('spider.txt', 5)
#     print(next(baby))  # 'went up all the itsy'
#     print(next(baby))  # 'washed the water spout down'
#     print(next(baby))  # 'dried up the spider out'
#     print(next(baby))  # 'spout again water spout down'
#     print(next(baby))  # 'water spout again sun dried'
#     print(next(baby))  # 'out came the itsy bitsy'
#     print('')
#     beatles = babble('yesterday.txt')
#     print(next(beatles))  # "it looks as though they're here to be"
#     print(next(beatles))  # 'me oh i believe in yesterday all my'
#     print(next(beatles))  # "suddenly i'm not half the man i need"
#     print(next(beatles))  # 'not half the man i said something wrong'
#     print(next(beatles))  # "looks as though they're here to go i"
#     print(next(beatles))  # "looks as though they're here to stay oh"
#     print(next(beatles))  # 'something wrong now i need a place to'
#     print(next(beatles))  # "a place to be there's a place to"
#     print(next(beatles))  # 'game to hide away now it looks as'
#     print(next(beatles))
#     # 'troubles seemed so far away oh yesterday why'
#     print('')
#     shakespeare = babble('hamlet.txt', 10)
#     print(next(shakespeare))
#     # 'grapple i once the thing my lord they may sweep'
#     print(next(shakespeare))
#     # 'garments heavy nor stands who by very cunning of us'
#     print(next(shakespeare))
#     # 'yea and i tell us where is but that live'
#     print(next(shakespeare))
#     # 'haunt this hamlet there’s the rugged pyrrhus stood and his'
#     print(next(shakespeare))
#     # 'whine to the players shall and shows his father’s person'
#
#
# if __name__ == '__main__':
#     main()

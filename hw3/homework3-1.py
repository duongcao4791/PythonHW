# # ----------------------------------------------------------------------
# # Name:        homework3
# # Purpose:     Practice Manipulating Sequence Data Types
# #
# # Author(s):   Haitao Huang, Duong Cao
# # ----------------------------------------------------------------------
# """
# Implement various functions to practice manipulating sequence data types
#
# Q1: transpose
# Q2: grader
# Q3: has_duplicates
# Q4: remove_vowels
# Q5: same_word_count
# """
#
# # Enter your 5 function definitions here
# def transpose(m):
#     """
#     Take a matrix and return the transpose of it
#     :param m: (nested list) a matrix of arbitrary size
#     :return: (nested list) the transpose of the matrix m
#     """
#     return [[m[column][row] for column in range(len(m))]
#             for row in range(len(m[0]))]
#
# def grader(grades, threshold = 4):
#     """
#     Keep the size of a list of grades within the threshold and calculate
#      the average grade
#     :param grades: (list) a list of grades
#     :param threshold: (number) threshold of grades
#     :return: (number) average grade
#     """
#     if grades:
#         if len(grades) > threshold:
#             for i in range(len(grades)-threshold):
#                 grades.remove(min(grades))
#         return sum(grades) / len(grades)
#     else:
#         return 0
#
# def has_duplicates(seq):
#     """
#     Check if a sequence contains duplicates
#     :param seq: (sequence) any sequence (string, list, or tuple)
#     :return: (boolean) True if the sequence contains duplicates
#     """
#     return len(seq) != len(set(seq))
#
# def remove_vowels(str):
#     """
#     Take a string and return another string with all the characters of
#     the original string except the vowels (a, e, i, o, u)
#     :param str: (string) a string
#     :return: (string) a new string without any vowels
#     """
#     return ''.join([c for c in str if c not in ['a', 'e', 'i', 'o', 'u',
#                                                 'A', 'E', 'I', 'O', 'U']])
#
# def same_word_count(str1, str2):
#     """
#     Check if two strings have the same number of words
#     :param str1: (string) the first string
#     :param str2: (string) the second string
#     :return: (boolean) True if two strings have the same number of words
#     """
#     return len(str1.split()) == len(str2.split())
#
# def main():
#     # You may use the main function to test your function definitions.
#     print(">>>>>>Question 1<<<<<<")
#     m = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9],
#          [0, 2, 4]]
#     print(transpose(m)) # [[1, 4, 7, 0], [2, 5, 8, 2], [3, 6, 9, 4]]
#     print(transpose([[1, 2, 3]])) # [[1], [2], [3]]
#     print(transpose([[1], [2], [3]])) # [[1, 2, 3]]
#     print(transpose ([[1]])) # [[1]]
#
#     print("")
#     print(">>>>>>Question 2<<<<<<")
#     anna = [100, 90, 60]
#     print(grader(threshold=2, grades=anna))  # 95.0
#     print(anna)  # [100, 90]
#
#     ryan = [80, 90, 81, 100, 100, 60, 70]
#     print(grader(ryan, 7))  # 83.0
#     print(ryan)  # [80, 90, 81, 100, 100, 60, 70]
#
#     alex = [100, 80, 60, 80]
#     print(grader(alex))  # 80.0
#     print(alex)  # [100, 80, 60, 80]
#
#     zoe = [100, 80, 60, 84, 94]
#     print(grader(zoe))  # 89.5
#     print(zoe)  # [100, 80, 84, 94]
#
#     print("")
#     print(">>>>>>Question 3<<<<<<")
#     print(has_duplicates('hello'))  # True
#     print(has_duplicates('python'))  # False
#     print(has_duplicates((1, 4, 2, 4)))  # True
#     print(has_duplicates([]))  # False
#
#     print("")
#     print(">>>>>>Question 4<<<<<<")
#     print(remove_vowels('Anticipation'))  # ntcptn
#     print(remove_vowels('PYTHON'))  # PYTHN
#     print(remove_vowels('Hello World!'))  # Hll Wrld!
#
#     print("")
#     print(">>>>>>Question 5<<<<<<")
#     print(same_word_count('Hello World!', 'Hi               there'))
#     # True
#     print(same_word_count('Hello  World!', 'Python is fun'))  # False
#
# if __name__ == '__main__':
#     main()

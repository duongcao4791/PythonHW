# ----------------------------------------------------------------------
# Name:    homework4
# Purpose: Practice Dictionaries, Comprehensions & Generator Expressions
#
# Author(s): Haitao Huang, Duong Cao
# ----------------------------------------------------------------------
"""
Implement various functions with dictionaries and generator expressions.

Q1: top_students
Q2: final_grade
Q3: boost_grade
Q4: word_lengths
Q5: geometric_sum
"""
import string


# Enter your 5 function definitions here
def top_students(grades, num=3):
    """
    Find the top n students with high grades.
    :param grades: (dictionary) containing student names and grades
    :param num: (number) number of top students wanted
    :return: (list) list of student names who have the top grades
    """
    return sorted(grades, key=grades.get, reverse=True)[0:num]


def final_grade(grades, extra_credit=1):
    """
    Add the extra credit to the student's grades and return a new
    dictionary after update.
    :param grades: (dictionary) containing student names and grades
    :param extra_credit: (number) extra credit points
    :return: (dictionary) student names and grades after update
    """
    return {name: grades[name] + extra_credit for name in grades}


def boost_grade(iclicker, exam):
    """
    Give the student a 1 point boost if the student's iclicker point is
    equal to or greater than the average, no boost otherwise.
    :param iclicker: (dictionary) representing iClicker points
    :param exam: (dictionary) representing student grades on the midterm
    :return: (dictionary) student names and midterm grades after update
    """
    student_set = {name for name in iclicker} | {name for name in exam}
    grades = {name: exam[name] if name in exam else 0
              for name in student_set}
    if iclicker:
        iclicker_avg = sum(iclicker.values()) / len(iclicker)
        grades = {name: grades[name] + 1 if name in iclicker and iclicker[name]
                                            >= iclicker_avg else grades[name]
                  for name in student_set}
    return grades


def word_lengths(str):
    """
    Find all words in the string and their lengths.
    :param str: (string) sentence(s)
    :return: (dictionary) words in the string and their lengths as value
    """
    return {word.strip(string.punctuation): len(word.strip(string.punctuation))
            for word in str.lower().split()}


def geometric_sum(n):
    """
    Create a generator and return the sum of all numbers generated.
    :param n: (number) a integer
    :return: (number) the sum of all numbers generated
    """
    return sum(1 / (2 ** x) for x in range(1, n + 1))


def main():
    # You may use the main function to test your function definitions.
    print('>>>>>>Question 1<<<<<<')
    empty_class = {}
    cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}
    print(top_students(cs122, 2))  # ['Anna', 'Alex']
    print(top_students(cs122))  # ['Anna', 'Alex', 'Zoe']
    print(top_students(cs122, 10))  # ['Anna', 'Alex', 'Zoe', 'Dan']
    print(cs122)  # {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}
    print(top_students(empty_class, 6))  # []

    print('')
    print('>>>>>>Question 2<<<<<<')
    empty_class = {}
    cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    print(final_grade(cs122))
    # {'Zoe':91, 'Alex': 94, 'Dan':80, 'Anna':101}
    print(final_grade(cs122, 2))
    # {'Zoe':92, 'Alex': 95, 'Dan':81, 'Anna':102}
    print(cs122)  # {'Zoe':90, 'Alex': 93, 'Dan':79, 'Anna':100}
    print(final_grade(empty_class, 5))  # {}

    print('')
    print('>>>>>>Question 3<<<<<<')
    iclicker = {'Zoe': 46, 'Alex': 121, 'Ryan': 100, 'Anna': 110,
                'Bryan': 2, 'Andrea': 110}
    exam = {'Dan': 89, 'Ryan': 89, 'Alex': 95, 'Anna': 64,
            'Bryan': 95, 'Andrea': 86}
    # the orders of the sample output dictionaries are not relevant
    print(boost_grade(iclicker, exam))
    # {'Bryan': 95, 'Zoe': 0, 'Anna': 65, 'Alex': 96, 'Ryan': 90,
    #  'Andrea': 87, 'Dan': 89}
    print(boost_grade({}, exam))
    # {'Ryan': 89, 'Andrea': 86, 'Bryan': 95, 'Anna': 64,
    #  'Dan': 89, 'Alex': 95}
    print(boost_grade(iclicker, {}))
    # {'Ryan': 1, 'Andrea': 1, 'Bryan': 0, 'Zoe': 0, 'Anna': 1,
    #  'Alex': 1}
    print(boost_grade({}, {}))  # {}

    print('')
    print('>>>>>>Question 4<<<<<<')
    phrase = '''Simple is better than     complex, and flat
                 IS BETTER than nested!?!'''
    print(word_lengths(''))  # {}
    print(word_lengths(phrase))
    # {'simple': 6, 'is': 2, 'better': 6, 'than': 4, 'complex': 7,
    #  'and': 3, 'flat': 4, 'nested': 6}

    print('')
    print('>>>>>>Question 5<<<<<<')
    print(geometric_sum(-5))  # 0
    print(geometric_sum(0))  # 0
    print(geometric_sum(1))  # 0.5
    print(geometric_sum(2))  # 0.75
    print(geometric_sum(3))  # 0.875
    print(geometric_sum(4))  # 0.9375
    print(geometric_sum(30))  # 0.9999999990686774


if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------
# Name:        homework3
# Purpose:     Practice Manipulating Sequence Data Types
#
# Author(s):    Duong Cao
# ----------------------------------------------------------------------
"""
Implement various functions to practice manipulating sequence data types

Q1: transpose
Q2: grader
Q3: has_duplicates
Q4: remove_vowels
Q5: same_word_count
"""


# Enter your 5 function definitions here
def transpose(m):
    return [[m[row][column] for row in range(len(m))]
            for column in range(len(m[0]))]


def grader(grades, threshold=4):
    if not grades:
        return 0
    else:
        if len(grades) > threshold:
            for i in range(len(grades) - threshold):
                grades.remove(min(grades))
        return sum(grades) / len(grades)


def has_duplicates(seq):
    return len(seq) != len(set(seq))


def remove_vowels(str):
    return ''.join([c for c in str if c.lower() not in ['a', 'e', 'i', 'o', 'u']])


def same_word_count(str1, str2):
    return len(str1.split()) != len(str2.split())


def main():
    # You may use the main function to test your function definitions.
    m1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [0, 2, 4]]
    print('QUESTION 1:')
    print(transpose(m1))
    print(transpose([[1, 2, 3]]))
    print(transpose([[1], [2], [3]]))
    print(transpose([[1]]))

    print('QUESTION 2:')
    anna = [100, 90, 60, 80]
    print(grader(threshold=2, grades=anna))  # 95.0
    print(anna)  # [100, 90]

    ryan = [80, 90, 81, 100, 100, 60, 70]
    print(grader(ryan, 7))  # 83.0
    print(ryan)  # [80, 90, 81, 100, 100, 60, 70]

    alex = [100, 80, 60, 80]
    print(grader(alex))  # 80.0
    print(alex)  # [100, 80, 60, 80]

    zoe = [100, 80, 60, 84, 94, 70]
    print(grader(zoe))  # 89.5
    print(zoe)  # [100, 80, 84, 94]

    print('QUESTION 3:')
    print(has_duplicates('hello'))  # True
    print(has_duplicates('python'))  # False
    print(has_duplicates((1, 4, 2, 4)))  # True
    print(has_duplicates([]))  # False

    print('QUESTION 4:')
    print(remove_vowels('Anticipation'))  # ntcptn
    print(remove_vowels('PYTHON'))  # PYTHN
    print(remove_vowels('Hello World!'))  # Hll Wrld!

    print('QUESTION 5:')
    print(same_word_count('Hello World!', 'Hi               there'))  # True
    print(same_word_count('Hello  World!', 'Python is fun'))  # False


if __name__ == '__main__':
    main()

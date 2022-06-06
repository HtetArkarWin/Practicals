"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():

    score = float(input("Enter score: "))
    print("{} mark is {}".format(score,evaluate_score(score)))

    score = random.randint(0, 100)
    print("{} mark is {}".format(score,evaluate_score(score)))

def evaluate_score(score):
    result=""
    if 90 <= score <= 100:
        result = "Excellent"
    elif 50 <= score < 90:
        result = "Passable"
    elif 0 <= score < 50:
        result = "Bad"
    else:
        result = "Invalid"
    return result


main()
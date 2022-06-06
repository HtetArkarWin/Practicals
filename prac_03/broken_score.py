"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():

    score = float(input("Enter score: "))
    print(evaluate_score(score))


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
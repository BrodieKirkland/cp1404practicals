
import random


def main():
    scores = []
    file_name = "results.txt"
    number_of_scores = int(input("Number of scores: "))
    for i in range(number_of_scores):
        random_score = random.randint(0, 100)
        scores.append(random_score)
    out_file = open(file_name, "w")
    for score in scores:
        print(f"{score} is {return_result(score)}", file=out_file)
    out_file.close()
    print(f"Saved {number_of_scores} scores to {file_name}")
    # score = float(input("Enter score: "))
    # result = return_result(score)
    # print(result)

    # i = random.randint(0, 100)
    # print(f"Random number: {i}, Result: {return_result(i)}")


def return_result(score):
    """return result"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()

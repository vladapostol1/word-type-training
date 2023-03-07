import pandas as pd
import matplotlib.pyplot as plt

def calculateScore(string1, string2, start, end):
    score = 0
    duration = end - start
    for i in range(0, len(string2)):
        if i < len(string1):
            if string2[i] == string1[i]:
                score = score + 1
    accuracy = score / len(string2) * 100
    if duration <= optimalTime(string2):
        score = accuracy
    else:
        score = optimalTime(string2)/duration * accuracy
    result = "Score: " + str(score) + "        Accuracy: " + str(accuracy) + "%"
    saveScoring(score, accuracy)
    return result

def optimalTime(string):
    return len(string) / 7

def saveScoring(score, accuracy):
    file = open("usrdata", "a")
    file.write(f'{score} {accuracy}\n')

def returnGraph():
    df = pd.read_table('usrdata', sep=' ', names=["Score", "Accuracy"])
    df.plot.scatter(x="Score", y="Accuracy", alpha=0.5)
    plt.show()




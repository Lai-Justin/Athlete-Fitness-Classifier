class NaiveBayesClassifier:
    def main():

        trainingFile = open("training.txt", "r")
        trainingData = []

        for line in trainingFile:
            tmp = trainingFile.readline().split(",")
            trainingData.insert(tmp)

        for line in trainingData:
            print(line)


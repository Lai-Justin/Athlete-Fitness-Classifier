import sys
import numpy as np
import time

results = {
        "Success" : 0,
        "Failure" : 0
    }
percentiles = []
trainingData = []

trainingData3D = np.zeros((2,11,4))


def training():

    trainingFile = open(sys.argv[1], "r")

    for line in trainingFile:
        tmp = line.split(",")
        trainingData.append(tmp)


    for entry in trainingData:
        if entry[11] == "1\n":
            results["Success"] += 1
        else:
            results["Failure"] += 1


    toGetPercentiles = [[],[],[],[],[],[],[],[],[],[],[]]

    for entry in trainingData:
        for i in range(11):
            if(i != 1):
                toGetPercentiles[i].append(float(entry[i]))





    percentiles.append([np.percentile(toGetPercentiles[0], 25), np.percentile(toGetPercentiles[0], 50), np.percentile(toGetPercentiles[0], 75), np.percentile(toGetPercentiles[0], 100)])
    percentiles.append([0])
    percentiles.append([np.percentile(toGetPercentiles[2], 25), np.percentile(toGetPercentiles[2], 50), np.percentile(toGetPercentiles[2], 75), np.percentile(toGetPercentiles[2], 100)])
    percentiles.append([np.percentile(toGetPercentiles[3], 25), np.percentile(toGetPercentiles[3], 50), np.percentile(toGetPercentiles[3], 75), np.percentile(toGetPercentiles[3], 100)])
    percentiles.append([np.percentile(toGetPercentiles[4], 25), np.percentile(toGetPercentiles[4], 50), np.percentile(toGetPercentiles[4], 75), np.percentile(toGetPercentiles[4], 100)])
    percentiles.append([np.percentile(toGetPercentiles[5], 25), np.percentile(toGetPercentiles[5], 50), np.percentile(toGetPercentiles[5], 75), np.percentile(toGetPercentiles[5], 100)])
    percentiles.append([np.percentile(toGetPercentiles[6], 25), np.percentile(toGetPercentiles[6], 50), np.percentile(toGetPercentiles[6], 75), np.percentile(toGetPercentiles[6], 100)])
    percentiles.append([np.percentile(toGetPercentiles[7], 25), np.percentile(toGetPercentiles[7], 50), np.percentile(toGetPercentiles[7], 75), np.percentile(toGetPercentiles[7], 100)])
    percentiles.append([np.percentile(toGetPercentiles[8], 25), np.percentile(toGetPercentiles[8], 50), np.percentile(toGetPercentiles[8], 75), np.percentile(toGetPercentiles[8], 100)])
    percentiles.append([np.percentile(toGetPercentiles[9], 25), np.percentile(toGetPercentiles[9], 50), np.percentile(toGetPercentiles[9], 75), np.percentile(toGetPercentiles[9], 100)])
    percentiles.append([np.percentile(toGetPercentiles[10], 25), np.percentile(toGetPercentiles[10], 50), np.percentile(toGetPercentiles[10], 75), np.percentile(toGetPercentiles[10], 100)])


    for entry in trainingData:
        for i in range(11):
            if(i == 1):
                if(entry[i] == 'M' and entry[11] == "1\n"):
                    trainingData3D[1][i][0] += 1
                elif(entry[i] == 'M' and entry[11] == "0\n"):
                    trainingData3D[0][i][0] += 1
                elif(entry[i] == 'F' and entry[11] == "1\n"):
                    trainingData3D[1][i][1] += 1
                elif(entry[i] == 'F' and entry[11] == "0\n"):
                    trainingData3D[0][i][1] += 1
            else:
                if(entry[11] == "1\n"):
                    for j in range(4):
                        if(float(entry[i]) <= percentiles[i][j]):
                            trainingData3D[1][i][j] += 1
                            break
                else:
                    for j in range(4):
                        if(float(entry[i]) <= percentiles[i][j]):
                            trainingData3D[0][i][j] += 1
                            break



    for i in range(2):
        for j in range(11):
            for k in range(4):
                if(i == 0):
                    trainingData3D[i][j][k] /= results["Failure"]
                else:
                    trainingData3D[i][j][k] /= results["Success"]
    
    

def testing():
    

    testingFile = open(sys.argv[2], "r")
    testingData = []

    for line in testingFile:
        tmp = line.split(",")
        testingData.append(tmp)

    testingResults = []

    tmpTrue = results["Success"] / len(trainingData)
    tmpFalse = results["Failure"] / len(trainingData)


    for entry in testingData:
        for i in range(11):
            if(i == 1):
                if(entry[i] == 'M'):
                    tmpTrue *= trainingData3D[1][1][0]
                    tmpFalse *= trainingData3D[0][1][0]
                elif(entry[i] == 'F'):
                    tmpTrue *= trainingData3D[1][1][1]
                    tmpFalse *= trainingData3D[0][1][1]
            else:
                for j in range(4):
                    if(float(entry[i]) <= percentiles[i][j]):
                        tmpTrue *= trainingData3D[1][i][j]
                        tmpFalse *= trainingData3D[0][i][j]
                        break
        if(tmpTrue > tmpFalse):
            testingResults.append(1) 
        else:
            testingResults.append(0)
        tmpTrue = 0.5
        tmpFalse = 0.5 

    res = 0
    for i in range(len(testingResults)):
        if testingResults[i] == int(testingData[i][11]):
            res += 1
    print(res / len(testingResults))






training()
testing()


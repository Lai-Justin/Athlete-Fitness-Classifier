import numpy as np



trainingFile = open("training.txt", "r")
trainingData = []

for line in trainingFile:
    tmp = line.split(",")
    trainingData.append(tmp)

results = {
    "Success" : 0,
    "Failure" : 0
}

for entry in trainingData:
    if entry[11] == "1\n":
        results["Success"] += 1
    else:
        results["Failure"] += 1


means = [[],[],[],[],[],[],[],[],[],[],[]]

for entry in trainingData:
    for i in range(11):
        if(i != 1):
            means[i].append(float(entry[i]))


percentiles = [
    [np.percentile(means[0], 25), np.percentile(means[0], 50), np.percentile(means[0], 75), np.percentile(means[0], 100)],
    [0], 
    [np.percentile(means[2], 25), np.percentile(means[2], 50), np.percentile(means[2], 75), np.percentile(means[2], 100)],
    [np.percentile(means[3], 25), np.percentile(means[3], 50), np.percentile(means[3], 75), np.percentile(means[3], 100)],
    [np.percentile(means[4], 25), np.percentile(means[4], 50), np.percentile(means[4], 75), np.percentile(means[4], 100)],
    [np.percentile(means[5], 25), np.percentile(means[5], 50), np.percentile(means[5], 75), np.percentile(means[5], 100)],
    [np.percentile(means[6], 25), np.percentile(means[6], 50), np.percentile(means[6], 75), np.percentile(means[6], 100)],
    [np.percentile(means[7], 25), np.percentile(means[7], 50), np.percentile(means[7], 75), np.percentile(means[7], 100)],
    [np.percentile(means[8], 25), np.percentile(means[8], 50), np.percentile(means[8], 75), np.percentile(means[8], 100)],
    [np.percentile(means[9], 25), np.percentile(means[9], 50), np.percentile(means[9], 75), np.percentile(means[9], 100)],
    [np.percentile(means[10], 25), np.percentile(means[10], 50), np.percentile(means[10], 75), np.percentile(means[10], 100)]
]

trainingData3D = np.zeros((2,11,4))

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



testingFile = open("testing.txt", "r")
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

print(testingResults)   

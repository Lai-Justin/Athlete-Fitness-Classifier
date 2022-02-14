trainingFile = open("training.txt", "r")
trainingData = []

for line in trainingFile:
    tmp = trainingFile.readline().split(",")
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

results["Success"] /= len(trainingData)
results["Failure"] /= len(trainingData)

for entry in results:
    print(results.get(entry))


genderStats = {
    "Success given male" : 0,
    "Success given female" : 0,
    "Failure given male" : 0,
    "Failure given female" : 0,
    "Prob s given m" : 0,
    "Prob s given f" : 0,
    "Prob f given m" : 0,
    "Prob f given f" : 0
}
for entry in trainingData:
    if entry[1] == 'M' and entry[11] == "1\n":
        genderStats["Success given male"] += 1
    elif entry[1] == 'M' and entry[11] == "0\n":
        genderStats["Failure given male"] += 1
    elif entry[1] == 'F' and entry[11] == "1\n":   
        genderStats["Success given female"] += 1
    elif entry[1] == 'F' and entry[11] == "0\n":
        genderStats["Failure given female"] += 1

genderStats["Success given male"] = (genderStats["Success given male"] / len(trainingData)) / results["Success"]
genderStats["Success given female"] = (genderStats["Success given female"] / len(trainingData)) / results["Success"]
genderStats["Failure given male"] = (genderStats["Failure given male"] / len(trainingData)) / results["Failure"]
genderStats["Failure given female"] = (genderStats["Failure given female"] / len(trainingData)) / results["Failure"]

for entry in genderStats:
    print(results.get(entry))

import os

path = "UET_175Data"
count = 0

for ID in os.listdir(path):
    for folder in os.listdir(path + "/" + ID):
        if folder.endswith(".json"):
            continue
        for file in os.listdir(path + "/" + ID + "/" + folder):
            if file.endswith(".csv"):
                count += 1

print(count)
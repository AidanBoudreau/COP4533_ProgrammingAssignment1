import sys
import os
from StudentHospital import Hospital, Student

# Check if input file exists
if os.path.getsize("input.txt") == 0:
    print("Input file is empty.")
    sys.exit()

# Read number of hospitals/students (first line)
file = open("input.txt")
firstLine = file.readline()
try:
    firstLine = int(firstLine)
except:
    print("Incorrect formatting for first line.")
    sys.exit()

# Read Hospital preferences
hospitalsUnmatched = []
for i in range(firstLine):
    currentLine = file.readline()
    if currentLine == "":
        print("Missing input lines.")
        sys.exit()
    currentLineAsList = currentLine.split(" ")
    if (len(currentLineAsList) != firstLine):
        print(f"Hospital {i+1} is missing preferences.")
        sys.exit()
    for j in range(firstLine):
        currentLineAsList[j] = int(currentLineAsList[j])
    hospitalsUnmatched.append(Hospital(currentLineAsList, i+1))

# Read student preferences
students = []
for i in range(firstLine):
    currentLine = file.readline()
    if currentLine == "":
        print("Missing input lines.")
        sys.exit()
    currentLineAsList = currentLine.split(" ")
    if (len(currentLineAsList) != firstLine):
        print(f"Student {i+1} is missing preferences.")
        sys.exit()
    for j in range(firstLine):
        currentLineAsList[j] = int(currentLineAsList[j])
    students.append(Student(currentLineAsList))

# Gale-Shapley Algorithm
while (len(hospitalsUnmatched) != 0):
    currentHospital = hospitalsUnmatched[0]
    a = currentHospital.preferences[0] - 1
    while True:
        if (not students[a].matched):
            students[a].matchTo(currentHospital)
            hospitalsUnmatched.pop(0)
            break
        elif (students[a].preferences.index(currentHospital.ID) < students[a].preferences.index(students[a].currentMatch.ID)):
            hospitalsUnmatched.append(students[a].currentMatch)
            students[a].matchTo(currentHospital)
            hospitalsUnmatched.pop(0)
            break
        else:
            a += 1

with open("matcherOutput.txt", "w") as f:
    for i in range(firstLine):
        f.write(str(i+1) + " " + str(students[i].currentMatch.ID) + "\n")
import sys
import os
from StudentHospital import Hospital, Student

if os.path.getsize("input.txt") == 0:
    print("Input file is empty.")
    sys.exit()

file = open("input.txt")
firstLine = file.readline()
try:
    firstLine = int(firstLine)
except:
    print("Incorrect formatting for first line.")
    sys.exit()

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

for i in range(firstLine):
    print(i+1, students[i].currentMatch.ID)
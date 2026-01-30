import sys
import os
from StudentHospital import Hospital, Student


# Check if input file exists
if os.path.getsize("matcherOutput.txt") == 0:
    print("Output file is empty.")
    sys.exit()


# Read matches from output file
file = open("matcherOutput.txt")
matches = []
for line in file:
    currentLineAsList = line.split(" ")
    if (len(currentLineAsList) != 2):
        print("Incorrect formatting in output file.")
        sys.exit()
    for j in range(2):
        currentLineAsList[j] = int(currentLineAsList[j])
    matches.append(currentLineAsList)


# Verify matches
for match in matches:
    hospitalID = match[0]
    studentID = match[1]
    if hospitalID < 1 or hospitalID > len(matches):
        print(f"Hospital ID {hospitalID} is out of range.")
        sys.exit()
    if studentID < 1 or studentID > len(matches):
        print(f"Student ID {studentID} is out of range.")
        sys.exit()


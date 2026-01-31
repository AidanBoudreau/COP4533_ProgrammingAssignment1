import os
from StudentHospital import Hospital, Student

#end program early with message
def endProgram(message):
    print(message)
    quit()

# Check if input file exists
message = ""
if os.path.getsize("input.txt") == 0:
    message = "Empty input file."
    endProgram(message)

# Read number of hospitals/students (first line)
file = open("input.txt")
n = file.readline()
try:
    n = int(n)
except:
    message = "Incorrect formatting for first line."
    endProgram(message)

# Read Hospital preferences by line and appending to list
hospitals = []
for row in range(1, n+1):
    line = file.readline()
    if not line:
        message = "Missing input lines." #not enough lines
        endProgram(message)
    preferences = line.split()
    if (len(preferences) != n):
        message = f"Hospital {row} is missing preferences." #not enough preferences
        endProgram(message)
    for col in range(n):
        preferences[col] = int(preferences[col])
    hospitals.append(Hospital(preferences, row))

# Read student preferences by line and appending to list
students = []
for row in range(1, n+1):
    line = file.readline()
    if not line:
        message = "Missing input lines." #not enough lines
        endProgram(message)
    preferences = line.split()
    if (len(preferences) != n):
        message = f"Student {row} is missing preferences." #not enough preferences
        endProgram(message)
    for col in range(n):
        preferences[col] = int(preferences[col])
    students.append(Student(preferences, row))

hospitalsUnmatched = hospitals.copy()

# Gale-Shapley Algorithm
while hospitalsUnmatched:
    currentHospital = hospitalsUnmatched[0]
    # propose to next student on preference list until matched
    while not currentHospital.matched:
        if currentHospital.nextProposalIndex >= n:
            message = "INVALID. No stable matching exists."
            endProgram(message)
        studentIndex = currentHospital.nextProposalIndex
        studentID = currentHospital.preferences[studentIndex]
        currentHospital.nextProposalIndex += 1
        student = students[studentID - 1]

        # if student is unmatched, match them
        if not student.matched:
            student.matchTo(currentHospital)
            currentHospital.matchTo(student)
            hospitalsUnmatched.pop(0)
        # if student is matched, see if they prefer new hospital
        else:
            currentMatch = student.currentMatch
            studentPrefs = student.preferences
            # if they prefer new hospital, rematch them
            if studentPrefs.index(currentHospital.ID) < studentPrefs.index(currentMatch.ID):
                currentMatch.unmatch()
                hospitalsUnmatched.append(currentMatch)
                student.matchTo(currentHospital)
                currentHospital.matchTo(student)
                hospitalsUnmatched.pop(0)
                break

# Write matches to output file
file.close()
file = open("output.txt", "w")
for hospital in hospitals:
    file.write(f"{hospital.ID} {hospital.currentMatch.ID}\n")
file.close()
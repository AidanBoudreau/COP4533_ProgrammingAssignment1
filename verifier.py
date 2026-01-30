import sys

# Read number of hospitals/students (first line)
file = open("input.txt")
n = file.readline()
if n == "":
    print("INVALID. Input file is empty.")
    sys.exit()
n = int(n)


# Read preferences into dictionaries
hospital_preferences = {}
student_preferences = {}
for i in range(n):
    currentLine = file.readline()
    currentLineAsList = currentLine.split()
    for j in range(n):
        currentLineAsList[j] = int(currentLineAsList[j])
    hospital_preferences[i + 1] = currentLineAsList
for i in range(n):
    currentLine = file.readline()
    currentLineAsList = currentLine.split()
    for j in range(n):
        currentLineAsList[j] = int(currentLineAsList[j])
    student_preferences[i + 1] = currentLineAsList


# Read matches from output file
file = open("matcherOutput.txt")
matches = []
for line in file:
    currentLineAsList = line.split()
    for j in range(2):
        currentLineAsList[j] = int(currentLineAsList[j])
    matches.append(currentLineAsList)


# validation checks
valid = True
# check correct number of matches
if len(matches) != n:
    valid = False
    print("INVALID. Number of matches does not equal number of hospitals/students.")
    sys.exit()

# load matches into maps and count frequencies
matchH = {}
matchS = {}
hospital_frequency = {}
student_frequency = {}
for match in matches:
    hospitalID = match[0]
    studentID = match[1]
    matchH[hospitalID] = studentID
    matchS[studentID] = hospitalID
    hospital_frequency[hospitalID] = hospital_frequency.get(hospitalID, 0) + 1
    student_frequency[studentID] = student_frequency.get(studentID, 0) + 1

    # check for out of range IDs (below 1 or above n)
    if hospitalID < 1 or hospitalID > n:
        print(f"INVALID. Hospital ID {hospitalID} is out of range.")
        valid = False
        sys.exit()
    if studentID < 1 or studentID > n:
        print(f"INVALID. Student ID {studentID} is out of range.")
        valid = False
        sys.exit()


# check for duplicates and unmatched
for i in range(1, n + 1):
    if hospital_frequency.get(i, 0) != 1:
        print(f"INVALID. Hospital {i} is matched {hospital_frequency.get(i, 0)} times.")
        valid = False
    elif student_frequency.get(i, 0) != 1:
        print(f"INVALID. Student {i} is matched {student_frequency.get(i, 0)} times.")
        valid = False

if valid == False:
    sys.exit()

    
# stability check (check if hospitals and students prefer each other over their current matches)
stable = True
blocking_pair = None

for hospital in range(1, n + 1):
    curr_student = matchH[hospital]
    curr_hospital_preference_list = hospital_preferences[hospital]

    preference_position = curr_hospital_preference_list.index(curr_student)
    #look at the preferable students' hospital preferences
    for more_preferable_student in curr_hospital_preference_list[:preference_position]:
        more_preferable_students_hospital = matchS[more_preferable_student]
        more_prefereble_students_preferences = student_preferences[more_preferable_student]

        # check if the more preferable student prefers this hospital over their current match
        current_hospital_position = more_prefereble_students_preferences.index(more_preferable_students_hospital)
        desired_hospital_position = more_prefereble_students_preferences.index(hospital)
        if desired_hospital_position < current_hospital_position:
            stable = False
            blocking_pair = (hospital, more_preferable_student)
            break

    if not stable:
        break

if valid and stable:
    print("VALID STABLE")
elif valid and not stable:
    print(f"UNSTABLE. Blocking pair: Hospital {blocking_pair[0]} and Student {blocking_pair[1]}")

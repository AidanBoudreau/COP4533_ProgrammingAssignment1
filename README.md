Aidan Boudreau (UFID:22043059)


## Instructions (Gale-Shapley Algorithm)
1. change input to a scenario in need of matching
2. run main.py
3. read output in matcherOutput.txt


## Input Format:
- **Line 1:**
first line: integer n, number of hospitals (proposal group) and students (accept/deny group)
- **next n lines:**
n lines: hospitals listing preffered students in decreasing order with space in between.
- **next n lines:**    
next n lines: students listing preferred hospitals in decreasing order with space in between.

## Example Input
3
2 1 3
1 2 3
3 2 1
1 2 3
2 3 1
3 1 2

## Output Format:
- **col 1:** Hospital
- **col 2:** Student
- **number of rows:** n
Each row represents a match between a hospital and a student

## Example Output:
1 2
2 3
3 1

This indicates:
- Hospital 1 is matched with Student 2  
- Hospital 2 is matched with Student 3  
- Hospital 3 is matched with Student 1  


## Scalability Analysis

![Scalability Graph](scalability.png)

## Observed Trend

For small vaues of n, the runtime of both the
matching engine and the verifier remains nearly constant. This behavior is caused by Python startup dominating execution time. At `n = 128`, the runtime increases more noticeably as the cost of
the matching and verification logic becomes significant.

The matcher and verifier exhibit similar growth rates across the tested
input sizes. The data shows that the execution time for the larger n sizes increases by almost a factor of 3. This makes sense due to the Big-Oh of Gale Shapley being O(n^2). 





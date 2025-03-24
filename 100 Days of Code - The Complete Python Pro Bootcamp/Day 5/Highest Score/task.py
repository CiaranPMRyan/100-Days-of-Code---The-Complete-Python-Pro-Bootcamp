student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# Max function

max_exam_score = max(student_scores) # Max function returns the highest number in a list

print(max_exam_score)

max_score = 0 # This is our starting value to use as a comparison

for score in student_scores: # Score will take the actual integer value.
    if score > max_score: # Here we compare the integer value stored in score and compare it with our variable
        max_score = score # Then we reassign the higher score to max_score

print(max_score)

# Sum function

total_exam_score = sum(student_scores) # Sum function returns everything added up

print(total_exam_score)

listSum = 0 # This is our starting value to hold the total sum

for score in student_scores: # Score will take the integer value each time according to the index
    listSum +=  score # Adds the current score value to the value held in listSum

print(listSum)
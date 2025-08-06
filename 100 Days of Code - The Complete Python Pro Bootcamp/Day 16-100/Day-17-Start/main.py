# Import the modules and classes needed

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#  Create an empty list for all the questions
question_bank = []

# Loop through the question data and put them into the list

# question_data is the name of the dictionary in the data file
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Feed the variables into the Question Init Method
    new_q = Question(question_text, question_answer)
    # Write the questions and answers into the list
    question_bank.append(new_q)

# prints out the whole dictionary to see what was written to it
# for item in range(len(question_bank)):
#     print(question_bank[item].text)
#     print(question_bank[item].answer)

# Create our object (instance) of the QuizBrain. We call it quiz. It needs the question bank to populate it
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    # Run the next_question Method from out object
    quiz.next_question()

quiz.final_score()
from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

for item in range(len(question_bank)):
    print(question_bank[item].text)
    print(question_bank[item].answer)


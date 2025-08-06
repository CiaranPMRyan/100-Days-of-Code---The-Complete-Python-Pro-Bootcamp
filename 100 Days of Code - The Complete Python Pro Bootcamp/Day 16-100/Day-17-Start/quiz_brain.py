class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Takes the question from the question_bank and uses 0 as the default index
        current_question = self.question_list[self.question_number]
        # Increments the question
        self.question_number += 1
        # Use the .text it will then tap into the actual text of the question from the q_list dictionary
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Yes! You got it right")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

    def final_score(self):
        print("You've completed the quiz")
        print(f"Your final score is {self.score}/{self.question_number}")

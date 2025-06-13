class QuizBrain:

    def __init__(self,  question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number != len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {current_question.text}: (True/False)?: ").title().strip()
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print(f"You got it right!\nYour current score is : {self.score}/{self.question_number}")
        else:
            print(f"You got it wrong!\nYour current score is : {self.score}/{self.question_number}")
        print(f"The correct answer is:  {correct_answer}\n")

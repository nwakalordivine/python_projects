import random

from question_model import Question
from quiz_brain import QuizBrain
import data
import random
question_bank = [
]

for questions in data.question_data:
    question = Question(questions["text"], questions["answer"])
    question_bank.append(question)

random.shuffle(question_bank)
quiz_brain = QuizBrain(question_list=question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score: {quiz_brain.score}/{len(quiz_brain.question_list)}")


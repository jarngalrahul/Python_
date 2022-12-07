from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# Creating list of objects of Question type
question_bank = []
for que in question_data:
    temp = Question(que["text"], que["answer"])
    question_bank.append(temp)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.retrieve_question()

print("You have completed the quiz.")
print(f"Your score is {quiz.score}/{quiz.question_number}")

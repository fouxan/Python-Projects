from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests

url = "https://opentdb.com/api.php"
params = {"amount": 10, "type": "boolean"}
response = requests.get(url, params=params).json()
question_data = response["results"]


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz_brain = QuizBrain(question_bank)
quiz = QuizInterface(quiz_brain)


from question_model import Question
from data import question_data
import random
# def create_question():
#     random_number = random.randint(0, 11)
#     q=Question()


question_bank = []
for n in range(12):
    question = Question(question_data[n]["text"],question_data[n]["answer"])
    question_bank.append(question)

for quest in question_bank:
    print(quest.question)



import data
class Question:

    def __init__(self,taxt,answer):
        self.question=taxt
        self.answer=answer
    def create_questions(self):
        question_bank = []
        for n in range(12):
            question_bank[n] = data.question_data[n]["text"]
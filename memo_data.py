class Form():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question 
        self.answer = answer 
        self.wrong_answer1 = wrong_ans1 
        self.wrong_answer2 = wrong_ans2 
        self.wrong_answer3 = wrong_ans3 

class FormView(Form):
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        super().__init__(question, answer, wrong_ans1, wrong_ans2, wrong_ans3)

    def show(self):
        print(self.question +
              self.answer + 
              self.wrong_answer1 + 
              self.wrong_answer2 + 
              self.wrong_answer3)
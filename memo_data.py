from contextlib import nullcontext
from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from memo_main_layout import *
from memo_edit_layout import *
from random import *

class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question 
        self.answer = answer 
        self.wrong_answer1 = wrong_ans1 
        self.wrong_answer2 = wrong_ans2 
        self.wrong_answer3 = wrong_ans3 
       
    
class FormModel():
    def __init__(self, lbl_question, rbtn_1, rbtn_2, rbtn_3, rbtn_4):
        self.lbl_question = lbl_question
        self.rbtn_1 = rbtn_1
        self.rbtn_2 = rbtn_2
        self.rbtn_3 = rbtn_3
        self.rbtn_4 = rbtn_4
        self.radio_btn_list = [self.rbtn_1, self.rbtn_2, self.rbtn_3, self.rbtn_4]
        self.count_asked = 0 
        self.count_right = 0 
    def shuffle(self):
        shuffle(self.radio_btn_list)
    def got_right(self):
        self.count_asked += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_asked += 1

class QuestionView(Question):
    ''' сопоставляет данные и виджеты для отображения вопроса'''
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3, frm_model):
        # конструктор получает и запоминает объект с данными и виджеты, соответствующие полям анкеты
        super().__init__(question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        
        self.frm_model = frm_model  # может получить и None - ничего страшного не случится, 
                                    # но для метода show нужно будет предварительно обновить данные методом change 
    def show(self):
        ''' выводит на экран все данные из объекта '''
        self.frm_model.lbl_question.setText(self.question)
        self.frm_model.radio_btn_list[0].setText(self.answer)
        self.frm_model.radio_btn_list[1].setText(self.wrong_answer1)
        self.frm_model.radio_btn_list[2].setText(self.wrong_answer2)
        self.frm_model.radio_btn_list[3].setText(self.wrong_answer3)

class AnswerCheck():
    ''' считая, что вопросы анкеты визуализируются чек-боксами, проверяет, выбран ли правильный ответ.'''
    def __init__(self, frm_model, lbl_correct, lbl_answer, lbl_test_result_asked, lbl_test_result_right):
        ''' запоминает все свойства. showed_answer - это виджет, в котором записывается правильный ответ (показывается позднее)
        result - это виджет, в который будет записан txt_right либо txt_wrong'''
        self.lbl_test_result_asked = lbl_test_result_asked
        self.lbl_test_result_right = lbl_test_result_right
        self.frm_model = frm_model
        self.lbl_correct = lbl_correct
        self.lbl_answer = lbl_answer
    def check(self):
        ''' ответ заносится в статистику, но переключение в форме не происходит: 
        этот класс ничего не знает про панели на форме '''
        correct = self.frm_model.radio_btn_list[0].isChecked()
        if correct:
            # ответ верный, запишем и отразим в статистике
            self.lbl_correct.setText('Відповідь правильна') # надпись "верно" или "неверно"
            self.lbl_answer.setText(self.frm_model.radio_btn_list[0].text()) # пишем сам текст ответа в соотв. виджете 
            self.frm_model.got_right() # обновить статистику, добавив один верный ответ
        else:
            incorrect = self.frm_model.radio_btn_list[1].isChecked() or self.frm_model.radio_btn_list[2].isChecked() or self.frm_model.radio_btn_list[3].isChecked()
            if incorrect:
                # ответ неверный, запишем и отразим в статистике
                self.lbl_correct.setText('Відповідь неправильна') # надпись "верно" или "неверно"
                self.lbl_answer.setText(self.frm_model.radio_btn_list[0].text()) # пишем сам текст ответа в соотв. виджете 
                self.frm_model.got_wrong() # обновить статистику, добавив неверный ответ
        self.lbl_test_result_asked.setText(str(self.frm_model.count_asked))
        self.lbl_test_result_right.setText(str(self.frm_model.count_right))       

class QuestionListModel():
    ''' в данных находится список объектов типа Question, 
    а также список активных вопросов, чтобы показывать его на экране '''
    def __init__(self):
        self.form_list = []
        self.asked_questions_list = []
    def rowCount(self):
        ''' число элементов для показа: обязательный метод для модели, с которой будет связан виджет "список"'''
        return len(self.form_list)
   
    def show_questionList(self):
        list_view.clear()
        for i in self.form_list:
            list_view.addItem(i.question)

    def add_question(self):
        new_question = Question(txt_question.text(),txt_answer.text(), txt_wrong_answer1.text(), txt_wrong_answer2.text(), txt_wrong_answer3.text())
        if new_question.question != '':
            self.form_list.append(new_question)
            txt_question.clear()
            txt_answer.clear()
            txt_wrong_answer1.clear()
            txt_wrong_answer2.clear()
            txt_wrong_answer3.clear()

    def delete_question(self):
        chosen = list_view.currentItem().text()
        txt_question.setText(chosen)
        for i in self.form_list:
            if i.question == chosen:
                self.form_list.remove(i)
                txt_question.clear()
                txt_answer.clear()
                txt_wrong_answer1.clear()
                txt_wrong_answer2.clear()
                txt_wrong_answer3.clear()

    def random_question(self):
        ''' Выдаёт случайный вопрос '''
        total = len(self.form_list)
        current = randint(0, total - 1)
        while current in self.asked_questions_list:
            current = randint(0, total - 1)
        self.asked_questions_list.append(current)
        return self.form_list[current]
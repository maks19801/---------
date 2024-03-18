from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt

from random import *

class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question 
        self.answer = answer 
        self.wrong_answer1 = wrong_ans1 
        self.wrong_answer2 = wrong_ans2 
        self.wrong_answer3 = wrong_ans3 
        self.actual = True 
        self.count_asked = 0 
        self.count_right = 0 
    def got_right(self):
        self.count_asked += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_asked += 1

class QuestionView(Question):
    ''' сопоставляет данные и виджеты для отображения вопроса'''
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        # конструктор получает и запоминает объект с данными и виджеты, соответствующие полям анкеты
        self.frm_model = frm_model  # может получить и None - ничего страшного не случится, 
                                    # но для метода show нужно будет предварительно обновить данные методом change
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3  
    def change(self, frm_model):
        ''' обновление данных, уже связанных с интерфейсом '''
        self.frm_model = frm_model
    def show(self):
        ''' выводит на экран все данные из объекта '''
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)

class AnswerCheck(QuestionView):
    ''' считая, что вопросы анкеты визуализируются чек-боксами, проверяет, выбран ли правильный ответ.'''
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3, showed_answer, result):
        ''' запоминает все свойства. showed_answer - это виджет, в котором записывается правильный ответ (показывается позднее)
        result - это виджет, в который будет записан txt_right либо txt_wrong'''
        super().init(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.showed_answer = showed_answer
        self.result = result
    def check(self):
        ''' ответ заносится в статистику, но переключение в форме не происходит: 
        этот класс ничего не знает про панели на форме '''
        if self.answer.isChecked():
            # ответ верный, запишем и отразим в статистике
            self.result.setText('Відповідь правильна') # надпись "верно" или "неверно"
            self.showed_answer.setText(self.frm_model.answer) # пишем сам текст ответа в соотв. виджете 
            self.frm_model.got_right() # обновить статистику, добавив один верный ответ
        else:
            # ответ неверный, запишем и отразим в статистике
            self.result.setText('Відповідь неправильна') # надпись "верно" или "неверно"
            self.showed_answer.setText(self.frm_model.answer) # пишем сам текст ответа в соотв. виджете 
            self.frm_model.got_wrong() # обновить статистику, добавив неверный ответ

class QuestionListModel(QAbstractListModel):
    ''' в данных находится список объектов типа Question, 
    а также список активных вопросов, чтобы показывать его на экране '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_list = []
    def rowCount(self, index):
        ''' число элементов для показа: обязательный метод для модели, с которой будет связан виджет "список"'''
        return len(self.form_list)
    def data(self, index, role):
        ''' обязательный метод для модели: какие данные она дает по запросу от интерфейса'''
        if role == Qt.DisplayRole:
            form = self.form_list[index.row()]
            return form.question
    def insertRows(self, parent=QModelIndex()):
        ''' этот метод вызывается, чтобы вставить в список объектов новые данные;
        генерируется и вставляется один пустой вопрос.'''
        position = len(self.form_list) 
        self.beginInsertRows(parent, position, position) 
        self.form_list.append(Question())
        self.endInsertRows()
        QModelIndex()
        return True 
    def removeRows(self, position, parent=QModelIndex()):
        ''' стандартный метод для удаления строк - после удаления из модели строка автоматически удаляется с экрана'''
        self.beginRemoveRows(parent, position, position) 
        self.form_list.pop(position) 
        self.endRemoveRows() 
        return True 
    def random_question(self):
        ''' Выдаёт случайный вопрос '''
        total = len(self.form_list)
        current = randint(0, total - 1)
        return self.form_list[current]
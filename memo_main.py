from memo_main_layout import *
from PyQt5.QtWidgets import QApplication, QWidget
from random import *
from memo_data import *
from memo_edit_layout import *

q_1 = Question('Яблуко','apple','application','building','caterpillar') 
q_2 = Question('Застосунок','application','apple','building','caterpillar') 
q_3 = Question('Будинок','building','application','apple','caterpillar') 
q_4 = Question('Гусінь','caterpillar','application','building','apple') 
q_5 = Question('Груша','pear','application','building','apple') 

questions_listmodel = QuestionListModel()

questions_listmodel.form_list.append(q_1)
questions_listmodel.form_list.append(q_2)
questions_listmodel.form_list.append(q_3)
questions_listmodel.form_list.append(q_4)
questions_listmodel.form_list.append(q_5)

frm_model = FormModel(lbl_question,rbtn_1, rbtn_2, rbtn_3, rbtn_4)

answer_check = AnswerCheck(frm_model, lbl_corect, lbl_answer, lbl_test_result_asked, lbl_test_result_right)

def start_training():
  main_win.hide()
  question_win.show()
  show_random_question()
  
def show_menu():
  question_win.hide()
  main_win.show()
  
def show_question_in_form():
  chosen = list_view.currentItem().text()
  txt_question.setText(chosen)
  for i in questions_listmodel.form_list:
    if i.question == chosen:
      txt_answer.setText(i.answer)
      txt_wrong_answer1.setText(i.wrong_answer1) 
      txt_wrong_answer2.setText(i.wrong_answer2)
      txt_wrong_answer3.setText(i.wrong_answer3)

def add_question():
  questions_listmodel.add_question()
  questions_listmodel.show_questionList()

def delete_question():
  questions_listmodel.delete_question()
  questions_listmodel.show_questionList()

def show_random_question():
  random_question = questions_listmodel.random_question()
  frm_model.shuffle()
  question_view = QuestionView(random_question.question, random_question.answer, random_question.wrong_answer1, random_question.wrong_answer2, random_question.wrong_answer3, frm_model)
  question_view.show()
  
  
def click_Ok():
  if btn_answer.text() != 'Наступне питання':
    answer_check.check()
    show_answer()
  else:
    if len(questions_listmodel.asked_questions_list) == len(questions_listmodel.form_list):
      show_test_result()
    else:
      show_question()
      show_random_question()
      
def app_sleep():
  question_win.hide()
  timer = QTimer()
  timer.singleShot(box_minutes.value() * 60 * 1000, start_training)

  
  


main_win = QWidget()
main_win.resize(600, 500)
main_win.setWindowTitle('Список питань')
main_win.setLayout(layout_edit_card)

questions_listmodel.show_questionList()
btn_start_training.clicked.connect(start_training)
btn_new_question.clicked.connect(add_question)
btn_delete_question.clicked.connect(delete_question)
list_view.itemClicked.connect(show_question_in_form)


question_win = QWidget()
question_win.resize(600, 500)
question_win.setWindowTitle('Memory Card')
question_win.setLayout(layout_card)
btn_answer.clicked.connect(click_Ok)
btn_menu.clicked.connect(show_menu)
btn_sleep.clicked.connect(app_sleep)


main_win.show()
app.exec_()
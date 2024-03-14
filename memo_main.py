from memo_main_layout import *
from PyQt5.QtWidgets import QApplication, QWidget
from random import *
from memo_data import *
from memo_edit_layout import *

q_1 = Form('Яблуко','apple','application','building','caterpillar') 


radio_btn_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_btn_list)

answer = radio_btn_list[0]
wrong_answer1, wrong_answer2, wrong_answer3 = radio_btn_list[1], radio_btn_list[2], radio_btn_list[3]

def start_training():
  main_win.hide()
  question_win.show()

def show_menu():
  question_win.hide()
  main_win.show()

def show_data():
  lbl_question.setText(q_1.question)
  answer.setText(q_1.answer)
  wrong_answer1.setText(q_1.wrong_answer1)
  wrong_answer2.setText(q_1.wrong_answer2)
  wrong_answer3.setText(q_1.wrong_answer3)

def check_result():
  correct = answer.isChecked()
  if correct:
    lbl_corect.setText('Правильна відповідь')
    lbl_answer.setText(answer.text())
    show_result()
  else:
    incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
    if incorrect:
      lbl_corect.setText('Відповідь неправильна')
      lbl_answer.setText(answer.text())
      show_result()


def click_Ok():
  if btn_answer.text() != 'Наступне питання':
    check_result()
  else:
    show_question()



main_win = QWidget()
main_win.resize(600, 500)
main_win.setWindowTitle('Список питань')
main_win.setLayout(layout_edit_card)

question_win = QWidget()
question_win.resize(600, 500)
question_win.setWindowTitle('Memory Card')
question_win.setLayout(layout_card)


show_data()
btn_start_training.clicked.connect(start_training)
btn_answer.clicked.connect(click_Ok)
btn_menu.clicked.connect(show_menu)
main_win.show()
app.exec_()
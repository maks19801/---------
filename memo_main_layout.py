from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QTableWidget, QListWidget, QListWidgetItem,
       QLineEdit, QFormLayout,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QButtonGroup, QRadioButton, 
       QPushButton, QLabel, QSpinBox)
from memo_data import Question

app = QApplication([])
btn_menu = QPushButton('Меню')
btn_sleep = QPushButton('Відпочити')
btn_answer = QPushButton('Відповісти')

box_minutes = QSpinBox()
box_minutes.setValue(5)

lbl_question = QLabel('')

radio_group_box = QGroupBox('Варіанти відповідей')
radio_group = QButtonGroup()

rbtn_1 = QRadioButton('') 
rbtn_2 = QRadioButton('') 
rbtn_3 = QRadioButton('') 
rbtn_4 = QRadioButton('') 

radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)

layout_h = QHBoxLayout()
layout_v1 = QVBoxLayout()
layout_v2 = QVBoxLayout()

layout_v1.addWidget(rbtn_1)
layout_v1.addWidget(rbtn_2)

layout_v2.addWidget(rbtn_3)
layout_v2.addWidget(rbtn_4)

layout_h.addLayout(layout_v1)
layout_h.addLayout(layout_v2)

radio_group_box.setLayout(layout_h)

answer_group_box = QGroupBox('Відповідь на питання')
lbl_corect = QLabel('')
lbl_answer = QLabel('')

layout_result = QVBoxLayout()
layout_result.addWidget(lbl_corect, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(lbl_answer, alignment= Qt.AlignHCenter, stretch=2)
answer_group_box.setLayout(layout_result)
answer_group_box.hide()

result_group_box = QGroupBox('Результат тесту')
lbl_test_result_asked = QLabel('')
lbl_test_result_right = QLabel('')

layout_test_result = QVBoxLayout()
layout_test_result.addWidget(QLabel('Заданих питань'))
layout_test_result.addWidget(lbl_test_result_asked, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_test_result.addWidget(QLabel('Правильних відповідей'))
layout_test_result.addWidget(lbl_test_result_right)
result_group_box.setLayout(layout_test_result)
result_group_box.hide()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_minutes)
layout_line1.addWidget(QLabel('хвилин'))

layout_line2.addWidget(lbl_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line3.addWidget(radio_group_box)
layout_line3.addWidget(answer_group_box)
layout_line3.addWidget(result_group_box)


layout_line4.addWidget(btn_answer, stretch=2)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_answer():
  radio_group_box.hide()
  answer_group_box.show()
  btn_answer.setText('Наступне питання')

def show_question():
  answer_group_box.hide()
  radio_group_box.show()
  btn_answer.setText('Відповісти')

  radio_group.setExclusive(False) 
  rbtn_1.setChecked(False)
  rbtn_2.setChecked(False)
  rbtn_3.setChecked(False)
  rbtn_4.setChecked(False)
  radio_group.setExclusive(True)
  

def show_test_result():
  answer_group_box.hide()
  result_group_box.show()
  lbl_question.hide()
  btn_answer.hide()
  



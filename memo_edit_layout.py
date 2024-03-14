from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QTableWidget, QListWidget, QListWidgetItem,
       QLineEdit, QFormLayout,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QButtonGroup, QRadioButton, 
       QPushButton, QLabel, QSpinBox)

app = QApplication([])
txt_question = QLineEdit('') 
txt_answer = QLineEdit('')
txt_wrong_answer1 = QLineEdit('') 
txt_wrong_answer2 = QLineEdit('')
txt_wrong_answer3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Запитання:', txt_question)
layout_form.addRow('Правильна відповідь:', txt_answer)
layout_form.addRow('Неправильна відповідь:', txt_wrong_answer1)
layout_form.addRow('Ще одна неправильна відповідь:', txt_wrong_answer2)
layout_form.addRow('І ще одна неправильна відповідь:', txt_wrong_answer3)

list_view = QListWidget()

btn_new_question = QPushButton('Нове питання')
btn_edit_question = QPushButton('Редагувати питання')
btn_start_training = QPushButton('Почати тренування')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(list_view)
layout_line1.addLayout(layout_form)

layout_line2.addWidget(btn_new_question)
layout_line2.addWidget(btn_edit_question)

layout_line3.addWidget(btn_start_training)

layout_edit_card = QVBoxLayout()
layout_edit_card.addLayout(layout_line1)
layout_edit_card.addLayout(layout_line2)
layout_edit_card.addLayout(layout_line3)


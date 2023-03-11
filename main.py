from PyQt5.QtWidgets import QApplication, QWidget
from card_layout import *
from data import *
from random import choice

# app = QApplication([])

card_width, card_height = 600, 500

window = QWidget()
window.resize(card_width, card_height)
window.setWindowTitle("Memory Card")
window.move(0, 0)

# тестове питання
# frm_question = "Яблуко"
# frm_right = "apple"
# frm_wr1 = "macintosh"
# frm_wr2 = "caterpillar"
# frm_wr3 = "jamm"

# def show_data():
#     quest_lb.setText(frm_question)
#     answ_lb.setText(frm_right)
#     shuffle(rbtn_list)
#     rbtn_list[0].setText(frm_right)
#     rbtn_list[1].setText(frm_wr1)
#     rbtn_list[2].setText(frm_wr2)
#     rbtn_list[3].setText(frm_wr3)
q = choice(q_list)
q.show(quest_lb, answ_lb, rbtn_list)

def check_result():
    if rbtn_group.checkedButton().text() == answ_lb.text():
        result_lb.setText("Вірно!")
    else:
        result_lb.setText("Невірно!") 

def ok_click():
    if ok_btn.text() == "Відповісти":
        if rbtn_group.checkedButton():
            check_result()
            show_result()
    else:
        q = choice(q_list)
        q.show(quest_lb, answ_lb, rbtn_list)
        show_quest()

ok_btn.clicked.connect(ok_click)    
# show_data()

window.show()

window.setLayout(layout_card)

app.exec_()

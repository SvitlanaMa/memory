from random import shuffle

class Question:
    def __init__(self, quest, right, wr1, wr2, wr3):
        self.quest = quest
        self.right = right
        self.wr1 = wr1
        self.wr2 = wr2
        self.wr3 = wr3
    
    def show(self, quest_lb, answ_lb, rbtn_list):
        quest_lb.setText(self.quest)
        answ_lb.setText(self.right)
        shuffle(rbtn_list)
        rbtn_list[0].setText(self.right)
        rbtn_list[1].setText(self.wr1)
        rbtn_list[2].setText(self.wr2)
        rbtn_list[3].setText(self.wr3)

q1 = Question("Яблуко", "apple", "macintosh", "caterpillar", "jamm")
q2 = Question("Дерево", "tree", "root", "groot", "three")
q3 = Question("Корова", "cow", "cat", "dog", "goat")
q4 = Question("Жаба", "frog", "ant", "dog", "vegetable")
q5 = Question("Червоний", "red", "blue", "green", "yellow")

q_list = [q1, q2, q3, q4, q5]

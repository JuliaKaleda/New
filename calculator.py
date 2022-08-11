from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import *
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = []
        self.operand_1 = []
        self.operand_2 = []

    def initUI(self):
        self.setGeometry(300, 300, 375, 570)
        self.setWindowTitle("Калькулятор")

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.resize(375, 95)
        self.move(0, 0)
        self.label.setFont(QFont('Times', 15))

        self.num_1 = QPushButton('1', self)
        self.num_1.resize(70, 70)
        self.num_1.move(5, 100)
        self.num_1.setFont(QFont('Times', 15))

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(70, 70)
        self.num_2.move(80, 100)
        self.num_2.setFont(QFont('Times', 15))

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(70, 70)
        self.num_3.move(155, 100)
        self.num_3.setFont(QFont('Times', 15))

        self.div = QPushButton('/', self)
        self.div.resize(70, 70)
        self.div.move(230, 100)
        self.div.setStyleSheet('QPushButton {background-color: orange}')
        self.div.setFont(QFont('Times', 15))

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(70, 70)
        self.num_4.move(5, 175)
        self.num_4.setFont(QFont('Times', 15))

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(70, 70)
        self.num_5.move(80, 175)
        self.num_5.setFont(QFont('Times', 15))

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(70, 70)
        self.num_6.move(155, 175)
        self.num_6.setFont(QFont('Times', 15))

        self.mul = QPushButton('*', self)
        self.mul.resize(70, 70)
        self.mul.move(230, 175)
        self.mul.setStyleSheet('QPushButton {background-color: orange}')
        self.mul.setFont(QFont('Times', 15))

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(70, 70)
        self.num_7.move(5, 250)
        self.num_7.setFont(QFont('Times', 15))

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(70, 70)
        self.num_8.move(80, 250)
        self.num_8.setFont(QFont('Times', 15))

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(70, 70)
        self.num_9.move(155, 250)
        self.num_9.setFont(QFont('Times', 15))

        self.plus = QPushButton('+', self)
        self.plus.resize(70, 70)
        self.plus.move(230, 250)
        self.plus.setStyleSheet('QPushButton {background-color: orange}')
        self.plus.setFont(QFont('Times', 15))

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(70, 70)
        self.num_0.move(5, 325)
        self.num_0.setFont(QFont('Times', 15))

        self.sqrt = QPushButton('√', self)
        self.sqrt.resize(70, 70)
        self.sqrt.move(80, 325)
        self.sqrt.setStyleSheet('QPushButton {background-color: orange}')
        self.sqrt.setFont(QFont('Times', 15))

        self.step = QPushButton('^', self)
        self.step.resize(70, 70)
        self.step.move(155, 325)
        self.step.setStyleSheet('QPushButton {background-color: orange}')
        self.step.setFont(QFont('Times', 15))

        self.minus = QPushButton('-', self)
        self.minus.resize(70, 70)
        self.minus.move(230, 325)
        self.minus.setStyleSheet('QPushButton {background-color: orange}')
        self.minus.setFont(QFont('Times', 15))

        self.perc = QPushButton('%', self)
        self.perc.resize(70, 70)
        self.perc.move(5, 400)
        self.perc.setStyleSheet('QPushButton {background-color: orange}')
        self.perc.setFont(QFont('Times', 15))

        self.diw = QPushButton('//', self)
        self.diw.resize(70, 70)
        self.diw.move(80, 400)
        self.diw.setStyleSheet('QPushButton {background-color: orange}')
        self.diw.setFont(QFont('Times', 15))

        self.squar = QPushButton('x²', self)
        self.squar.resize(70, 70)
        self.squar.move(155, 400)
        self.squar.setStyleSheet('QPushButton {background-color: orange}')
        self.squar.setFont(QFont('Times', 15))

        self.c = QPushButton('C', self)
        self.c.resize(70, 70)
        self.c.move(230, 400)
        self.c.setStyleSheet('QPushButton {background-color: red}')
        self.c.setFont(QFont('Times', 15))

        self.ravn = QPushButton('=', self)
        self.ravn.resize(295, 70)
        self.ravn.move(5, 475)
        self.ravn.setStyleSheet('QPushButton {background-color: red}')
        self.ravn.setFont(QFont('Times', 15))

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.mul.clicked.connect(self.mul_1)
        self.div.clicked.connect(self.div_1)
        self.step.clicked.connect(self.step_1)
        self.sqrt.clicked.connect(self.sqrt_1)
        self.perc.clicked.connect(self.perc_1)
        self.diw.clicked.connect(self.diw_1)
        self.squar.clicked.connect(self.squar_1)
        self.c.clicked.connect(self.clean)
        self.ravn.clicked.connect(self.ravno)

    def enterValue(self):
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def plus_1(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def minus_1(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def mul_1(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def div_1(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def step_1(self):
        self.operation = '^'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def sqrt_1(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def perc_1(self):
        self.operation = '%'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def diw_1(self):
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def squar_1(self):
        self.operation = 'x²'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def ravno(self):
        if self.operation == 'x²':
            self.rezult = self.operand_1 ** 2
            self.label.setText(str(self.rezult))
        self.operand_2 = float(self.label.text())
        if self.operation == '+':
            self.rezult = self.operand_1 + self.operand_2
        elif self.operation == '-':
            self.rezult = self.operand_1 - self.operand_2
        elif self.operation == '*':
            self.rezult = self.operand_1 * self.operand_2
        elif self.operation == '/':
            if self.operand_2 == 0:
                self.rezult = 'error'
            else:
                self.rezult = self.operand_1 / self.operand_2
        elif self.operation == '^':
            self.rezult = self.operand_1 ** self.operand_2
        elif self.operation == '√':
            self.rezult = self.operand_1 ** (1 / self.operand_2)
        elif self.operation == '%':
            self.rezult = self.operand_1 * (self.operand_2 / 100)
        elif self.operation == '//':
            self.rezult = self.operand_1 // self.operand_2

        self.label.setText(str(self.rezult))

    # def squar_1(self):
    #     if self.operation == 'x²':
    #         self.rezult = self.operand_1 ** 2
    #     self.label.setText(str(self.rezult))

    def clean(self):
        self.label.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())

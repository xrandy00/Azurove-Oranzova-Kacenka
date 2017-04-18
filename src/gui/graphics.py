#!/usr/bin/python3

##
# @file graphics.py
# File containing definitions of all buttons and connecting with logic.
#

import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QLabel)

from src.ui import logic

##
# @brief Class Graphics - contains methods that create GUI for calculator
class Graphics(QWidget):

    ##
    # @brief Constructor __init__ initialize objects from class QWidget
    def __init__(self):

        super().__init__()

        self.initUI()

    ##
    # @brief Create graphics look and print it as created window
    def initUI(self):

        self.equation = QLabel(str(logic.term), self)
        self.display = QLabel(str(logic.res), self)
        self.equation.setAlignment(QtCore.Qt.AlignRight)
        self.display.setAlignment(QtCore.Qt.AlignRight)

        self.equation.setFont(QtGui.QFont('Arial', 15))
        self.display.setFont(QtGui.QFont('SansSerif', font_size))


        self.btn1 = QPushButton("1", self)  # button 1
        self.btn2 = QPushButton("2", self)  # button 2
        self.btn3 = QPushButton("3", self)  # button 3
        self.btn4 = QPushButton("4", self)  # button 4
        self.btn5 = QPushButton("5", self)  # button 5
        self.btn6 = QPushButton("6", self)  # button 6
        self.btn7 = QPushButton("7", self)  # button 7
        self.btn8 = QPushButton("8", self)  # button 8
        self.btn9 = QPushButton("9", self)  # button 9
        self.btn0 = QPushButton("0", self)  # button 0
        self.btndot = QPushButton(".", self)  # button dot
        self.btnfact = QPushButton("!", self)  # button factorial
        self.btnce = QPushButton("CE", self)  # button CE
        self.btnadd = QPushButton("+", self)  # button addition
        self.btnsub = QPushButton("-", self)  # button substitution
        self.btnmul = QPushButton("*", self)  # button multiply
        self.btndiv = QPushButton("/", self)  # button division
        self.btnLbracket = QPushButton("(", self)  # button (
        self.btnRbracket = QPushButton(")", self)  # button )
        self.btnc = QPushButton("C", self)  # button C
        self.btnabs = QPushButton("abs", self)  # button abs
        self.btnsqrt = QPushButton("√", self)  # button sqrt
        self.btnneg = QPushButton("neg", self)  # button neg
        self.btnpow = QPushButton("^", self)  # button power
        self.btneq = QPushButton("=", self)  # button =

        self.equation.move(0, 0)
        self.display.move(0, 30)
        self.btnce.move(300, 90)

        self.btn1.move(0, 90)
        self.btn2.move(60, 90)
        self.btn3.move(120, 90)
        self.btnadd.move(180, 90)
        self.btnLbracket.move(240, 90)
        self.btnc.move(300, 30)

        self.btn4.move(0, 150)
        self.btn5.move(60, 150)
        self.btn6.move(120, 150)
        self.btnsub.move(180, 150)
        self.btnRbracket.move(240, 150)
        self.btnabs.move(300, 150)

        self.btn7.move(0, 210)
        self.btn8.move(60, 210)
        self.btn9.move(120, 210)
        self.btnmul.move(180, 210)
        self.btnsqrt.move(240, 210)
        self.btnneg.move(300, 210)

        self.btndot.move(0, 270)
        self.btn0.move(60, 270)
        self.btnfact.move(120, 270)
        self.btndiv.move(180, 270)
        self.btnpow.move(240, 270)
        self.btneq.move(300, 270)

        self.equation.setMinimumWidth(358)
        self.display.setMinimumWidth(298)
        self.btn1.setMaximumWidth(60)
        self.btn2.setMaximumWidth(60)
        self.btn3.setMaximumWidth(60)
        self.btn4.setMaximumWidth(60)
        self.btn5.setMaximumWidth(60)
        self.btn6.setMaximumWidth(60)
        self.btn7.setMaximumWidth(60)
        self.btn8.setMaximumWidth(60)
        self.btn9.setMaximumWidth(60)
        self.btn0.setMaximumWidth(60)
        self.btndot.setMaximumWidth(60)
        self.btnfact.setMaximumWidth(60)
        self.btnce.setMaximumWidth(60)
        self.btnadd.setMaximumWidth(60)
        self.btnsub.setMaximumWidth(60)
        self.btnmul.setMaximumWidth(60)
        self.btndiv.setMaximumWidth(60)
        self.btnLbracket.setMaximumWidth(60)
        self.btnRbracket.setMaximumWidth(60)
        self.btnc.setMaximumWidth(60)
        self.btnabs.setMaximumWidth(60)
        self.btnsqrt.setMaximumWidth(60)
        self.btnneg.setMaximumWidth(60)
        self.btnpow.setMaximumWidth(60)
        self.btneq.setMaximumWidth(60)

        self.equation.setMinimumHeight(30)
        self.display.setMinimumHeight(60)
        self.btn1.setMinimumHeight(60)
        self.btn2.setMinimumHeight(60)
        self.btn3.setMinimumHeight(60)
        self.btn4.setMinimumHeight(60)
        self.btn5.setMinimumHeight(60)
        self.btn6.setMinimumHeight(60)
        self.btn7.setMinimumHeight(60)
        self.btn8.setMinimumHeight(60)
        self.btn9.setMinimumHeight(60)
        self.btn0.setMinimumHeight(60)
        self.btndot.setMinimumHeight(60)
        self.btnfact.setMinimumHeight(60)
        self.btnce.setMinimumHeight(60)
        self.btnadd.setMinimumHeight(60)
        self.btnsub.setMinimumHeight(60)
        self.btnmul.setMinimumHeight(60)
        self.btndiv.setMinimumHeight(60)
        self.btnLbracket.setMinimumHeight(60)
        self.btnRbracket.setMinimumHeight(60)
        self.btnc.setMinimumHeight(60)
        self.btnabs.setMinimumHeight(60)
        self.btnsqrt.setMinimumHeight(60)
        self.btnneg.setMinimumHeight(60)
        self.btnpow.setMinimumHeight(60)
        self.btneq.setMinimumHeight(60)

        self.equation.setText(logic.term)

        # connect buttons with logic
        self.btn0.clicked.connect(self.make_handleButton('0'))
        self.btn1.clicked.connect(self.make_handleButton('1'))
        self.btn2.clicked.connect(self.make_handleButton('2'))
        self.btn3.clicked.connect(self.make_handleButton('3'))
        self.btn4.clicked.connect(self.make_handleButton('4'))
        self.btn5.clicked.connect(self.make_handleButton('5'))
        self.btn6.clicked.connect(self.make_handleButton('6'))
        self.btn7.clicked.connect(self.make_handleButton('7'))
        self.btn8.clicked.connect(self.make_handleButton('8'))
        self.btn9.clicked.connect(self.make_handleButton('9'))
        self.btndot.clicked.connect(self.make_handleButton('.'))
        self.btnneg.clicked.connect(self.make_handleButton('Neg'))
        self.btnabs.clicked.connect(self.make_handleButton('Abs'))
        self.btnfact.clicked.connect(self.make_handleButton('Fact'))
        self.btnadd.clicked.connect(self.make_handleButton('+'))
        self.btnsub.clicked.connect(self.make_handleButton('-'))
        self.btnmul.clicked.connect(self.make_handleButton('*'))
        self.btndiv.clicked.connect(self.make_handleButton('/'))
        self.btneq.clicked.connect(self.make_handleButton('='))
        self.btnc.clicked.connect(self.make_handleButton('Cls'))
        self.btnce.clicked.connect(self.make_handleButton('Bck'))
        self.btnsqrt.clicked.connect(self.make_handleButton('Sqrt'))
        self.btnLbracket.clicked.connect(self.make_handleButton('('))
        self.btnRbracket.clicked.connect(self.make_handleButton(')'))
        self.btnpow.clicked.connect(self.make_handleButton('Pow'))


        self.setFixedSize(360, 330)

        self.setWindowTitle('Calculator')

        self.show()


    ##
    # @brief Watching signal keyPressEvent and simulate click on specific button
    # @param qKeyEvent - signal from keyboard
    def keyPressEvent(self, qKeyEvent):

        key = qKeyEvent.key()
        # keys
        if key == QtCore.Qt.Key_0:
            self.btn0.click()
        elif key == QtCore.Qt.Key_1:
            self.btn1.click()
        elif key == QtCore.Qt.Key_2:
            self.btn2.click()
        elif key == QtCore.Qt.Key_3:
            self.btn3.click()
        elif key == QtCore.Qt.Key_4:
            self.btn4.click()
        elif key == QtCore.Qt.Key_5:
            self.btn5.click()
        elif key == QtCore.Qt.Key_6:
            self.btn6.click()
        elif key == QtCore.Qt.Key_7:
            self.btn7.click()
        elif key == QtCore.Qt.Key_8:
            self.btn8.click()
        elif key == QtCore.Qt.Key_9:
            self.btn9.click()

        # operators
        elif key == QtCore.Qt.Key_Enter:
            self.btneq.click()
        elif key == QtCore.Qt.Key_Return:
            self.btneq.click()
        elif key == QtCore.Qt.Key_Comma:
            self.btndot.click()
        elif key == QtCore.Qt.Key_Plus:
            self.btnadd.click()
        elif key == QtCore.Qt.Key_Minus:
            self.btnsub.click()
        elif key == QtCore.Qt.Key_Asterisk:
            self.btnmul.click()
        elif key == QtCore.Qt.Key_Slash:
            self.btndiv.click()
        elif key == QtCore.Qt.Key_Backspace:
            self.btnce.click()
        elif key == QtCore.Qt.Key_C:
            self.btnc.click()
        elif key == QtCore.Qt.Key_ParenLeft:
            self.btnLbracket.click()
        elif key == QtCore.Qt.Key_ParenRight:
            self.btnRbracket.click()

        # functions
        elif key == QtCore.Qt.Key_S:
            self.btnsqrt.click()
        elif key == QtCore.Qt.Key_P:
            self.btnpow.click()
        elif key == QtCore.Qt.Key_F:
            self.btnfact.click()
        elif key == QtCore.Qt.Key_Exclam:
            self.btnfact.click()
        elif key == QtCore.Qt.Key_N:
            self.btnneg.click()
        elif key == QtCore.Qt.Key_A:
            self.btnabs.click()

        # exit
        elif qKeyEvent.key() == QtCore.Qt.Key_Escape:
            self.close()
        else:
            pass


    ##
    # @brief Function connect logic with GUI
    # @param name - Value sent on event from GUI
    # @return - Inside function, that compare values
    def make_handleButton(self, name):

        ##
        # @brief Compare string sent on signal 'clicked' with value and calls appropriate function from logic
        def handleButton():

            if name in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                logic.num_pressed(name)
            elif name == 'Neg':
                logic.negate_pressed()
            elif name == 'Abs':
                logic.abs_pressed()
            elif name == 'Fact':
                logic.fact_pressed()
            elif name in ['+', '-', '*', '/']:
                logic.operator_pressed(name)
            elif name == 'Cls':
                logic.c_pressed()
            elif name == 'Pow':
                logic.operator_pressed('^')
            elif name == 'Bck':
                logic.ce_pressed()
            elif name == 'Sqrt':
                logic.sqrt_pressed()
            elif name == '(':
                logic.leftpar_pressed()
            elif name == ')':
                logic.rightpar_pressed()
            elif name == '=':
                logic.result()
            self.equation.setText(str(logic.term))
            self.display.setText(str(logic.res))
        return handleButton

# startup for app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("windows")
    ex = Graphics()
    sys.exit(app.exec_())
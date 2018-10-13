# Multiply by 11
# October 13, 2018, 12:45am
import random
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

class MainApp(QMainWindow):
        def __init__(self):
            super(MainApp,self).__init__()
            loadUi('11x.ui',self)
            self.setWindowTitle('Multipy by 11')
            self.nxtButton.clicked.connect(self.next)
            self.nxtButton.setAutoDefault(True)
            self.inproduct.returnPressed.connect(self.multy)
            self.radio1.setChecked(True)
            self.radio1.clicked.connect(self.radio1_button_clicked)
            self.radio2.clicked.connect(self.radio2_button_clicked)

        @pyqtSlot()

        def multy(self):
            #Generate random response if the answer is correct.
            correct = ["That is correct!", "Good Job!", "Well Done!", "Amazing!", "You're a Genius!"]

            #Generate random response if the answer is wrong.
            wrong =   ["Try Again.", "Incorrect.","Baby, one more time."]

            #Ask the user the answer for the addition question

            try:
                answer = int(self.inproduct.text())

            except ValueError:
                self.response.setText("Only Numbers are allowed. Click the Next button to continue.")
                return #Exit the def add function


            product = value1 * 11

            if (answer == product):
                self.response.setText(random.choice(correct))

            else:
                self.response.setText(random.choice(wrong) + ' Correct answer is ' + str(product) + '.')

            self.nxtButton.setFocus()

        def next(self):
            global product  # variables declare in functions are local only

            if self.radio1.isChecked():
                self.radio1_button_clicked()
            else:
                self.radio2_button_clicked()

            self.ranumb.setText(str(value1))
            self.inproduct.clear()
            self.response.clear()
            self.inproduct.setFocus()

        def radio1_button_clicked(self):
            global value1
            value1 = random.randint(0, 99)

        def radio2_button_clicked(self):
            global value1
            value1 = random.randint(100, 999)

value1 = 0
product = 0

app = QApplication(sys.argv)
widget = MainApp()
widget.show()
sys.exit(app.exec_())

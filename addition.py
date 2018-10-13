# Addition games
# Do not make sum as a variable. It's a built-in function
import random
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

class MainApp(QDialog):
        def __init__(self):
            super(MainApp,self).__init__()
            loadUi('addition.ui',self)
            self.setWindowTitle('Math Game')
            self.okButton.clicked.connect(self.add)
            self.nextButton.clicked.connect(self.next)

        @pyqtSlot()

        def add(self):
            #Generate random response if the answer is correct.
            correct = ["That is correct!", "Good Job!", "Well Done!", "Amazing!", "You're a Genius!"]

            #Generate random response if the answer is wrong.
            wrong =   ["Try Again.", "Incorrect.","Baby, one more time."]

            #Ask the user the answer for the addition question

            try:
                answer = int(self.inputsum.text())

            except ValueError:
                self.response.setText("Only Numbers are allowed. Click the Next button to continue.")
                return #Exit the def add function


            if (answer == total):
                self.response.setText(random.choice(correct))

            else:
                self.response.setText(random.choice(wrong) + ' Correct answer is ' + str(total) + '.')

        def next(self):
            #Generate up to 3 digit numbers to add

            global total  # variables declare in functions are local only
            value1 = random.randint(0, 100)
            value2 = random.randint(0, 100)
            total = value1 + value2

            self.lcd1.display(value1)
            self.lcd2.display(value2)
            self.inputsum.clear()
            self.response.clear()



total = 0

app = QApplication(sys.argv)
widget = MainApp()
widget.show()
sys.exit(app.exec_())

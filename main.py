import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 150)

        layout = QVBoxLayout()

        fnt = QFont('Open Sans', 120, QFont.Bold)

        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setFont(fnt)
        layout.addWidget(self.lbl)

        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000) # update every second

        self.showTime()

    def showTime(self):
        currentTime = QTime.currentTime()

        displayTxt = currentTime.toString('hh:mm:ss')
        print(displayTxt)

        self.lbl.setText(displayTxt)


app = QApplication(sys.argv)

demo = AppDemo()
demo.show()

app.exit(app.exec_())
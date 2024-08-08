# importing packages
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QHBoxLayout, QPushButton)


# Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Button Clicker')
        # self.setWindowIcon(QIcon('img.png')) u can add img.png ur own image if u want
        self.setGeometry(700, 300, 500, 500)

        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.label = QLabel('', self)
        self.initUI()

    # CSS
    def initUI(self):
        self.label.setGeometry(500 // 2, 50, 500, 100)
        self.label.setStyleSheet('font-size: 50px;'
                                 'font-family: Arial;'
                                 'color: blue;')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName('button1')
        self.button2.setObjectName('button2')
        self.button3.setObjectName('button3')

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font_family: Arial;
                padding: 15px 75px;
                margin: 25;
                border: 3px solid;
                border-radius: 15px
            }
            QPushButton#button1{
                background-color: hsl(11, 97%, 62%); 
            }
            QPushButton#button2{
                background-color: hsl(63, 97%, 62%); 
            }
            QPushButton#button3{
                background-color: hsl(128, 97%, 62%); 
            }

            QPushButton#button1:hover{
                background-color: hsl(11, 97%, 82%); 
            }
            QPushButton#button2:hover{
                background-color: hsl(63, 97%, 82%); 
            }
            QPushButton#button3:hover{
                background-color: hsl(128, 97%, 82%); 
            }
        """)

        self.button1.clicked.connect(self.on_click)
        self.button2.clicked.connect(self.on_click)
        self.button3.clicked.connect(self.on_click)

    def on_click(self):
        button = self.sender()
        self.label.setText(f'{button.text()} is clicked')


# Running window
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

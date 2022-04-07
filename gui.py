from turtle import window_height
from howdoi import howdoi
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Howdoi GUI")

        self.label = QLabel()       
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter your question")        

        self.button = QPushButton("Ask!")
        self.button.clicked.connect(self.do_question)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def do_question(self):
        question = self.input.text()  
        if question:   
            answer = howdoi.howdoi(question)
            self.label.setText(answer)

if __name__ == '__main__':       
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(350, 580)
    window.show()

    app.exec_()
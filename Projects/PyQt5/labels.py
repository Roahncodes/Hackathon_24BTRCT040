import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 GUI")
        self.resize(400, 300)
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: maroon;"
                            "background-color: turquoise;"
                            "font-weight: bold;"
                            "font-style: italic;") #Can also use rgb values or hexadecimal values of colours

# Create the application
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())

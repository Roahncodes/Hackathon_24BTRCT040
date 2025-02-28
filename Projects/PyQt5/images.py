import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 GUI")
        self.resize(400, 300)
        label = QLabel(self)
        label.setGeometry(00, 00, 400, 300)

        label.setScaledContents(True)

        pixmap = QPixmap("C:\\Users\\rohan\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-12-27 182637.png")
        label.setPixmap(pixmap)



# Create the application
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())

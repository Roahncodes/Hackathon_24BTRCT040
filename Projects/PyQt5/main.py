import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First PyQt5 GUI")
        self.resize(400, 300)
      

# Create the application
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())

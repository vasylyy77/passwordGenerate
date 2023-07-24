import sys


from PySide6.QtWidgets import QApplication, QMainWindow
from password_generation import Ui_MainWindow
from PySide6.QtTextToSpeech import QTextToSpeech
class NewWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewWindow()
    window.show()
    app.exec()


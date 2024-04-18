from windows.MainWindow import MainWindow
import sys
from PyQt6 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

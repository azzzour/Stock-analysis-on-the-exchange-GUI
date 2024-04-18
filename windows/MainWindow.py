from PyQt6 import QtWidgets, QtCore
from ui.mainUI import Ui_MainWindow as mainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = mainWindow()
        self.ui.setupUi(self)
        self.window().setWindowTitle("Stock price forecast")

        self.ui.dateTimeEdit.timeChanged.connect(self.validateTime)
        self.ui.enterButton.clicked.connect(self.sendData)

    def validateTime(self, time):
        if time.minute() % 5 != 0:
            correctedMinute = time.minute() // 5 * 5
            self.ui.dateTimeEdit.setTime(QtCore.QTime(time.hour(), correctedMinute))

    def sendData(self):
        selectedTime = self.ui.dateTimeEdit.time()
        if selectedTime < QtCore.QTime(4, 0):
            self.ui.dateTimeEdit.setTime(QtCore.QTime(4, 0))
            QtWidgets.QMessageBox.warning(self, "Внимание", "Время не может быть ранее 4:00.")
            return
        elif selectedTime > QtCore.QTime(20, 0):
            self.ui.dateTimeEdit.setTime(QtCore.QTime(20, 0))
            QtWidgets.QMessageBox.warning(self, "Внимание", "Время не может быть позднее 20:00.")
            return
        dateTime = self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-d h:mm")
        print(dateTime)




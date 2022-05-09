from PyQt5 import QtCore
from time import sleep


class CandyTime(QtCore.QThread):
    time_signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super(CandyTime, self).__init__()

    def run(self) -> None:
        cnt = 5
        while True:
            cnt -= 1
            if cnt < 0:
                break
            sleep(1)
            self.time_signal.emit(cnt)

from module.Element import GrilleCandy
from module.countertime import *
from PyQt5 import QtWidgets, QtGui
from win2 import Ui_MainWindow
from database.rank import Database
# def getData():
#     data = Database()
#     print(data.select())
class Window2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = Ui_MainWindow()
        self.win.setupUi(self)
class Candy(QtWidgets.QMainWindow):
    def __init__(self):
        super(Candy, self).__init__()
        # QtWidgets.QMainWindow.__init__(self)
        self.icons_dict = {
            1: 'icones/1.png',
            2: 'icones/2.png',
            3: 'icones/3.png',
            4: 'icones/4.png',
            5: 'icones/5.png',
            6: 'icones/6.png',
        }
        self.game = GrilleCandy()
        self.btn = [[QtWidgets.QPushButton("", self)
                     for _ in range(len(self.game.grille))] for _ in range(len(self.game.grille))]
        self.click = []
        self.timecandy = CandyTime()
        self.timecandy.time_signal.connect(self.getTime)

    def isBtnClicked(self):
        sender = self.sender()
        index = sender.value
        sender.setText("*")
        self.setClick(index)

    def setClick(self, index):
        if len(self.click) == 0:
            self.click.append(index)
        elif len(self.click) == 1:
            self.click.append(index)
            self.game.move(self.click[0][0], self.click[0][1], self.click[1][0], self.click[1][1])
            self.resetGrille()
        else:
            self.click = []
            self.click.append(index)

    def resetGrille(self):
        self.scoreLabel.setText(str(self.game.scores))
        for y in range(len(self.game.grille)):
            for i in range(len(self.game.grille)):
                self.btn[i][y].setText("")
                self.btn[i][y].setIcon(QtGui.QIcon(self.icons_dict[self.game.getItem(i, y)]))

    def getTime(self, value):
        time = value
        if time > 0:
            self.timecnt.setText(str(time))
        else:
            self.timecnt.setText('<b>' + 'Time out' + '</b>')
            for i in range(len(self.btn)):
                for y in range(len(self.btn)):
                    self.btn[i][y].setEnabled(False)
            self.username()

    def username(self):
        # name, dialog1 = QtWidgets.QInputDialog.getText(self, 'Greatt !!', 'Enter your name:')
        text, okPressed = QtWidgets.QInputDialog.getText(self, "Greatt!!", "Your name:", QtWidgets.QLineEdit.Normal, "")
        # if text and okPressed:
        #     print(text)
        self.showrank()
        # QtWidgets.QMainWindow.hide()
    def setupUI(self):
        self.timecandy.start()
        score = QtWidgets.QLabel('<b>' + 'Score' + '</b>', self)
        time = QtWidgets.QLabel('<b>' + 'Time' + '</b>', self)
        self.timecnt = QtWidgets.QLabel(str(5), self)
        self.timecnt.move(520, 20)
        score.move(480, 50)
        time.move(480, 20)
        self.scoreLabel = QtWidgets.QLabel(str(self.game.scores), self)
        self.scoreLabel.move(520, 50)
        for i in range(len(self.game.grille)):
            for y in range(len(self.game.grille)):
                self.btn[i][y].setFixedSize(50, 50)
                self.btn[i][y].move(50 * (y + 1), 50 * (i + 1))
                self.btn[i][y].setIcon(QtGui.QIcon(self.icons_dict[self.game.getItem(i, y)]))
                self.btn[i][y].clicked.connect(self.isBtnClicked)
                self.btn[i][y].value = [i, y]
        self.setGeometry(700, 300, 600, 500)
        self.setWindowTitle("Candy Crush Saga Python")
        iconWin = QtGui.QIcon("icones/1.png")
        self.setWindowIcon(iconWin)
        self.show()

    def showrank(self):
        # getData()
        self.w = Window2()
        self.w.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    candy = Candy()
    candy.setupUI()
    sys.exit(app.exec_())

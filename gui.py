import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon


class App(QMainWindow):

    def __init__(self, contest):
        super().__init__()
        self.title = 'Simple window'
        self.left = 100
        self.top = 130
        self.width = 640
        self.height = 480
        self.contest = contest
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('MEssage')
        button = QPushButton('Baton', self)
        button.setToolTip('Example')
        button.move(100, 70)
        button.clicked.connect(self.on_click)
        self.setFixedSize(self.size())
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Baton clicked!')
        for mg in self.contest.masters_list:
            print(mg.fullname, 'w', mg.room)
            for player in mg.players:
                print('-', player.fullname)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
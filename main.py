import resources
import gui
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    nerd_konkurs = resources.Contest('NERD')
    nerd_konkurs.load_masters()
    nerd_konkurs.load_players()
    nerd_konkurs.populate_sessions()

    app = QApplication(sys.argv)
    ex = gui.App(nerd_konkurs)
    print('Goodbye World')
    sys.exit(app.exec_())
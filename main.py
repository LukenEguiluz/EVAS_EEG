import sys
from PyQt6 import QtWidgets
from modulos.interfazInicio import MainWindow
from modulos.grabar import GrabarWidget

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
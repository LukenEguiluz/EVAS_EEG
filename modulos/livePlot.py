import sys
import numpy as np
from PyQt6 import QtWidgets
import pyqtgraph as pg

class PlotWindow(QtWidgets.QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 800, 600)

        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QtWidgets.QVBoxLayout(self.centralWidget)

        self.plotWidget = pg.PlotWidget()
        self.layout.addWidget(self.plotWidget)

        self.plotData = self.plotWidget.plot(pen='r')
        self.data = np.zeros(200)
        self.ptr = 0

        # Crear la barra azul
        self.bar = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen('b', width=2))
        self.plotWidget.addItem(self.bar)

        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.updatePlot)
        self.timer.start(50)

        # Botón para terminar la grabación o reproducción
        self.stopButton = QtWidgets.QPushButton('Terminar')
        self.stopButton.clicked.connect(self.close)
        self.layout.addWidget(self.stopButton)

    def updatePlot(self):
        self.data[self.ptr] = np.random.normal()  # Simulación de datos
        self.ptr += 1
        if self.ptr >= self.data.shape[0]:
            self.ptr = 0
        self.plotData.setData(self.data)
        
        # Actualizar la posición de la barra azul
        self.bar.setPos(self.ptr)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = PlotWindow('Live Plot')
    mainWin.show()
    sys.exit(app.exec())
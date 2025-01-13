import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from modulos.grabar import GrabarWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Interfaz de Inicio')
        self.setGeometry(100, 100, 800, 600)

        # Crear el widget central
        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)

        # Layout principal
        self.layout = QtWidgets.QVBoxLayout(self.centralWidget)

        # Layout para los botones
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.layout.addStretch(1)
        self.layout.addLayout(self.buttonLayout)
        self.layout.addStretch(1)

        # Botón Grabar
        self.recordButton = QtWidgets.QPushButton('Grabar')
        self.buttonLayout.addStretch(1)
        self.buttonLayout.addWidget(self.recordButton)
        self.buttonLayout.addStretch(1)

        # Botón Reproducir
        self.playButton = QtWidgets.QPushButton('Reproducir')
        self.buttonLayout.addWidget(self.playButton)
        self.buttonLayout.addStretch(1)

        # Logos
        self.logo1 = QtWidgets.QLabel(self)
        self.setLogo(self.logo1, 'images/Logo Biomedica.png', 10, 10)

        self.logo2 = QtWidgets.QLabel(self)
        self.setLogo(self.logo2, 'images/Logo EVAS.png', 740, 10)

        self.logo3 = QtWidgets.QLabel(self)
        self.setLogo(self.logo3, 'images/Logo EVAS.png', 740, 540)

        # Conectar el botón Grabar a la función para mostrar los dropdowns
        self.recordButton.clicked.connect(self.showDropdowns)

    def setLogo(self, label, imagePath, x, y):
        pixmap = QtGui.QPixmap(imagePath)
        if not pixmap.isNull():
            label.setPixmap(pixmap.scaled(50, 50, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
            label.setGeometry(x, y, 50, 50)
        else:
            print(f"Error: No se pudo cargar la imagen {imagePath}")

    def showDropdowns(self):
        # Cambiar al widget de grabación
        self.grabarWidget = GrabarWidget(self)
        self.setCentralWidget(self.grabarWidget)

    def showMainMenu(self):
        # Restaurar el widget central original
        self.setCentralWidget(self.centralWidget)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
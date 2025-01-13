import json
import serial.tools.list_ports
from PyQt6 import QtWidgets

class ReproducirWidget(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow  # Guardamos la referencia a la ventana principal
        self.initUI()

    def initUI(self):
        # Layout del nuevo widget
        layout = QtWidgets.QVBoxLayout(self)

        # Botón para seleccionar el archivo JSON
        self.selectFileButton = QtWidgets.QPushButton('Seleccionar Archivo JSON')
        self.selectFileButton.clicked.connect(self.selectFile)
        layout.addWidget(self.selectFileButton)

        # Campo de texto para mostrar el nombre
        self.nameLabel = QtWidgets.QLabel('Nombre:')
        self.nameInput = QtWidgets.QLineEdit()
        self.nameInput.setReadOnly(True)
        layout.addWidget(self.nameLabel)
        layout.addWidget(self.nameInput)

        # Campo de texto para mostrar la fecha
        self.dateLabel = QtWidgets.QLabel('Fecha:')
        self.dateInput = QtWidgets.QLineEdit()
        self.dateInput.setReadOnly(True)
        layout.addWidget(self.dateLabel)
        layout.addWidget(self.dateInput)

        # Dropdown para los LEDs RGB
        self.ledDropdown = QtWidgets.QComboBox()
        self.ledDropdown.addItems(self.getSerialPorts())
        self.ledDropdown.showPopup = self.createShowPopup(self.ledDropdown)
        layout.addWidget(QtWidgets.QLabel('Seleccionar LEDs RGB:'))
        layout.addWidget(self.ledDropdown)

        # Botón para iniciar la reproducción
        self.startPlaybackButton = QtWidgets.QPushButton('Iniciar Reproducción')
        layout.addWidget(self.startPlaybackButton)

        # Botón para regresar al inicio
        self.backButton = QtWidgets.QPushButton('Regresar al Inicio')
        self.backButton.clicked.connect(self.returnToMainMenu)
        layout.addWidget(self.backButton)

    def selectFile(self):
        # Abrir un diálogo para seleccionar el archivo JSON
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Seleccionar Archivo JSON", "", "Archivos JSON (*.json)", options=options)
        if fileName:
            self.loadJsonData(fileName)

    def loadJsonData(self, fileName):
        # Cargar los datos del archivo JSON
        with open(fileName, 'r') as file:
            data = json.load(file)
            self.nameInput.setText(data.get('nombre', ''))
            self.dateInput.setText(data.get('fecha', ''))

    def getSerialPorts(self):
        # Obtener la lista de puertos seriales disponibles
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def createShowPopup(self, comboBox):
        # Crear una función para actualizar los elementos del dropdown antes de mostrarlo
        originalShowPopup = comboBox.showPopup
        def showPopup():
            comboBox.clear()
            comboBox.addItems(self.getSerialPorts())
            originalShowPopup()
        return showPopup

    def returnToMainMenu(self):
        # Ocultar el widget de reproducción y mostrar el menú principal
        self.hide()
        self.mainWindow.showMainMenu()
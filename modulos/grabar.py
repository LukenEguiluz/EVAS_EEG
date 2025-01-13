import serial.tools.list_ports
from PyQt6 import QtWidgets
from modulos.livePlot import PlotWindow  # Importar PlotWindow

class GrabarWidget(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow  # Guardamos la referencia a la ventana principal
        self.initUI()

    def initUI(self):
        # Layout del nuevo widget
        dropdownLayout = QtWidgets.QVBoxLayout(self)

        # Campo de texto para el nombre
        self.nameInput = QtWidgets.QLineEdit()
        self.nameInput.setPlaceholderText('Ingrese su nombre')
        dropdownLayout.addWidget(QtWidgets.QLabel('Nombre:'))
        dropdownLayout.addWidget(self.nameInput)

        # Dropdown para el dispositivo EEG
        self.eegDropdown = QtWidgets.QComboBox()
        self.eegDropdown.addItems(self.getSerialPorts())
        self.eegDropdown.showPopup = self.createShowPopup(self.eegDropdown)
        dropdownLayout.addWidget(QtWidgets.QLabel('Seleccionar Dispositivo EEG:'))
        dropdownLayout.addWidget(self.eegDropdown)

        # Dropdown para los LEDs RGB
        self.ledDropdown = QtWidgets.QComboBox()
        self.ledDropdown.addItems(self.getSerialPorts())
        self.ledDropdown.showPopup = self.createShowPopup(self.ledDropdown)
        dropdownLayout.addWidget(QtWidgets.QLabel('Seleccionar LEDs RGB:'))
        dropdownLayout.addWidget(self.ledDropdown)

        # Botón para iniciar la grabación
        self.startRecordingButton = QtWidgets.QPushButton('Iniciar Grabación')
        self.startRecordingButton.clicked.connect(self.startRecording)
        dropdownLayout.addWidget(self.startRecordingButton)

        # Botón para regresar al inicio
        self.backButton = QtWidgets.QPushButton('Regresar al Inicio')
        self.backButton.clicked.connect(self.returnToMainMenu)
        dropdownLayout.addWidget(self.backButton)

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

    def startRecording(self):
        self.plotWindow = PlotWindow('Grabación en Vivo')
        self.plotWindow.show()

    def returnToMainMenu(self):
        # Ocultar el widget de grabación y mostrar el menú principal
        self.hide()
        self.mainWindow.showMainMenu()
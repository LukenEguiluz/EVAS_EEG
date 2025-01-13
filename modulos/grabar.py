import serial.tools.list_ports
from PyQt6 import QtWidgets

class GrabarWidget(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.initUI()

    def initUI(self):
        # Layout del nuevo widget
        dropdownLayout = QtWidgets.QVBoxLayout(self)

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
        dropdownLayout.addWidget(self.startRecordingButton)

        # Botón para regresar al inicio
        self.backButton = QtWidgets.QPushButton('Regresar al Inicio')
        self.backButton.clicked.connect(self.mainWindow.showMainMenu)
        dropdownLayout.addWidget(self.backButton)

    def getSerialPorts(self):
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def createShowPopup(self, comboBox):
        originalShowPopup = comboBox.showPopup
        def showPopup():
            comboBox.clear()
            comboBox.addItems(self.getSerialPorts())
            originalShowPopup()
        return showPopup
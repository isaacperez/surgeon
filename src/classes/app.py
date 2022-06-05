"""
This file creates the QApplication, and displays the main window

"""
from PyQt5.QtWidgets import QApplication, QWidget


class SurgeonApp(QApplication):
    """The primary QApplication subclass for Surgeon."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
    def gui(self):
        # Create main window
        self.mainWindow = QWidget()

        self.mainWindow.setGeometry(0, 0, 350, 400)
        self.mainWindow.setWindowTitle('Hello World')

        self.mainWindow.show()

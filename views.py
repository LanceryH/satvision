from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtWebEngineWidgets import QWebEngineView
import parameters as params
import os
import subprocess
dir_path = os.path.dirname(os.path.realpath(__file__))

class Window_3D(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.dad = None
        loadUi(dir_path +"\\ui\\window_3D.ui",self)
        layout = QVBoxLayout()
        self.webviewframe = QWebEngineView(self.widget)
        layout.addWidget(self.webviewframe)
        self.webviewframe.setUrl(QUrl(params.URL_3D))
        self.webviewframe.setGeometry(QRect(0, 0, self.widget.width(), self.widget.height()))
        self.setLayout(layout)
        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)
        self.show()
    def closeEvent(self, event):
        self.dad.action_3D_window.setChecked(False)
        
class Window_2D(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.dad = None
        loadUi(dir_path +"\\ui\\window_2D.ui",self)
        layout = QVBoxLayout()
        self.webviewframe = QWebEngineView(self.widget)
        layout.addWidget(self.webviewframe)
        self.webviewframe.setUrl(QUrl(params.URL_2D))
        self.webviewframe.setGeometry(QRect(0, 0, self.widget.width(), self.widget.height()))
        self.setLayout(layout)
        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)
        self.show()
    def closeEvent(self, event):
        self.dad.action_2D_window.setChecked(False)
        
class Window_Rocket(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        loadUi(dir_path +"\\ui\\window_rocket.ui",self)
        self.show()
        
class Window_Nozzle(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        loadUi(dir_path +"\\ui\\window_nozzle.ui",self)
        self.show()
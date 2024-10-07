from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class Window_3D(QWidget):
    def __init__(self):
        super().__init__()
        self.dad = None
        loadUi(dir_path +"/window/3d_view.ui",self)
        layout = QVBoxLayout()
        self.webviewframe = QWebEngineView(self.widget)
        layout.addWidget(self.webviewframe)
        self.webviewframe.setUrl(QUrl("http://127.0.0.1:5000"))
        self.webviewframe.setGeometry(QRect(0, 0, self.widget.width(), self.widget.height()))
        self.setLayout(layout)
        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)
        self.show()
        
    def closeEvent(self, event):
        self.dad.menuView3D.setChecked(False)
        self.dad.socketio.emit('send_message', "Closed 3D View")

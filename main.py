import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from socketio import Client
from interface import *
import subprocess

if __name__ == '__main__':
    sprocess = subprocess.Popen("python server.py")    
    app = QApplication(sys.argv)
    window = MyQtApp()
    window.show()
    sys.exit(app.exec_())       
    
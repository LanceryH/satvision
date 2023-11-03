import os
from pathlib import Path
import sys

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView


CURRENT_DIRECTORY = Path(__file__).resolve().parent


class webView(QWidget):
    def __init__(self):
        super(webView, self).__init__()
        

        filename = os.fspath(CURRENT_DIRECTORY / "index_py.html")
        url = QUrl.fromLocalFile(filename)
        
        self.webV = QWebEngineView()
        def test1(percent):
            print(percent)
        self.webV.loadProgress.connect(test1)
        def test2(success):
            print(success)
        self.webV.loadFinished.connect(test2)
        self.webV.load(url)

        layout = QVBoxLayout(self)
        layout.addWidget(self.webV)

        print (self.size())

if __name__ == "__main__":
    app = QApplication([])

    web = webView()
    web.show()

    sys.exit(app.exec())
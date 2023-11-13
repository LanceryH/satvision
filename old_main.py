import os
from pathlib import Path
import sys
import re
import requests
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView

CURRENT_DIRECTORY = Path(__file__).resolve().parent
CELESTRAK_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=csv"

class WebView(QWidget):
    def __init__(self):
        super(WebView, self).__init__()

        filename = os.fspath(CURRENT_DIRECTORY / "index.html")
        url = QUrl.fromLocalFile(filename)

        self.webV = QWebEngineView()
        def test1(percent):
            print(percent)
        self.webV.loadProgress.connect(test1)
        def test2(success):
            print(success)
        self.webV.loadFinished.connect(test2)
        self.webV.load(url)

        # Create two buttons
        self.left_button = QPushButton("Left Button")
        self.right_button = QPushButton("Update")

        self.right_button.clicked.connect(self.button_clicked)

        # Create a layout for the buttons in a column
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.left_button)
        buttons_layout.addWidget(self.right_button)

        # Create a layout for the buttons and the web view in a horizontal row
        layout = QHBoxLayout(self)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.webV)

    def button_clicked(self):
        # Replace this URL with the actual CSV file URL you want to download

        # Send an HTTP GET request to download the CSV file
        response = requests.get(CELESTRAK_URL)
        data = response.text

        if response.status_code == 200:
            # Replace 'downloaded.csv' with the desired local file name
            with open('satvision/downloaded.csv', 'w') as file:
                file.write(data)
            print("CSV file downloaded successfully")
        else:
            print("Failed to download CSV file")

if __name__ == "__main__":
    app = QApplication([])

    web = WebView()
    web.show()

    sys.exit(app.exec())

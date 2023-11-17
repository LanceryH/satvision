from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(250, 10, 541, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setEnabled(True)
        self.tab_1.setObjectName("tab_1")
        self.webviewframe = QWebEngineView(self.tab_1)
        self.webviewframe.load(QUrl(url_1))
        self.webviewframe.setGeometry(QtCore.QRect(10, 10, 517, 404))
        self.webviewframe.setObjectName("webviewframe")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 430, 517, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        #self.webviewframe_3 = QWebEngineView(self.groupBox_4)
        #self.webviewframe_3.load(QUrl(url_3))
        #self.webviewframe_3.setGeometry(QtCore.QRect(10, 20, 491, 61))
        #self.webviewframe_3.setObjectName("webviewframe_3")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.webviewframe_2 = QWebEngineView(self.tab_2)
        self.webviewframe_2.load(QUrl(url_2))
        self.webviewframe_2.setGeometry(QtCore.QRect(10, 10, 511, 204))
        self.webviewframe_2.setObjectName("webviewframe_2")
        self.widget_4 = QtWidgets.QWidget(self.tab_2)
        self.widget_4.setGeometry(QtCore.QRect(10, 260, 511, 261))
        self.widget_4.setObjectName("widget_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 231, 551))
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 211, 81))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButton_func)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(100, 20, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.activated.connect(self.comboBox_func)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 101, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pushButton_func_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 211, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.webviewframe_4 = QWebEngineView(self.groupBox_2)
        self.webviewframe_4.load(QUrl(url_3))
        self.webviewframe_4.setGeometry(QtCore.QRect(10, 30, 191, 171))
        self.webviewframe_4.setObjectName("webviewframe_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 330, 211, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 40, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        dt = QtCore.QDateTime(int(data[0]["EPOCH"][0:4]), int(data[0]["EPOCH"][5:7]), int(data[0]["EPOCH"][8:10]), int(data[0]["EPOCH"][11:13]), int(data[0]["EPOCH"][14:16])) 
        self.dateTimeEdit.setDateTime(dt) 
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox_3)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(10, 100, 194, 22))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        dt2 = QtCore.QDateTime(int(data[0]["EPOCH"][0:4]), int(data[0]["EPOCH"][5:7]), int(data[0]["EPOCH"][8:10])+2, int(data[0]["EPOCH"][11:13]), int(data[0]["EPOCH"][14:16])) 
        self.dateTimeEdit_2.setDateTime(dt2) 
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 80, 181, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 181, 16))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(20, 140, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.checked_func)
        self.checkBox.setChecked(True)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 140, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pushButton_func_3)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar.setGeometry(QtCore.QRect(10, 520, 211, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        for index in list_sat_name:
            self.comboBox.addItem(index)
    
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pushButton_func_2(self): 
        response = requests.get("https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json")
        data = response.text

        if response.status_code == 200:
            # Replace 'downloaded.csv' with the desired local file name
            with open('satvision/data.json', 'w') as file:
                file.write(data)
            print("Done")
        else:
            print("Error")

    def checked_func(self):
        return

    def comboBox_func(self): 
        with open('satvision/param.json', 'w') as f:
            json.dump([{"val":self.comboBox.currentIndex(),
                        "date":str(self.dateTimeEdit.dateTime()).split("(")[1].split(")")[0].split(","),
                        "live":self.checkBox.checkState(),
                        "Dt":str(self.dateTimeEdit_2.dateTime()).split("(")[1].split(")")[0].split(",")}], f)

    def pushButton_func(self): 
        self.webviewframe.load(QUrl(url_1))
        #self.webviewframe.reload() 
        self.webviewframe_2.load(QUrl(url_2))
        #self.webviewframe_2.reload() 
        self.webviewframe_4.load(QUrl(url_3))

    def pushButton_func_3(self): 
        with open('satvision/param.json', 'w') as f:
            json.dump([{"val":self.comboBox.currentIndex(),
                        "date":str(self.dateTimeEdit.dateTime()).split("(")[1].split(")")[0].split(","),
                        "live":self.checkBox.checkState(),
                        "Dt":str(self.dateTimeEdit_2.dateTime()).split("(")[1].split(")")[0].split(",")}], f)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "GroupBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "3D"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "2D"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Parameters"))
        self.groupBox.setTitle(_translate("MainWindow", "Satellite"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_2.setText(_translate("MainWindow", "Update"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Live data"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Time set"))
        self.label.setText(_translate("MainWindow", "End Time"))
        self.label_2.setText(_translate("MainWindow", "Start Time"))
        self.checkBox.setText(_translate("MainWindow", "Live Time"))
        self.pushButton_3.setText(_translate("MainWindow", "Validate"))

if __name__ == "__main__":
    import sys
    import subprocess
    import os
    import json
    import requests

    list_sat_name=[]

    with open('satvision/data.json') as json_file:
        data = json.load(json_file)

    with open('satvision/param.json', 'w') as f:
            json.dump([{"val":0,
                        "date":["0", " 0", " 0", " 0", " 0"],
                        "live":2,
                        "Dt":["0", " 0", " 0", " 0", " 0"]}], f)
            
    for index in range(8000):
        list_sat_name.append(data[index]["OBJECT_NAME"])

    url_1 = "http://localhost:7221/satvision/js_1/index.html"
    url_2 = "http://localhost:7221/satvision/js_2/index.html"
    url_3 = "http://localhost:7221/satvision/js_3/index.html"
    subprocess.Popen("python -m http.server 7221")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
#C:\Users\hugol\AppData\Roaming\Python\Python311\Scripts>pyuic5.exe -x C:\Users\hugol\Documents\JavaScript\satvision\ui\window.ui
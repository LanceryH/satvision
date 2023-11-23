from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

data = {'col1':['1','2','3','4'],
        'col2':['1','2','1','3'],
        'col3':['1','1','2','1']}


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
        self.webviewframe.setUrl(QUrl(url_1))
        self.webviewframe.setGeometry(QtCore.QRect(10, 10, 517, 404))
        self.webviewframe.setObjectName("webviewframe")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 430, 517, 91))
        self.groupBox_4.setObjectName("groupBox_4") 
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 491, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 491, 31))
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.webviewframe_2 = QWebEngineView(self.tab_2)
        self.webviewframe_2.setUrl(QUrl(url_2))
        self.webviewframe_2.setGeometry(QtCore.QRect(10, 10, 511, 204))
        self.webviewframe_2.setObjectName("webviewframe_2")
        self.widget_4 = QtWidgets.QWidget(self.tab_2)
        self.widget_4.setGeometry(QtCore.QRect(10, 260, 511, 261))
        self.widget_4.setObjectName("widget_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.widget_5 = QtWidgets.QWidget(self.tab_3)
        self.widget_5.setGeometry(QtCore.QRect(10, 260, 511, 261))
        self.widget_5.setObjectName("widget_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 10, 511, 241))
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 40, 71, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 40, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_6)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 251, 161))
        self.tableWidget.setObjectName("tableWidget")
        self.createTable()
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(100, 20, 111, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 40, 73, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(["1","2","3"])
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(190, 20, 71, 16))
        self.label_7.setObjectName("label_7")
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
        self.webviewframe_4.setUrl(QUrl(url_3))
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
        dt2 = QtCore.QDateTime(int(data[0]["EPOCH"][0:4]), int(data[0]["EPOCH"][5:7]), int(data[0]["EPOCH"][8:10]), int(data[0]["EPOCH"][11:13])+2, int(data[0]["EPOCH"][14:16])) 
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
        response_map = requests.get("https://clouds.matteason.co.uk/images/8192x4096/earth.jpg", stream = True)
        response = requests.get("https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json")
        data = response.text

        if response.status_code == 200:
            # Replace 'downloaded.csv' with the desired local file name
            with open('satvision/map_earth.jpg','wb') as f:
                shutil.copyfileobj(response_map.raw, f)
            print("Done")
        else:
            print("Error")

        if response.status_code == 200:
            # Replace 'downloaded.csv' with the desired local file name
            with open('satvision/data.json', 'w') as file:
                file.write(data)
            print("Done")
            with open('satvision/code_saved.json', 'w') as f:
                json.dump([{ "Update_date": str(date.today()) }], f)
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Mission"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Parameters"))
        self.groupBox.setTitle(_translate("MainWindow", "Satellite"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_2.setText(_translate("MainWindow", "Update"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Live data"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Time set"))
        self.label.setText(_translate("MainWindow", "End Time 🔵"))
        self.label_2.setText(_translate("MainWindow", "Start Time 🟢"))
        self.checkBox.setText(_translate("MainWindow", "Live Time "))
        self.pushButton_3.setText(_translate("MainWindow", "Validate"))
        with open('satvision/code_saved.json') as json_file:
            update_date = json.load(json_file)
        self.label_8.setText(_translate("MainWindow", f"Last update: {update_date[0]['Update_date']}"))
        self.label_9.setText(_translate("MainWindow", "Help: We are in Live"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Launch parameters"))
        self.label_3.setText(_translate("MainWindow", "Launch site"))
        self.label_5.setText(_translate("MainWindow", "Orbit Inclination"))
        self.label_7.setText(_translate("MainWindow", "Stages"))

    def createTable(self):   
        #Row count 
        self.tableWidget.setRowCount(4)  
  
        #Column count 
        self.tableWidget.setColumnCount(2)   
  
        self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Name")) 
        self.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("City")) 
        self.tableWidget.setItem(1,0, QtWidgets.QTableWidgetItem("Aloysius")) 
        self.tableWidget.setItem(1,1, QtWidgets.QTableWidgetItem("Indore")) 
        self.tableWidget.setItem(2,0, QtWidgets.QTableWidgetItem("Alan")) 
        self.tableWidget.setItem(2,1, QtWidgets.QTableWidgetItem("Bhopal")) 
        self.tableWidget.setItem(3,0, QtWidgets.QTableWidgetItem("Arnavi")) 
        self.tableWidget.setItem(3,1, QtWidgets.QTableWidgetItem("Mandsaur")) 
   
        #Table will fit the screen horizontally 
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) 
        
if __name__ == "__main__":
    import shutil
    import sys
    import subprocess
    import os
    import json
    import requests
    from datetime import date

    list_sat_name=[]

    with open('satvision/data.json') as json_file:
        data = json.load(json_file)

    with open('satvision/param.json', 'w') as f:
            json.dump([{"val":0,
                        "date":["0", " 0", " 0", " 0", " 0"],
                        "live":2,
                        "Dt":["0", " 0", " 0", " 0", " 0"]}], f)
            
    for index in range(80):
        list_sat_name.append(data[index]["OBJECT_NAME"])

    url_1 = "http://localhost:8201/satvision/js_1/index.html"
    url_2 = "http://localhost:8201/satvision/js_2/index.html"
    url_3 = "http://localhost:8201/satvision/js_3/index.html"
    subprocess.Popen("python -m http.server 8201")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
#C:\Users\hugol\AppData\Roaming\Python\Python311\Scripts>pyuic5.exe -x C:\Users\hugol\Documents\JavaScript\satvision\ui\window.ui
import subprocess
import sys
import requests
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem
from PyQt5.QtCore import QUrl, QRect, QDateTime
from PyQt5.uic import loadUi
from PyQt5.QtWebEngineWidgets import QWebEngineView
from parameters import *

class MyQtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(path +"/ui/window.ui",self)

        #self.webviewframe = QWebEngineView(self.groupBox)
        #self.webviewframe.setUrl(QUrl(URL_0D))
        #self.webviewframe.setGeometry(QRect(10, 10, 0, 0))
        #self.webviewframe.setObjectName("webviewframe")
        self.webviewframe_2 = QWebEngineView(self.widget)
        self.webviewframe_2.setUrl(QUrl(URL_3D))
        self.webviewframe_2.setGeometry(QRect(0, 0, 581, 491))
        self.webviewframe_2.setObjectName("webviewframe_2")
        self.webviewframe_3 = QWebEngineView(self.widget_2)
        self.webviewframe_3.setUrl(QUrl(URL_2D))
        self.webviewframe_3.setGeometry(QRect(0, 0, 581, 491))
        self.webviewframe_3.setObjectName("webviewframe_3")
        self.actionUpdate.triggered.connect(self.actionUpdate_func)
        self.actionValidate.triggered.connect(self.actionValidate_func)
        self.actionRefresh.triggered.connect(self.actionRefresh_func)
        self.radioButton.toggled.connect(self.radioButton_func) 
        self.comboBox.currentIndexChanged.connect(self.comboBox_func) 
        self.comboBox.addItems(["Satellite","Launcher"])  
        self.comboBox_2.currentIndexChanged.connect(self.comboBox_2_func) 
        dt = QDateTime(int(data[0]["EPOCH"][0:4]), int(data[0]["EPOCH"][5:7]), int(data[0]["EPOCH"][8:10]), int(data[0]["EPOCH"][11:13]), int(data[0]["EPOCH"][14:16])) 
        dt2 = QDateTime(int(data[0]["EPOCH"][0:4]), int(data[0]["EPOCH"][5:7]), int(data[0]["EPOCH"][8:10]), int(data[0]["EPOCH"][11:13])+2, int(data[0]["EPOCH"][14:16])) 
        self.dateTimeEdit.setDateTime(dt) 
        self.dateTimeEdit_2.setDateTime(dt2) 

        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.header().setVisible(False)

        itemTop1 = QTreeWidgetItem(self.treeWidget)
        itemTop1.setText(0,"QAbstractItemView")
        itemChild1 = QTreeWidgetItem(itemTop1)
        itemChild1.setText(0,"QListView")
        itemChild2 = QTreeWidgetItem(itemTop1)
        itemChild2.setText(0,"QTreeView")

        itemTop2 = QTreeWidgetItem(self.treeWidget)
        itemTop2.setText(0,"QAbstractItemModel")
        itemChild3 = QTreeWidgetItem(itemTop2)
        itemChild3.setText(0,"QListModel")
        itemChild4 = QTreeWidgetItem(itemChild3)
        itemChild4.setText(0,"QStringListModel")


        self.show()

    def actionUpdate_func(self):
        response = requests.get(URL_CELESTRAK)
        data = response.text

        if response.status_code == 200:
            with open(path +'/data.json', 'w') as file:
                file.write(data)
                print("Done")
        else:
            print("Error")


    def actionRefresh_func(self):
        #self.webviewframe.load(QUrl(URL_0D))
        self.webviewframe_2.load(QUrl(URL_3D))
        self.webviewframe_3.load(QUrl(URL_2D))

    def actionValidate_func(self):
        if self.radioButton.isChecked()==True:
            with open(path +'/param.json', 'w') as f:
                json.dump({"val":self.comboBox_2.currentIndex(),
                            "date":str(self.dateTimeEdit.dateTime()).split("(")[1].split(")")[0].split(","),
                            "live":2,
                            "Dt":str(self.dateTimeEdit_2.dateTime()).split("(")[1].split(")")[0].split(",")}, f) 
        else:   
            with open(path +'/param.json', 'w') as f:
                json.dump({"val":self.comboBox_2.currentIndex(),
                            "date":str(self.dateTimeEdit.dateTime()).split("(")[1].split(")")[0].split(","),
                            "live":0,
                            "Dt":str(self.dateTimeEdit_2.dateTime()).split("(")[1].split(")")[0].split(",")}, f) 
        print("wrote")

    def radioButton_func(self):
        if self.radioButton.isChecked()==True:
            self.dateTimeEdit.setEnabled(False)
            self.dateTimeEdit_2.setEnabled(False)
        else:
            self.dateTimeEdit.setEnabled(True)
            self.dateTimeEdit_2.setEnabled(True)
        return

    def comboBox_func(self):
        if self.comboBox.currentText()=="Satellite":
            self.comboBox_2.addItems(list_sat_name)  
        else:
            return

    def comboBox_2_func(self):
        return
            
if __name__ == '__main__':
    
    path = "C:/Users/Lance/Documents/Codes_win/JavaScript/satvision1.0"
    list_sat_name = []
    with open(path + '/data.json', 'r') as file:
        data = json.load(file)  
    for index in range(800):
        list_sat_name.append(data[index]["OBJECT_NAME"])
    subprocess.Popen("python -m http.server "+str(PORT))
    app = QApplication(sys.argv)
    ui = MyQtApp()
    ui.show()
    app.exec_()


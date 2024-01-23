import subprocess
import sys
import requests
import json
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem
from PyQt5.QtCore import QUrl, QRect, QDateTime
from PyQt5.uic import loadUi
from PyQt5.QtWebEngineWidgets import QWebEngineView
from source import parameters as params

class MyQtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(dir_path +"\\ui\\window.ui",self)

        self.webviewframe_2 = QWebEngineView(self.widget)
        self.webviewframe_2.setUrl(QUrl(params.URL_3D))
        self.webviewframe_2.setGeometry(QRect(0, 0, 581, 491))
        self.webviewframe_2.setObjectName("webviewframe_2")
        self.webviewframe_3 = QWebEngineView(self.widget_2)
        self.webviewframe_3.setUrl(QUrl(params.URL_2D))
        self.webviewframe_3.setGeometry(QRect(0, 0, 581, 491))
        self.webviewframe_3.setObjectName("webviewframe_3")
        self.actionUpdate.triggered.connect(self.actionUpdate_func)
        self.actionValidate.triggered.connect(self.actionValidate_func)
        self.actionRefresh.triggered.connect(self.actionRefresh_func)
        self.radioButton.toggled.connect(self.radioButton_func) 
        self.pushButton.clicked.connect(self.pushButton_func)
        self.pushButton_2.clicked.connect(self.pushButton_2_func)
        self.comboBox.currentIndexChanged.connect(self.comboBox_func) 
        self.comboBox.addItems(["Satellite","Launcher"])  
        self.comboBox_2.currentIndexChanged.connect(self.comboBox_2_func) 
        dt = QDateTime(int(data[0]["EPOCH"][0:4]), int(data[0]["EPOCH"][5:7]), int(data[0]["EPOCH"][8:10]), int(data[0]["EPOCH"][11:13]), int(data[0]["EPOCH"][14:16])) 
        dt2 = QDateTime(int(data[0]["EPOCH"][0:4]), int(data[0]["EPOCH"][5:7]), int(data[0]["EPOCH"][8:10]), int(data[0]["EPOCH"][11:13])+2, int(data[0]["EPOCH"][14:16])) 
        self.dateTimeEdit.setDateTime(dt) 
        self.dateTimeEdit_2.setDateTime(dt2) 

        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.header().setVisible(False)
        self.parent_tree = QTreeWidgetItem(self.treeWidget,["Scenario"])

        self.show()

    def actionUpdate_func(self):
        response = requests.get(params.URL_CELESTRAK)
        data = response.text

        if response.status_code == 200:
            with open(dir_path +'\\jsons\\data.json', 'w') as file:
                file.write(data)
                print("Done")
        else:
            print("Error")


    def actionRefresh_func(self):
        self.webviewframe_2.load(QUrl(params.URL_3D))   
        self.webviewframe_3.load(QUrl(params.URL_2D))

    def actionValidate_func(self):
        try:
            list_of_obj = []
            for i in range(self.parent_tree.childCount()):
                list_of_obj.append(str(self.parent_tree.child(i).text(1)))
            if self.radioButton.isChecked()==True:
                with open(dir_path + '\\jsons\\param.json', 'w') as f:
                    json.dump([{"val":list_of_obj,
                                "date":str(self.dateTimeEdit.dateTime()).split("(")[1].split(")")[0].split(","),
                                "live":2,
                                "Dt":str(self.dateTimeEdit_2.dateTime()).split("(")[1].split(")")[0].split(",")}], f) 
            else:   
                with open(dir_path + '\\jsons\\param.json', 'w') as f:
                    json.dump([{"val":list_of_obj,
                                "date":str(self.dateTimeEdit.dateTime()).split("(")[1].split(")")[0].split(","),
                                "live":0,
                                "Dt":str(self.dateTimeEdit_2.dateTime()).split("(")[1].split(")")[0].split(",")}], f) 
            print("wrote")
        except:
            pass

    def radioButton_func(self):
        if self.radioButton.isChecked()==True:
            self.dateTimeEdit_2.setEnabled(False)
            self.dateTimeEdit.setEnabled(False)
        else:
            self.dateTimeEdit_2.setEnabled(True)
            self.dateTimeEdit.setEnabled(True)
        return

    def comboBox_func(self):
        if self.comboBox.currentText()=="Satellite":
            self.comboBox_2.clear()
            self.comboBox_2.addItems(list_sat_name)  
        else:
            self.comboBox_2.clear()
            self.comboBox_2.addItems(["SaxaVord","Baikonour","Kourou","Cap_Canaveral"])  
            return

    def comboBox_2_func(self):
        return
    
    def pushButton_func(self):
        print("+")
        self.parent_tree.addChild(QTreeWidgetItem([str(self.comboBox_2.currentText()),str(self.comboBox_2.currentIndex())]))
        print(self.parent_tree.child(0).text(1))
        return
    
    def pushButton_2_func(self):
        print("-")
        selected_items = self.treeWidget.selectedItems()

        if selected_items:
            item_to_remove = selected_items[0]
            parent_item = item_to_remove.parent()

            if parent_item:
                parent_item.takeChild(parent_item.indexOfChild(item_to_remove))
            else:
                self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(item_to_remove))

        return
            
if __name__ == '__main__':

    dir_path = os.path.dirname(os.path.realpath(__file__))
    list_sat_name = []

    with open(dir_path + '\\jsons\\param.json', 'w') as f:
            json.dump([{"val":[0],
                        "date":["0", " 0", " 0", " 0", " 0"],
                        "live":2,
                        "Dt":["0", " 0", " 0", " 0", " 0"]}], f)
            
    with open(dir_path + '\\jsons\\data.json', 'r') as file:
        data = json.load(file)  
    for index in range(len(data)):
        list_sat_name.append(data[index]["OBJECT_NAME"])
    subprocess.Popen("python -m http.server "+str(params.PORT))    
    app = QApplication(sys.argv)
    ui = MyQtApp()
    ui.show()
    app.exec_()


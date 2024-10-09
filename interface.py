from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from socketio import Client
import random
import os
import pandas as pd
from satellite import *
from view_3d import *
import requests
from parameters import *
from treehandle import *

dir_path = os.path.dirname(os.path.realpath(__file__))
url_satellites = dir_path+"/resources/active.json"

data_sat_pd = pd.read_json(url_satellites)
data_sat_np = data_sat_pd.to_numpy()

class MyQtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(dir_path +"/window/main.ui",self)
        self.setWindowTitle('Satvision 3.0')
        
        self.runStatus = False
        self.viewStatus = {"Orbit": False}
        self.treeStatus = {}
        self.dataToSend = {}
         
        self.menuFileUpdate = QAction(QIcon(dir_path + "/window/image/update.png"),"&Update", self)
        self.menuFile.addAction(self.menuFileUpdate)
        self.menuFileUpdate.triggered.connect(self.menuFileUpdate_func)
        
        self.menuFileNew = QAction(QIcon(dir_path + "/window/image/file.png"),"&File", self)
        self.menuFile.addAction(self.menuFileNew)
        #self.menuFileNew.triggered.connect(self.menuFileNew_func)
        
        self.menuViewOrbit = QAction("Orbit", self, checkable=True, checked=False)
        self.menuView.addAction(self.menuViewOrbit)
        self.menuViewOrbit.triggered.connect(self.menuViewOrbit_func)
        
        self.pushButton.clicked.connect(self.pushButton_func)
        self.pushButton_2.clicked.connect(self.pushButton_2_func)
        self.pushButton_3.clicked.connect(self.pushButton_3_func)
        self.checkBox.clicked.connect(self.checkBox_func)

        self.comboBox.addItems(data_sat_pd["OBJECT_NAME"])
        
        self.treeWidget.itemClicked.connect(self.treeWidget_func)
        
        self.socketio = Client()
        self.socketio.connect('http://127.0.0.1:5000')
        self.socketio.emit('send_message', 'Hello from interface')
        
        self.ui_3D = Window_3D()

        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit.dateTimeChanged.connect(self.dateTimeEdit_func)
        self.dateTimeEdit_2.setDateTime(QDateTime.currentDateTime().addSecs(-2*3600))
        self.dateTimeEdit_2.dateTimeChanged.connect(self.dateTimeEdit_2_func)
        self.dateTimeEdit_3.setDateTime(QDateTime.currentDateTime().addSecs(2*3600))
        self.dateTimeEdit_3.dateTimeChanged.connect(self.dateTimeEdit_3_func)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  
        
        self.show()
    
    def checkBox_func(self):
        self.runStatus = not(self.runStatus)
        #self.dateTimeEdit.setEnabled(self.runStatus)
        #self.dateTimeEdit_2.setDisabled(self.runStatus)
        #self.dateTimeEdit_3.setDisabled(self.runStatus)
            
    def dateTimeEdit_func(self):
        for index in range(self.treeWidget.topLevelItemCount()):
            self.treeWidget.topLevelItem(index).child(18).child(0).setText(0, self.dateTimeEdit.dateTime().toString("dd.MM.yyyy hh:mm:ss.zzz"))
        if self.runStatus:
            self.socketio.emit('send_data_live', getFromTreeWidget(self.treeWidget))
    
    def dateTimeEdit_2_func(self):
        for index in range(self.treeWidget.topLevelItemCount()):
            self.treeWidget.topLevelItem(index).child(19).child(0).setText(0, self.dateTimeEdit_2.dateTime().toString("dd.MM.yyyy hh:mm:ss.zzz"))
        
    def dateTimeEdit_3_func(self):
        for index in range(self.treeWidget.topLevelItemCount()):
            self.treeWidget.topLevelItem(index).child(20).child(0).setText(0, self.dateTimeEdit_3.dateTime().toString("dd.MM.yyyy hh:mm:ss.zzz"))
        
          
    def update_time(self):
        if self.runStatus:
            self.dateTimeEdit.setDateTime(self.dateTimeEdit.dateTime().addSecs(1))
          
    def treeWidget_func(self, item, _):
        try:
            nameClicked = item.child(0).child(0).text(0)
            epochClicked = data_sat_pd[data_sat_pd["OBJECT_NAME"] == nameClicked]["EPOCH"]
            dateEpoch = str(epochClicked).split("T")[0].split(" ")[-1]
            timeEpoch = str(epochClicked).split("T")[1].split(":")[:2]
            self.statusBar().showMessage("last updated: "+dateEpoch+" "+timeEpoch[0]+":"+timeEpoch[1], 0)
            self.treeWiget_selected()
        except:
            pass
    
    def treeWiget_selected(self):
        for index in range(self.treeWidget.topLevelItemCount()):
            self.treeStatus[self.treeWidget.topLevelItem(index).text(0)] = self.treeWidget.topLevelItem(index).checkState(0)
        self.socketio.emit('selected_status', self.treeStatus)            
   
    def pushButton_func(self):
        self.socketio.emit('send_data', getFromTreeWidget(self.treeWidget))
        self.socketio.emit('send_data_live', getFromTreeWidget(self.treeWidget))

    def pushButton_2_func(self):
        indexChosen = self.comboBox.currentIndex()
        nameChosen = data_sat_pd.iloc[indexChosen]["OBJECT_NAME"]
        dataTree = data_sat_pd.iloc[indexChosen].to_dict()
        dataTree["COLOR"] = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
        dataTree["TIME_SIMU_LIVE"] = self.dateTimeEdit.dateTime().toString("dd.MM.yyyy hh:mm:ss.zzz")
        dataTree["TIME_SIMU_START"] = self.dateTimeEdit_2.dateTime().toString("dd.MM.yyyy hh:mm:ss.zzz")
        dataTree["TIME_SIMU_END"] = self.dateTimeEdit_3.dateTime().toString("dd.MM.yyyy hh:mm:ss.zzz")
        addToTreeWidget(self.treeWidget, {nameChosen: dataTree})
        self.treeWiget_selected()

    def pushButton_3_func(self):
        removeFromTreeWidget(self.treeWidget)
        self.treeWiget_selected()
        
    def menuFileUpdate_func(self):
        response = requests.get(URL_CELESTRAK)
        with open(dir_path +'/resources/active.json', 'w') as file:
            file.write(response.text)
            file.close()
            self.socketio.emit('send_message', 'Database updated successfully')
    
    def menuViewOrbit_func(self):
        if self.menuViewOrbit.isChecked():
            self.viewStatus["Orbit"] = 1
        else:
            self.viewStatus["Orbit"] = 0
        self.socketio.emit('view_status', self.viewStatus)

    def closeEvent(self, _):
        self.ui_3D.close()
        self.socketio.disconnect()

import subprocess
import sys
import requests
import json
import os
import signal
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import parameters as params
from stage import Stage_class
from rocket import Rocket_class
from mission import Mission_class
from random import randint
from views import *

class MyQtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(dir_path +"\\ui\\window.ui",self)
        self.setWindowIcon(QIcon(dir_path + '\\image\\logo.ico'))
        
        # Création du menu pour la "view"
        self.actionUpdate = QAction(QIcon(dir_path + "\\ui\\images\\update.png"), "&Update", self)
        self.menuSatvision.addAction(self.actionUpdate)
        
        self.actionLoad = QAction(QIcon(dir_path + "\\ui\\images\\load.png"), "&Load", self)
        self.menuSatvision.addAction(self.actionLoad)
        
        self.action_3D_window = QAction("&3D window", self, checkable=True, checked=False)
        self.action_3D_window.setShortcut("Ctrl+P")
        self.menuView.addAction(self.action_3D_window)
        self.action_3D_window.triggered.connect(self.show_3D_window)
        
        self.action_2D_window = QAction("&2D window", self, checkable=True, checked=False)
        self.action_2D_window.setShortcut("Ctrl+M")
        self.menuView.addAction(self.action_2D_window)
        self.action_2D_window.triggered.connect(self.show_2D_window)
        
        self.actionRocket.triggered.connect(self.actionRocket_func)
        self.actionNozzle.triggered.connect(self.actionNozzle_func)
        
        self.actionUpdate.triggered.connect(self.actionUpdate_func)
        self.radioButton.toggled.connect(self.radioButton_func) 
        self.pushButton.clicked.connect(self.pushButton_func)
        self.pushButton_2.clicked.connect(self.pushButton_2_func)
        # self.pushButton_3.clicked.connect(self.pushButton_3_func) a mettre dans Rocket window
        # self.pushButton_4.clicked.connect(self.pushButton_4_func)
        # self.pushButton_5.clicked.connect(self.pushButton_5_func)
        self.pushButton_7.clicked.connect(self.actionValidate_func)
        self.comboBox.currentIndexChanged.connect(self.comboBox_func) 
        self.comboBox.addItems(["Satellite","Launcher"])  
        self.comboBox_2.currentIndexChanged.connect(self.comboBox_2_func) 
        # self.comboBox_5.addItems(["Monopropellants","Mixpropellants"]) 
        # self.comboBox_5.currentIndexChanged.connect(self.comboBox_5_func) 
        # self.comboBox_6.addItems(["H202","N2H4","N20","Solid"])  
        dt = QDateTime(int(data[0]["EPOCH"][0:4]), int(data[0]["EPOCH"][5:7]), int(data[0]["EPOCH"][8:10]), int(data[0]["EPOCH"][11:13]), int(data[0]["EPOCH"][14:16])) 
        dt2 = QDateTime(int(data[0]["EPOCH"][0:4]), int(data[0]["EPOCH"][5:7]), int(data[0]["EPOCH"][8:10]), int(data[0]["EPOCH"][11:13])+2, int(data[0]["EPOCH"][14:16])) 
        self.dateTimeEdit.setDateTime(dt) 
        self.dateTimeEdit_2.setDateTime(dt2) 
        self.count = 0
        self.count_2 = 0
        self.color_child = {}
        self.treeWidget.setAlternatingRowColors(True)
        # self.treeWidget_2.setAlternatingRowColors(True)
        self.parent_list=[]
        self.parent_list_2=[]
        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)
        self.show()

    def actionRocket_func(self):
        self.ui_Rocket = Window_Rocket()
    
    def actionNozzle_func(self):
        self.ui_Nozzle = Window_Nozzle()
        
    def closeEvent(self, event):
        with open(dir_path + '\\jsons\\param.json', 'w') as f:
            json.dump([{"val": None,
                        "date": None,
                        "live":None,
                        "Dt":None,
                        "color": None,
                        "active": False}], f)
        for window in QApplication.topLevelWidgets():
            window.close()
            
    def update_menu_window_3D(self):
        print("closed")
        #self.action_3D_window.isChecked(False)
        
    def show_3D_window(self):
        try:
            if self.ui_3D.isActiveWindow():
                self.ui_3D.close() 
        except:
            pass
        if self.action_3D_window.isChecked():
            self.ui_3D = Window_3D()
            self.ui_3D.dad = ui
        else:
            try:
                self.ui_3D.close() 
            except:
                pass
                
    
    def show_2D_window(self):
        if self.action_2D_window.isChecked():
            self.ui_2D = Window_2D()
            self.ui_2D.dad = ui
        else:
            try:
                self.ui_2D.close() 
            except:
                pass
        
    def actionUpdate_func(self):
        response = requests.get(params.URL_CELESTRAK)
        data = response.text

        if response.status_code == 200:
            with open(dir_path +'\\jsons\\data.json', 'w') as file:
                file.write(data)
                print("Done")
        else:
            print("Error")

    def actionValidate_func(self):
        try:
            print(self.color_child)
            list_of_obj = []
            list_of_color = []
            for i in range(self.count):
                list_of_obj.append(str(self.parent_list[i][0].child(0).text(0)))
            for i in list(self.color_child):
                list_of_color.append(self.color_child[i]["color"])
            if self.radioButton.isChecked()==True:
                with open(dir_path + '\\jsons\\param.json', 'w') as f:
                    json.dump([{"val":list_of_obj,
                                "date":str(self.dateTimeEdit.dateTime()).split("(")[1].split(")")[0].split(","),
                                "live":2,
                                "Dt":str(self.dateTimeEdit_2.dateTime()).split("(")[1].split(")")[0].split(","),
                                "color": list_of_color,
                                "active": True}], f) 
            else:   
                with open(dir_path + '\\jsons\\param.json', 'w') as f:
                    json.dump([{"val":list_of_obj,
                                "date":str(self.dateTimeEdit.dateTime()).split("(")[1].split(")")[0].split(","),
                                "live":0,
                                "Dt":str(self.dateTimeEdit_2.dateTime()).split("(")[1].split(")")[0].split(","),
                                "color": list_of_color,
                                "active": True}], f) 
            print("wrote")
        except:
            pass
        try:
            self.ui_3D.webviewframe.load(QUrl(params.URL_3D))
        except:
            pass
        try:
            self.ui_2D.webviewframe.load(QUrl(params.URL_2D))
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
    
    def pushButton_5_func(self):
        R_i = self.lineEdit_4.text()
        w = self.lineEdit_5.text()
        e = self.lineEdit_6.text()
        R_et = self.lineEdit.text()
        R_e = self.lineEdit_2.text()
        theta = self.lineEdit_3.text()
        Pc = self.lineEdit_7.text()
        
        return

    def comboBox_5_func(self):
        if self.comboBox_5.currentText()=="Mixpropellants":
            self.comboBox_6.clear()
            self.comboBox_6.addItems(["LOX/Kérosène","LOX/LCH4","LOX/LH2"])  
        else:
            self.comboBox_6.clear()
            self.comboBox_6.addItems(["H202","N2H4","N20","Solid"])  
        return

    def pushButton_func(self):
        print("+")
        color = {}
        self.count = self.count + 1

        self.parent_tree = QTreeWidgetItem(self.treeWidget,[str(self.comboBox_2.currentText())])
        self.parent_tree.addChild(QTreeWidgetItem([str(self.comboBox_2.currentIndex())]))

        color["color"]=[randint(0, 255), randint(0, 255), randint(0, 255)] #faut mettre ca en dict et relier la couleur au child
        color["name"]=str(data[int(self.comboBox_2.currentIndex())]["OBJECT_NAME"])
        self.color_child[str([self.parent_tree])] = color

        self.parent_tree.setForeground(0, QColor(color["color"][0], color["color"][1], color["color"][2]))

        self.child_tree = QTreeWidgetItem(["OBJECT_ID"])
        self.parent_tree.addChild(self.child_tree)
        self.child_tree.addChild(QTreeWidgetItem([str(data[int(self.comboBox_2.currentIndex())]["OBJECT_ID"])]))

        self.child_tree = QTreeWidgetItem(["ECCENTRICITY"])
        self.parent_tree.addChild(self.child_tree)
        self.child_tree.addChild(QTreeWidgetItem([str(data[int(self.comboBox_2.currentIndex())]["ECCENTRICITY"])]))

        self.child_tree = QTreeWidgetItem(["INCLINATION"])
        self.parent_tree.addChild(self.child_tree)
        self.child_tree.addChild(QTreeWidgetItem([str(data[int(self.comboBox_2.currentIndex())]["INCLINATION"])]))

        self.child_tree = QTreeWidgetItem(["ARG_OF_PERICENTER"])
        self.parent_tree.addChild(self.child_tree)
        self.child_tree.addChild(QTreeWidgetItem([str(data[int(self.comboBox_2.currentIndex())]["ARG_OF_PERICENTER"])]))

        self.child_tree = QTreeWidgetItem(["MEAN_ANOMALY"])
        self.parent_tree.addChild(self.child_tree)
        self.child_tree.addChild(QTreeWidgetItem([str(data[int(self.comboBox_2.currentIndex())]["MEAN_ANOMALY"])]))

        self.parent_list.append([self.parent_tree])

        return
    
    def pushButton_2_func(self):
        print("-")
        self.count = self.count - 1
        selected_items = self.treeWidget.selectedItems()
        self.parent_list.remove(selected_items)
        del self.color_child[str(selected_items)]
        if selected_items:
            item_to_remove = selected_items[0]
            parent_item = item_to_remove.parent()

            if parent_item:
                parent_item.takeChild(parent_item.indexOfChild(item_to_remove))
            else:
                self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(item_to_remove))
        return

    def pushButton_3_func(self):
        print("-")
        self.count_2 = self.count_2 - 1
        selected_items = self.treeWidget_2.selectedItems()
        self.parent_list_2.remove(selected_items)
        if selected_items:
            item_to_remove = selected_items[0]
            parent_item = item_to_remove.parent()

            if parent_item:
                parent_item.takeChild(parent_item.indexOfChild(item_to_remove))
            else:
                self.treeWidget_2.takeTopLevelItem(self.treeWidget_2.indexOfTopLevelItem(item_to_remove))

        return
    
    def pushButton_4_func(self):
        print("+")
        self.count_2 = self.count_2 + 1
        self.parent_tree = QTreeWidgetItem(self.treeWidget_2,["stage "+str(self.count_2)])

        self.child_tree = QTreeWidgetItem(["Stage n°"])
        self.parent_tree.addChild(self.child_tree)
        self.child_tree.addChild(QTreeWidgetItem([str(self.comboBox_2.currentIndex())]))

        self.child_tree = QTreeWidgetItem(["Isp"])
        self.parent_tree.addChild(self.child_tree)
        self.child_tree.addChild(QTreeWidgetItem([str(self.lineEdit_ISP.text())]))

        self.child_tree = QTreeWidgetItem(["k*"])
        self.parent_tree.addChild(self.child_tree)
        self.child_tree.addChild(QTreeWidgetItem([str(self.lineEdit_index.text())]))

        self.child_tree = QTreeWidgetItem(["Mass Propellant"])
        self.parent_tree.addChild(self.child_tree)
        self.child_tree.addChild(QTreeWidgetItem([str(self.lineEdit_mprop.text())]))

        self.child_tree = QTreeWidgetItem(["Mass Payload"])
        self.parent_tree.addChild(self.child_tree)
        self.child_tree.addChild(QTreeWidgetItem([str(self.lineEdit_mpay.text())]))

        self.parent_list_2.append([self.parent_tree])

        return
    
    def pushButton_5_func(self):
        stage_Solid_1 = Stage_class(PROPELLANT_TYPE="Solid",PROPELLANT_MASS=500,STAGE_NUMBER="1")
        stage_Solid_1.build()

        stage_LOX_RP1_1 = Stage_class(PROPELLANT_TYPE="LOX-RP1",PROPELLANT_MASS=500,STAGE_NUMBER="1")
        stage_LOX_RP1_1.build()

        stage_LOX_RP1_2_3 = Stage_class(PROPELLANT_TYPE="LOX-RP1",PROPELLANT_MASS=200,STAGE_NUMBER="2")
        stage_LOX_RP1_2_3.build()

        stage_LOX_LK2_2_3 = Stage_class(PROPELLANT_TYPE="LOX-LK2",PROPELLANT_MASS=200,STAGE_NUMBER="2")
        stage_LOX_LK2_2_3.build()

        stages_combination = {"Solid+RP1":[stage_Solid_1,stage_LOX_RP1_2_3]}

        data_dic = {"":["Mass propellant stage 1",
                            "Mass structure stage 1",
                            "Mass propellant stage 2",
                            "Mass structure stage 2",
                            "Mass propellant stage 3",
                            "Mass structure stage 3",
                            "Total Mass",
                            "Mission authorisation"]}

        rocket_1 = Rocket_class(STAGES=stages_combination["Solid+RP1"],PAYLOAD_MASS=230)
        rocket_1.build()
        mission_1 = Mission_class(CLIENT="CNES",ALTITUDE=340,ROCKET=rocket_1)
        mission_1.build(error_min=1e-5, b_last=3, pas=1)
        data_dic=[mission_1.me1,mission_1.ms1,
                        mission_1.me2,mission_1.ms2,
                        mission_1.me3,mission_1.ms3,
                        mission_1.m_total,
                        mission_1.message]
        print(data_dic)
if __name__ == '__main__':

    dir_path = os.path.dirname(os.path.realpath(__file__))
    list_sat_name = []
            
    with open(dir_path + '\\jsons\\data.json', 'r') as file:
        data = json.load(file)  
    for index in range(len(data)):
        list_sat_name.append(data[index]["OBJECT_NAME"])
    subprocess.Popen("python -m http.server "+str(params.PORT))    
    app = QApplication(sys.argv)
    ui = MyQtApp()
    ui.show()
    sys.exit(app.exec_())

# Transférer les fonction et liens de la fenetre de Rocket design dans sa classe dédié
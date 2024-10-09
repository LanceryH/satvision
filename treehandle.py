from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
    
def addToTreeWidget(tree_widget, data_dict):
        def add_items(parent, value):
            if isinstance(value, dict):
                for key, val in value.items():
                    child = QTreeWidgetItem([str(key)])
                    parent.addChild(child)
                    add_items(child, val)
            elif isinstance(value, list):
                for index, val in enumerate(value):
                    child = QTreeWidgetItem([f'Item {index}', str(val)])
                    parent.addChild(child)
            else:
                item = QTreeWidgetItem([str(value)])
                parent.addChild(item)
        for key, value in data_dict.items():
            parent = QTreeWidgetItem([key])
            tree_widget.addTopLevelItem(parent)
            parent.setIcon(0, QIcon(dir_path + "/window/image/satellite.png"))
            parent.setBackground(0, QColor(value["COLOR"]))
            parent.setFlags(parent.flags() | Qt.ItemIsUserCheckable)
            parent.setCheckState(0, Qt.Checked)
            add_items(parent, value)
            

def removeFromTreeWidget(tree_widget):
        selected_items = tree_widget.selectedItems()
        if selected_items:
            item_to_remove = selected_items[0]
            parent_item = item_to_remove.parent()

            if parent_item:
                parent_item.takeChild(parent_item.indexOfChild(item_to_remove))
            else:
                tree_widget.takeTopLevelItem(tree_widget.indexOfTopLevelItem(item_to_remove))
        return

def getFromTreeWidget(tree_widget):
    tree_dict = {}
    for i in range(tree_widget.topLevelItemCount()):
        top_item = tree_widget.topLevelItem(i)
        tree_dict[top_item.text(0)] = {}
        for j in range(top_item.childCount()):
            child_item = top_item.child(j)
            try:
                tree_dict[top_item.text(0)][child_item.text(0)] = float(child_item.child(0).text(0) if child_item.childCount() > 0 else child_item.text(1))
            except:
                tree_dict[top_item.text(0)][child_item.text(0)] = str(child_item.child(0).text(0) if child_item.childCount() > 0 else child_item.text(1))
    return tree_dict


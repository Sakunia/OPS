from maya import OpenMayaUI as omui
import os

import maya.cmds as mc
from pymel.core import *
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin



try:
  from PySide2.QtCore import *
  from PySide2.QtGui import *
  from PySide2.QtWidgets import *
  from PySide2 import __version__
  from shiboken2 import wrapInstance
except ImportError:
  from PySide.QtCore import *
  from PySide.QtGui import *
  from PySide import __version__
  from shiboken import wrapInstance


# to be sure we laod the plugin
# loadPlugin("fbxmaya")

class ToolWindow(MayaQWidgetBaseMixin,QMainWindow):
    selected_items = [None]

    def __init__(self, *args, **kwargs):
        super(ToolWindow,self).__init__(*args, **kwargs)
        self.setWindowTitle('OPS - Batch export')
        self.setWindowFlags(Qt.Window)

        frame = QWidget()
        layout = QVBoxLayout()

        asset_list_label = QLabel("Exportable assets")
        asset_list = QListWidget()
        asset_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        objects = self.getAllGroupsInScene()
        for i in objects:
            asset_list.addItem(i[:-5])

        asset_list.itemClicked.connect(lambda item: self.getSelectedFromList(asset_list))

        # buttons
        button_layout = QHBoxLayout()
        export_button = QPushButton("Export selected")
        browse_button = QPushButton("browse exported")
        set_custom_export = QPushButton("Set export path")

        export_button.clicked.connect(self.onExportClicked)
        browse_button.clicked.connect(self.onShowExported)

        button_layout.addWidget(export_button)
        button_layout.addWidget(browse_button)
        button_layout.addWidget(set_custom_export)

        layout.addWidget(asset_list_label)
        layout.addWidget(asset_list)
        layout.addLayout(button_layout)

        frame.setLayout(layout)
        self.setCentralWidget(frame)

    def onExportClicked(self):
        for object in self.selected_items:
            self.ExportObject(object)

    def onShowExported(self):
        os.startfile(self.getFilePath(True))

    def getFilePath(self, bExport_folder):

        file_path = str(mc.file(q=True, sn = True, un = True))
        file_name = str(mc.file(q=True, sn = True, shn = True))
        out_path = file_path[:-len(file_name)]

        if bExport_folder:
            self.checkExportDirValid(out_path + 'Export/')
            return out_path + 'Export/'

        return file_path[:-len(file_name)]

    def checkExportDirValid(self,input_dir):
        dir = os.path.dirname(input_dir)
        if not os.path.exists(dir):
            os.makedirs(dir)

    def getAllGroupsInScene(self):
        out = mc.ls('Root_*', s =True)
        print out
        return out

    def getSelectedFromList(self,List):
        out_list = []
        for i in List.selectedItems():
            out_list.append( i.text())

        self.selected_items = out_list

    def ExportObject(self,object):
        select(object)
        selection = ls(sl=True)
        shape = selection [0].getShape()
        makeIdentity(a= True, t= True, s = True, pn = True)

        shape_x = getAttr(shape + '.localPositionX')
        shape_y = getAttr(shape + '.localPositionY')
        shape_z = getAttr(shape + '.localPositionZ')

        setAttr(selection[0] + '.translateX',shape_x *-1)
        setAttr(selection[0] + '.translateY',shape_y *-1)
        setAttr(selection[0] + '.translateZ',shape_z *-1)

        export_path = self.getFilePath(True) + "SM" + object[4:]
        export_string = 'FBXExport -f "%s.fbx" -s' % (export_path)
        mel.eval(export_string)  # remove -s to export all

        setAttr(selection[0] + '.translateX',0)
        setAttr(selection[0] + '.translateY',0)
        setAttr(selection[0] + '.translateZ',0)
        
        
mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
mayaMainWindow= wrapInstance(long(mayaMainWindowPtr), ToolWindow) 

tool_window = ToolWindow()
tool_window.show()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from fileinfo import *

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class FileForm(QWidget):

    def __init__(self,parent=None):
        super(FileForm,self).__init__(parent)
        
        self.setWindowTitle("FileInfo")
        self.resize(600,480)
        
        filePushButton=QPushButton(self.tr("打开"))

        self.fileLineEdit=QLineEdit()

        self.ownerLabel = QLabel(u"所有者  : ")
        self.ownerLine = QLineEdit()
        self.ownerLine.setReadOnly(True)

        self.createLabel = QLabel(u"创建时间: ")
        self.createLine = QLineEdit()
        self.createLine.setReadOnly(True)

        self.accesseLabel = QLabel(u"访问时间: ")
        self.accesseLine = QLineEdit()
        self.accesseLine.setReadOnly(True)

        self.motifedLabel = QLabel(u"修改时间: ")
        self.motifedLine = QLineEdit()
        self.motifedLine.setReadOnly(True)

        self.sizeLabel = QLabel(u"文件大小: ")
        self.sizeLine = QLineEdit()
        self.sizeLine.setReadOnly(True)
        
        filePushButton=QPushButton(self.tr("打开"))

        self.fileLineEdit=QLineEdit()
        self.ownerLine = QLineEdit()
        self.ownerLine.setReadOnly(True)

        layout=QGridLayout()
        layout.addWidget(filePushButton,0,0)
        layout.addWidget(self.fileLineEdit,0,1)
        layout.addWidget(self.ownerLabel, 1, 0)
        layout.addWidget(self.ownerLine, 1, 1)
        layout.addWidget(self.createLabel, 2, 0)
        layout.addWidget(self.createLine, 2, 1)
        layout.addWidget(self.accesseLabel, 3, 0)
        layout.addWidget(self.accesseLine, 3, 1)
        layout.addWidget(self.motifedLabel, 4, 0)
        layout.addWidget(self.motifedLine, 4, 1)
        layout.addWidget(self.sizeLabel, 5, 0)
        layout.addWidget(self.sizeLine, 5, 1)
        
        self.setLayout(layout)

        self.connect(filePushButton,SIGNAL("clicked()"),self.openFile)

    def openFile(self):
        
        s=QFileDialog.getOpenFileName(self,"Open file dialog","/","All files(*.*)")
        file_stat = get_file_stat(str(s))
        file_owner = ownerinfo(file_stat)
        file_created_time = created_time(file_stat)
        file_accesse_time = last_accesse_time(file_stat)
        file_motified_time = last_motified_time(file_stat)
        file_size = get_file_size(file_stat)
        self.fileLineEdit.setText(str(s))
        self.ownerLine.setText(str(file_owner))
        self.createLine.setText(str(file_created_time))
        self.accesseLine.setText(str(file_accesse_time))
        self.motifedLine.setText(str(file_motified_time))
        self.sizeLine.setText(str(file_size))
        

    def openColor(self):

        c=QColorDialog.getColor(Qt.blue)
        if c.isValid():
            self.colorFrame.setPalette(QPalette(c))

    def openFont(self):
   
        f,ok=QFontDialog.getFont()
        if ok:
            self.fontLineEdit.setFont(f)

            
if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=FileForm()
    form.show()
    sys.exit(app.exec_())

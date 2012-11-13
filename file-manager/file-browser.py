#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import *

class Browser(QWidget):
    def __init__(self):
        super(Browser, self).__init__()

        self.resize(700, 600)
        self.setWindowTitle("File Browser")
        self.treeView = QTreeView()
        self.fileSystemModel = QFileSystemModel(self.treeView)
        self.fileSystemModel.setReadOnly(False)
        root = self.fileSystemModel.setRootPath("/")
        self.treeView.setModel(self.fileSystemModel)
        self.treeView.setRootIndex(root)

        Layout = QVBoxLayout(self)
        Layout.addWidget(self.treeView)
        self.setLayout(Layout)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Browser()
    main.show()
    sys.exit(app.exec_())

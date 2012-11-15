#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import psutil
from threading import Thread




class MyItem(QTreeWidgetItem):
    def __init__(self, parent, process_name, pid, user, cpu_percent, mem_percent, command=None):
        QTreeWidgetItem.__init__(self, parent)

        self.process_name = process_name
        self.pid = pid
        self.user = user
        self.cpu_percent = cpu_percent
        self.mem_percent = mem_percent
        self.command = command
        self.setText(0, self.process_name)
        self.setText(1, self.pid)
        self.setText(2, self.user)
        self.setText(3, self.cpu_percent)
        self.setText(4, self.mem_percent)
        self.setText(5, self.command)
        
class ProcessTree(QTreeWidget):
    def __init__(self, parent):
        QTreeWidget.__init__(self, parent)
        self.itemList = []
        self.setColumnCount(4)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setTextElideMode(Qt.ElideRight)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.setAutoExpandDelay(-1)
        self.setRootIsDecorated(False)
        self.setItemsExpandable(False)
        self.setAnimated(False)
        self.setWordWrap(False)
        self.setExpandsOnDoubleClick(False)
        self.headerItem().setText(0, QApplication.translate("ProcessMonitor", "Process", None, QApplication.UnicodeUTF8))
        self.headerItem().setText(1, QApplication.translate("ProcessMonitor", "Pid", None, QApplication.UnicodeUTF8))
        self.headerItem().setText(2, QApplication.translate("ProcessMonitor", "User", None, QApplication.UnicodeUTF8))
        self.headerItem().setText(3, QApplication.translate("ProcessMonitor", "CPU", None, QApplication.UnicodeUTF8))
        self.headerItem().setText(4, QApplication.translate("ProcessMonitor", "Memory", None, QApplication.UnicodeUTF8))
        self.headerItem().setText(5, QApplication.translate("ProcessMonitor", "Command", None, QApplication.UnicodeUTF8))

        
        pids = psutil.get_pid_list()
        procs = []
        for pid in pids:
            try:
                p = psutil.Process(pid)
                new_proc = (p.name, 
                            str(p.pid),
                            p.username,
                            str(0),
                            str(int(p.get_memory_percent() * 100)),
                            p.cmdline)
                procs.append(new_proc)
            except:
                pass
            
        sorted_procs = sorted(procs)
        for proc in sorted_procs:
            item = MyItem(self, process_name=proc[0], pid=proc[1], user=proc[2], cpu_percent=proc[3], mem_percent=proc[4], command=" ".join(proc[5][:]))

        self.insertTopLevelItem(0, item)
        self.itemList.append(item)

class ProcessMonitor(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(768,480)

        # Central Widget
        self.layoutWidget = QWidget(self)
        self.setCentralWidget(self.layoutWidget)

        # Button
        self.btn = QPushButton(self.layoutWidget)
        self.btn.setText('End Process')
        self.btn.setGeometry(QRect(0,0,60,40))
        self.btn.setMinimumSize(QSize(60, 40))
        self.btn.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,
QSizePolicy.Fixed))
        # Tree
        self.tree = ProcessTree(self.layoutWidget)
        # Layout
        self.lv_Main = QVBoxLayout(self.layoutWidget)
        self.lv_Main.addWidget(self.btn)
        self.lv_Main.addWidget(self.tree)
        # Connections
        self.connect(self.btn, SIGNAL('clicked()'), self.end_process)

    def end_process(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ProcessMonitor()
    form.setWindowTitle("System Monitor")
    form.show()
    app.exec_()

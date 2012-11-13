#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from system import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.initUI()

        
    def initUI(self):

        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border:1px solid rgb(255, 170, 255);")
        # get system info
        self.spaceOneLabel = QLabel(" ")
        self.spaceTwoLabel = QLabel(" ")
        ## os_info
        self.os_info = OsInfo()
        self.hardware_info = HardwareInfo()
        self.system_status = SystemStatus()
        self.host_nameLabel = QLabel((self.os_info.get_hostname()))
        self.host_nameLabel.setStyleSheet("QLabel {font-size : 20px; font-weight:bold; color : black;}")
        self.dist_nameLabel = QLabel(self.os_info.get_dist_name())
        self.dist_nameLabel.setStyleSheet("QLabel {font-size : 18px; color : black;}")
        self.dist_release_infoLabel = QLabel(self.os_info.get_dist_release_info())
        self.kernel_versionLabel = QLabel(("Kernel: " + self.os_info.get_kernel_version()))

        ## hardware_info
        self.hardwareLabel = QLabel("Hardware")
        self.hardwareLabel.setStyleSheet("QLabel {font-size : 20px; font-weight:bold; color : black;}")
        self.cpu_nameLabel = QLabel(("Processor: " + self.hardware_info.get_cpuname() +" X " + str(self.hardware_info.get_cpu_processor_num())))
        self.total_phpmemLabel = QLabel(("Memory: " + self.hardware_info.get_total_memery()))

        ## system_status
        self.systemStatusLabel = QLabel("System Status")
        self.systemStatusLabel.setStyleSheet("QLabel {font-size : 20px; font-weight:bold; color : black;}")
        self.available_diskLabel = QLabel(("Available disk space: " + self.system_status.get_available_disk()))

        
        ## SystemTab
        self.systemTab = QWidget()
        self.systemTab.setSizeIncrement(500, 700)
        self.systemLayout = QGridLayout(self.systemTab)
        self.systemLayout.addWidget(self.host_nameLabel, 0, 0)
        self.systemLayout.addWidget(self.dist_nameLabel, 1, 0)
        self.systemLayout.addWidget(self.dist_release_infoLabel, 2, 0)
        self.systemLayout.addWidget(self.kernel_versionLabel,3, 0)
        self.systemLayout.addWidget(self.spaceOneLabel, 4, 0)
        self.systemLayout.addWidget(self.hardwareLabel, 5, 0)
        self.systemLayout.addWidget(self.total_phpmemLabel, 6, 0)
        self.systemLayout.addWidget(self.cpu_nameLabel, 7, 0)
        self.systemLayout.addWidget(self.spaceTwoLabel, 8, 0)
        self.systemLayout.addWidget(self.systemStatusLabel, 9, 0)
        self.systemLayout.addWidget(self.available_diskLabel, 10, 0)
        self.processTab = QCalendarWidget()
        
        self.topTab = QTabWidget()
        self.topTab.addTab(self.systemTab, "system")
        self.topTab.resize(640, 480)
        self.topTab.setWindowTitle("system-monitor")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.topTab.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        


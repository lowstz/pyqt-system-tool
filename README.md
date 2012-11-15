pyqt-system-tool
================

操作系统课程的实验

子文件夹信息
-----------
```
 ├── file-info  -- 文件属性查看
 │   ├── fileinfo.py
 │   ├── __init__.py
 │   └── main.py
 ├── file-manager -- 资源管理器
 │   └── file-browser.py
 ├── README.md
 ├── system-info -- 系统信息查看
 │   ├── __init__.py
 │   ├── main.py
 │   └── system.py
 └── system-monitor -- 进程管理器
     ├── pyqt
     │   ├── cpu_usage_realtime.py  -- cpu利用率实时图
     │   └── process-montor.py      -- pyqt版本的进程管理器，结束进程那部分很糟糕
     └── wx
          └── process-montor_wx.py   -- 参考别人wx版写的，功能晚上，比原作者的性能好99倍！
```
运行环境
-----------
运行环境： Linux、python2
已测试运行环境： Fedora 17， python2.7

依赖
-----------
PyQt
psutil

进程管理器wx版用到依赖
psutil
wxpython
ObjectListView





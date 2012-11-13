#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import platform
import psutil

def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1)*10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

# 获取主机名、发行版和内核版本等信息
class OsInfo():
    def get_hostname(self):
        return platform.uname()[1]

    def get_dist_name(self):
        return platform.dist()[0]

    def get_dist_release_info(self):
        self.dist = platform.dist()
        self.arch = platform.architecture()
        return self.dist[1] + " (" + self.dist[2] + ") " + self.arch[0]
    def get_kernel_version(self):
        return platform.uname()[2]

# 获取硬件信息
class HardwareInfo():
    def get_cputype(self):
        pass

    def get_cpuname(self):
        f = open("/proc/cpuinfo")
        self.lines = f.readlines()
        f.close()
        self.cpu = []
        pattern = re.compile(r'^model name')
        for self.line in self.lines:
            match = pattern.match(self.line)
            if match:
                self.cpu.append(self.line)

        self.cpu_str = re.findall(':(.*)', self.cpu[0], re.M)
        self.cpu_name = self.cpu_str[0].strip()
        return self.cpu_name

    def get_cpu_processor_num(self):
        return psutil.NUM_CPUS

    def get_total_memery(self):
        return bytes2human(psutil.TOTAL_PHYMEM)

# 获取系统状态信息

class SystemStatus():
    def get_available_disk(self):
        self.free_space = 0
        for self.path in psutil.disk_partitions(all=False):
            self.free_space += psutil.disk_usage(self.path.mountpoint)[2]
        return bytes2human(self.free_space)

if __name__ == "__main__":
    os_info = OsInfo()
    hardware_info = HardwareInfo()
    system_status = SystemStatus()
    print os_info.get_hostname()
    print os_info.get_dist_name()
    print os_info.get_dist_release_info()
    print os_info.get_kernel_version()
    
    print hardware_info.get_cpuname()
    #    print hardware_info.get_cputype()
    print hardware_info.get_cpu_processor_num()
    print hardware_info.get_total_memery()

    print system_status.get_available_disk()

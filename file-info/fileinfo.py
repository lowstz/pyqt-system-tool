#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pwd
from time import strftime
from datetime import datetime


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

def get_file_stat(filename):
    filepath = os.path.abspath(filename)
    file_stat = os.stat(filepath)
    return file_stat

def ownerinfo(file_stat):
    owner = pwd.getpwuid(file_stat.st_uid).pw_name
    return owner

def created_time(file_stat):
    created_time = datetime.fromtimestamp(int(file_stat.st_ctime)).strftime('%Y-%m-%d %H:%M:%S')
    return created_time

def last_accesse_time(file_stat):
    last_accessed_time = datetime.fromtimestamp(int(file_stat.st_atime)).strftime('%Y-%m-%d %H:%M:%S')
    return last_accessed_time

def last_motified_time(file_stat):
    last_motified_time = datetime.fromtimestamp(int(file_stat.st_mtime)).strftime('%Y-%m-%d %H:%M:%S')
    return last_motified_time

def get_file_size(file_stat):
    file_size = bytes2human(file_stat.st_size)
    return file_size

if __name__ == "__main__":
    filestat = get_file_stat("/home/lowstz/ovpn.tar.gz")
    print ownerinfo(filestat)
    print created_time(filestat)
    print last_accesse_time(filestat)
    print last_motified_time(filestat)
    print get_file_size(filestat)


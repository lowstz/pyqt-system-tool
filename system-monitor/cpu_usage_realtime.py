#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg \
import FigureCanvasQTAgg as FigureCanvas
import psutil as p

# Total number of iterations
MAXITERS = 200
class CPUMonitor(FigureCanvas):
    """Matplotlib Figure widget to display CPU utilization"""
    def __init__(self):
        # save the current CPU info (used by updating algorithm)
        self.before = self.prepare_cpu_usage()
        # first image setup
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # set specific limits for X and Y axes
        self.ax.set_xlim(0, 200)
        self.ax.set_ylim(0, 100)
        # and disable figure-wide autoscale
        self.ax.set_autoscale_on(False)
        # generates first "empty" plots
        self.user, self.nice, self.sys, self.idle =[], [], [], []
        self.l_user, = self.ax.plot([],self.user, label='User %')
        self.l_nice, = self.ax.plot([],self.nice, label='Nice %')
        self.l_sys, = self.ax.plot([],self.sys, label='Sys %')
        self.l_idle, = self.ax.plot([],self.idle, label='Idle %')
        # add legend to plot
        self.ax.legend()
        # force a redraw of the Figure
        self.fig.canvas.draw()
        # initialize the iteration counter
        self.cnt = 0
        # call the update method (to speed-up visualization)
        self.timerEvent(None)
        # start timer, trigger event every 1000 millisecs (=1sec)
        self.timer = self.startTimer(1000)
    def prepare_cpu_usage(self):
        """helper function to return CPU usage info"""
        # get the CPU times using psutil module
        t = p.cpu_times()
        # return only the values we're interested in
        if hasattr(t, 'nice'):
            return [t.user, t.nice, t.system, t.idle]
        else:
            # special case focr Windows, without 'nice' value
            return [t.user, 0, t.system, t.idle]
    def get_cpu_usage(self):
        """Compute CPU usage comparing previous and current measurements"""
        # take the current CPU usage information
        now = self.prepare_cpu_usage()
        # compute delta between current and previous measurements
        delta = [now[i]-self.before[i] for i in range(len(now))]
        # compute the total (needed for percentages calculation)
        total = sum(delta)
        # save the current measurement to before object
        self.before = now
        # return the percentage of CPU usage for our 4 categories
        return [(100.0*dt)/total for dt in delta]
    def timerEvent(self, evt):
        # get the cpu percentage usage
        result = self.get_cpu_usage()
        # append new data to the datasets
        self.user.append(result[0])
        self.nice.append(result[1])
        self.sys.append( result[2])
        self.idle.append(result[3])
        # update lines data using the lists with new data
        self.l_user.set_data(range(len(self.user)), self.user)
        self.l_nice.set_data(range(len(self.nice)), self.nice)
        self.l_sys.set_data( range(len(self.sys)), self.sys)
        self.l_idle.set_data(range(len(self.idle)), self.idle)
        # force a redraw of the Figure
        self.fig.canvas.draw()
        if self.cnt == MAXITERS:
            # stop the timer
            self.killTimer(self.timer)
        else:
           #else, we increment the counter
           self.cnt += 1
# create the GUI application

widget = CPUMonitor()
widget.setWindowTitle("CPU Usage Realtime")
widget.show()
sys.exit(app.exec_())

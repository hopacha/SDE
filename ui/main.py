# -*- coding: utf-8 -*-
"""
Module implementing MainWindow.
"""
from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow, QVBoxLayout
from PyQt4.QtCore import pyqtSignature
import random
import math
import numpy
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from Ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.widget)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.widget.setLayout(self.layout)
        #layout.addWidget(self.navigation_toolbar)
        self.axes = self.fig.add_subplot(111)
        self.axes.legend()
        
        self.line = None
        #self.axes.plot(, y, label = 'График')
        
        self.fig_2 = Figure()
        self.canvas_2 = FigureCanvas(self.fig_2)
        self.canvas_2.setParent(self.widget_2)
        
        self.layout_2 = QVBoxLayout()
        self.layout_2.addWidget(self.canvas_2)
        self.widget_2.setLayout(self.layout_2)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_2 = self.fig_2.add_subplot(111)
        self.axes_2.legend()
        
        self.line_2 = None
        #self.axes.plot(, y, label = 'График')
        
        self.fig_3 = Figure()
        self.canvas_3 = FigureCanvas(self.fig_3)
        self.canvas_3.setParent(self.widget_3)
        
        self.layout_3 = QVBoxLayout()
        self.layout_3.addWidget(self.canvas_3)
        self.widget_3.setLayout(self.layout_3)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_3 = self.fig_3.add_subplot(111)
        self.axes_3.legend()
        
        self.line_3 = None
        #self.axes.plot(, y, label = 'График')
        
        self.fig_4 = Figure()
        self.canvas_4 = FigureCanvas(self.fig_4)
        self.canvas_4.setParent(self.widget_4)
        
        self.layout_4 = QVBoxLayout()
        self.layout_4.addWidget(self.canvas_4)
        self.widget_4.setLayout(self.layout_4)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_4 = self.fig_4.add_subplot(111)
        self.axes_4.legend()
        
        self.line_4 = None
        
        self.fig_5 = Figure()
        self.canvas_5 = FigureCanvas(self.fig_5)
        self.canvas_5.setParent(self.widget_5)
        
        self.layout_5 = QVBoxLayout()
        self.layout_5.addWidget(self.canvas_5)
        self.widget_5.setLayout(self.layout_5)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_5 = self.fig_5.add_subplot(111)
        self.axes_5.legend()
        
        self.line_5 = None
        
        self.fig_6 = Figure()
        self.canvas_6 = FigureCanvas(self.fig_6)
        self.canvas_6.setParent(self.widget_6)
        
        self.layout_6 = QVBoxLayout()
        self.layout_6.addWidget(self.canvas_6)
        self.widget_6.setLayout(self.layout_6)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_6 = self.fig_6.add_subplot(111)
        self.axes_6.legend()
        
        self.line_6 = None
        
        self.fig_7 = Figure()
        self.canvas_7 = FigureCanvas(self.fig_7)
        self.canvas_7.setParent(self.widget_7)
        
        self.layout_7 = QVBoxLayout()
        self.layout_7.addWidget(self.canvas_7)
        self.widget_7.setLayout(self.layout_7)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_7= self.fig_7.add_subplot(111)
        self.axes_7.legend()
        
        self.line_7 = None
        
        self.fig_8 = Figure()
        self.canvas_8 = FigureCanvas(self.fig_8)
        self.canvas_8.setParent(self.widget_8)
        
        self.layout_8 = QVBoxLayout()
        self.layout_8.addWidget(self.canvas_8)
        self.widget_8.setLayout(self.layout_8)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_8= self.fig_8.add_subplot(111)
        self.axes_8.legend()
        
        self.line_8 = None
        
        self.fig_9 = Figure()
        self.canvas_9 = FigureCanvas(self.fig_9)
        self.canvas_9.setParent(self.widget_9)
        
        self.layout_9 = QVBoxLayout()
        self.layout_9.addWidget(self.canvas_9)
        self.widget_9.setLayout(self.layout_9)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_9= self.fig_9.add_subplot(111)
        self.axes_9.legend()
        
        self.line_9 = None
        
        self.fig_10 = Figure()
        self.canvas_10 = FigureCanvas(self.fig_10)
        self.canvas_10.setParent(self.widget_10)
        
        self.layout_10 = QVBoxLayout()
        self.layout_10.addWidget(self.canvas_10)
        self.widget_10.setLayout(self.layout_10)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_10= self.fig_10.add_subplot(111)
        self.axes_10.legend()
        
        self.line_10 = None
        
        self.fig_11 = Figure()
        self.canvas_11 = FigureCanvas(self.fig_11)
        self.canvas_11.setParent(self.widget_11)
        
        self.layout_11 = QVBoxLayout()
        self.layout_11.addWidget(self.canvas_11)
        self.widget_11.setLayout(self.layout_11)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_11= self.fig_11.add_subplot(111)
        self.axes_11.legend()
        
        self.line_11 = None
        
        self.fig_12 = Figure()
        self.canvas_12 = FigureCanvas(self.fig_12)
        self.canvas_12.setParent(self.widget_12)
        
        self.layout_12 = QVBoxLayout()
        self.layout_12.addWidget(self.canvas_12)
        self.widget_12.setLayout(self.layout_12)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_12= self.fig_12.add_subplot(111)
        self.axes_12.legend()
        
        self.line_12 = None
        
        self.fig_13 = Figure()
        self.canvas_13 = FigureCanvas(self.fig_13)
        self.canvas_13.setParent(self.widget_13)
        
        self.layout_13 = QVBoxLayout()
        self.layout_13.addWidget(self.canvas_13)
        self.widget_13.setLayout(self.layout_13)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_13= self.fig_13.add_subplot(111)
        self.axes_13.legend()
        
        self.line_13 = None
        
        self.fig_14 = Figure()
        self.canvas_14 = FigureCanvas(self.fig_14)
        self.canvas_14.setParent(self.widget_14)
        
        self.layout_14 = QVBoxLayout()
        self.layout_14.addWidget(self.canvas_14)
        self.widget_14.setLayout(self.layout_14)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_14= self.fig_14.add_subplot(111)
        self.axes_14.legend()
        
        self.line_14 = None
        
        self.fig_15 = Figure()
        self.canvas_15 = FigureCanvas(self.fig_15)
        self.canvas_15.setParent(self.widget_15)
        
        self.layout_15 = QVBoxLayout()
        self.layout_15.addWidget(self.canvas_15)
        self.widget_15.setLayout(self.layout_15)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_15= self.fig_15.add_subplot(111)
        self.axes_15.legend()
        
        self.line_15 = None
        
        self.fig_16 = Figure()
        self.canvas_16 = FigureCanvas(self.fig_16)
        self.canvas_16.setParent(self.widget_16)
        
        self.layout_16 = QVBoxLayout()
        self.layout_16.addWidget(self.canvas_16)
        self.widget_16.setLayout(self.layout_16)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_16= self.fig_16.add_subplot(111)
        self.axes_16.legend()
        
        self.line_16 = None
        
        self.fig_17 = Figure()
        self.canvas_17 = FigureCanvas(self.fig_17)
        self.canvas_17.setParent(self.widget_17)
        
        self.layout_17 = QVBoxLayout()
        self.layout_17.addWidget(self.canvas_17)
        self.widget_17.setLayout(self.layout_17)
        #layout.addWidget(self.navigation_toolbar)
        self.axes_17= self.fig_17.add_subplot(111)
        self.axes_17.legend()
        
        self.line_17 = None
        
        self.a_1 = self.doubleSpinBox.value()
        self.b_1 = self.doubleSpinBox_2.value()
        self.t0_1 = self.doubleSpinBox_3.value()
        self.t1_1 = self.doubleSpinBox_4.value()
        self.n_1 = self.doubleSpinBox_5.value()
        self.x0_1 = self.doubleSpinBox_6.value()
        self.c_1 = self.doubleSpinBox_20.value()
        self.s_1 = self.spinBox.value()
        self.mean_1 = []
        self.std_1 = []
        self.mean_teor_1 = []
        self.std_teor_1 = []
        self.razn_mean_1 = []
        self.razn_std_1 = []
        self.list1_1 = []
        self.list5_1 = []
        
        self.a_2 = self.doubleSpinBox_9.value()
        self.b_2 = self.doubleSpinBox_8.value()
        self.t0_2 = self.doubleSpinBox_10.value()
        self.t1_2 = self.doubleSpinBox_11.value()
        self.n_2 = self.doubleSpinBox_12.value()
        self.x0_2 = self.doubleSpinBox_7.value()
        self.s_2 = self.spinBox_2.value()
        self.mean_2 = []
        self.std_2 = []
        self.mean_teor_2 = []
        self.std_teor_2 = []
        self.razn_mean_2 = []
        self.razn_std_2 = []
        self.list1_2 = []
        self.list5_2 = []
        
        self.a_3 = self.doubleSpinBox_15.value()
        self.b_3 = self.doubleSpinBox_14.value()
        self.c_3 = self.doubleSpinBox_16.value()
        self.t0_3 = self.doubleSpinBox_17.value()
        self.t1_3 = self.doubleSpinBox_18.value()
        self.n_3 = self.doubleSpinBox_19.value()
        self.x0_3 = self.doubleSpinBox_13.value()
        self.s_3 = self.spinBox_3.value()
        self.mean_3 = []
        self.std_3 = []
        self.list1_3 = []
        self.list5_3 = []
    
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        self.a_1 = self.doubleSpinBox.value()
        self.b_1 = self.doubleSpinBox_2.value()
        self.t0_1 = self.doubleSpinBox_3.value()
        self.t1_1 = self.doubleSpinBox_4.value()
        self.n_1 = self.doubleSpinBox_5.value()
        self.x0_1 = self.doubleSpinBox_6.value()
        self.c_1 = self.doubleSpinBox_20.value()
        self.s_1 = self.spinBox.value()
        self.mean_1 = []
        self.std_1 = []
        self.mean_teor_1 = []
        self.std_teor_1 = []
        self.list1_1 = []
        self.list5_1 = []
        #x0 = random.normalvariate(0, 1)
        x = self.x0_1
        i = self.t0_1
        j = 0
        T = self.t1_1 - self.t0_1
        h = T / self.n_1 
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        self.list5_1 = []
        razn_mean = []
        razn_std = []
        m0 = 1
        d0 = 1
        mean_teor = []
        std_teor = []
        for j in range(0, self.s_1):
            #x0 = random.normalvariate(0, 1)
            x = self.x0_1
            i = 0
            list1 = []
            list2 = []
            list3 = []
            list4 = []
            mean_teor = []
            std_teor = []
            while i < self.t1_1:
                v = random.normalvariate(0, 1)
                w = v * math.sqrt(h) 
                x += self.a_1 * (self.b_1 - x) * h + self.c_1 * w
                list1.append(i)
                list2.append(x)
                i += h   
            self.list5_1.append(list2)
        for j in range(len(self.list5_1)):
            self.line = self.axes.plot(list1 , self.list5_1[j], label = 'График')[0]
            self.canvas.draw()
        self.mean_1 = [numpy.mean([self.list5_1[i][j] for i in range(len(self.list5_1))]) for j in range(len(list1))]
        self.std_1 = [numpy.std([self.list5_1[i][j] for i in range(len(self.list5_1))]) for j in range(len(list1))]
        self.line_2 = self.axes_2.plot(list1 , self.mean_1, label = 'График')[0]
        self.canvas_2.draw()
        self.line_3 = self.axes_3.plot(list1 , self.std_1, label = 'График')[0]
        self.canvas_3.draw()

    
    @pyqtSignature("int")
    def on_tabWidget_currentChanged(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError

    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        self.tabWidget.setCurrentIndex(1)

    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        self.tabWidget.setCurrentIndex(0)
    
    @pyqtSignature("")
    def on_pushButton_4_clicked(self):
        self.a_2 = self.doubleSpinBox_9.value()
        self.b_2 = self.doubleSpinBox_8.value()
        self.t0_2 = self.doubleSpinBox_10.value()
        self.t1_2 = self.doubleSpinBox_11.value()
        self.n_2 = self.doubleSpinBox_12.value()
        self.x0_2 = self.doubleSpinBox_7.value()
        self.s_2 = self.spinBox_2.value()
        self.mean_2 = []
        self.std_2 = []
        self.mean_teor_2 = []
        self.std_teor_2 = []
        self.list1_2 = []
        self.list5_2 = []
        #x0 = random.normalvariate(0, 1)
        x = self.x0_2
        i = self.t0_2
        j = 0
        T = self.t1_2 - self.t0_2
        h = T / self.n_2 
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        self.list5_2 = []
        razn_mean = []
        razn_std = []
        m0 = 1
        d0 = 1
        mean_teor = []
        std_teor = []
        for j in range(0, self.s_2):
            #x0 = random.normalvariate(0, 1)
            x = self.x0_2
            i = 0
            list1 = []
            list2 = []
            list3 = []
            list4 = []
            mean_teor = []
            std_teor = []
            while i < self.t1_2:
                v = random.normalvariate(0, 1)
                w = v * math.sqrt(h) 
                x += self.a_2 * x * h + self.b_2 * x * w
                list1.append(i)
                list2.append(x)
                i += h   
            self.list5_2.append(list2)
        for j in range(len(self.list5_2)):
            self.line_4 = self.axes_4.plot(list1 , self.list5_2[j], label = 'График')[0]
            self.canvas_4.draw()
        self.mean_2 = [numpy.mean([self.list5_2[i][j] for i in range(len(self.list5_2))]) for j in range(len(list1))]
        self.std_2 = [numpy.std([self.list5_2[i][j] for i in range(len(self.list5_2))]) for j in range(len(list1))]
        self.line_5 = self.axes_5.plot(list1 , self.mean_2, label = 'График')[0]
        self.canvas_5.draw()
        self.line_6 = self.axes_6.plot(list1 , self.std_2, label = 'График')[0]
        self.canvas_6.draw()


    
    #@pyqtSignature("")
    def on_pushButton_6_clicked(self):
        self.axes.clear()
        self.axes_2.clear()
        self.axes_3.clear()
        self.canvas.draw()
        self.canvas_2.draw()
        self.canvas_3.draw()
    
    @pyqtSignature("")
    def on_pushButton_7_clicked(self):
        f1 = open('x_traekt_model_1.txt',  'w')
        for i in self.list5_1:
            f1.write('%s\n' % i)
        f1.close()
        f2 = open('mean_model_1.txt',  'w')
        for i in self.mean_1:
            f2.write('%s\n' % i)
        f2.close()
        f3 = open('std_model_1.txt',  'w')
        for i in self.std_1:
            f3.write('%s\n' % i)
        f3.close()

        self.fig.savefig('x_traekt_model_1.jpg')
        self.fig_2.savefig('mean_model_1.jpg')
        self.fig_3.savefig('std_model_1.jpg')

    
    @pyqtSignature("")
    def on_pushButton_8_clicked(self):
        f1 = open('x_traekt_model_2.txt',  'w')
        for i in self.list5_2:
            f1.write('%s\n' % i)
        f1.close()
        f2 = open('mean_model_2.txt',  'w')
        for i in self.mean_2:
            f2.write('%s\n' % i)
        f2.close()
        f3 = open('std_model_2.txt',  'w')
        for i in self.std_2:
            f3.write('%s\n' % i)
        f3.close()
        self.fig_4.savefig('x_traekt_model_2.jpg')
        self.fig_5.savefig('mean_model_2.jpg')
        self.fig_6.savefig('std_model_2.jpg')

    
    @pyqtSignature("")
    def on_pushButton_5_clicked(self):
        self.tabWidget.setCurrentIndex(2)

    
    #@pyqtSignature("")
    def on_pushButton_9_clicked(self):
        self.tabWidget.setCurrentIndex(3)
        T = self.t1_1 - self.t0_1
        h = T / self.n_1 
        i = 0    
        m0 = 1
        d0 = 0
        list1 = []
        x0 = 1
        x_teor_1 = 0
        self.mean_teor_1 = []
        self.std_teor_1 = []
        self.razn_mean_1 = []
        self.razn_std_1 = []
        list_x_2 = []
        while i < self.t1_1:
            list1.append(i)
            v = random.normalvariate(0, 1)
            w = v * math.sqrt(h) 
            m = self.b_1 + (self.x0_1 - self.b_1)* numpy.exp(-self.a_1 * i)
            #x_teor_1 = x0 * numpy.exp(- self.a_1 * i) + self.b_1 * (1 - numpy.exp(-self.a_1 * i)) + self.c_1 * w
            self.mean_teor_1.append(m)
            d = (1 - numpy.exp(-2 * self.a_1 * i)) * (self.c_1**2) /(2 * self.a_1)
            d1 = numpy.sqrt(d)
            self.std_teor_1.append(d1)
            i += h 
        for i in range(len(self.mean_1)):
            k = numpy.abs(self.mean_teor_1[i]-self.mean_1[i])
            self.razn_mean_1.append(k)
            #print razn[i]
        for i in range(len(self.std_1)):
            k = numpy.abs(self.std_teor_1[i]-self.std_1[i])
            self.razn_std_1.append(k)
            #print razn_std[i]
        #print len(razn_mean), len(razn_std),  len(list1)
        #print len(mean_teor_1), len(std_teor_1),  len(list1)
        self.line_7 = self.axes_7.plot(list1 , self.mean_teor_1, label = 'График')[0]
        self.canvas_7.draw()
        self.line_8 = self.axes_8.plot(list1 , self.std_teor_1, label = 'График')[0]
        self.canvas_8.draw()
        self.line_14 = self.axes_14.plot(list1 , self.razn_mean_1, label = 'График')[0]
        self.canvas_14.draw()
        self.line_15 = self.axes_15.plot(list1 , self.razn_std_1, label = 'График')[0]
        self.canvas_15.draw()

    
    #@pyqtSignature("")
    def on_pushButton_10_clicked(self):
        self.axes_4.clear()
        self.axes_5.clear()
        self.axes_6.clear()
        self.canvas_4.draw()
        self.canvas_5.draw()
        self.canvas_6.draw()

    
    @pyqtSignature("")
    def on_pushButton_11_clicked(self):
        self.tabWidget.setCurrentIndex(4)
        T = self.t1_2 - self.t0_2
        h = T / self.n_2 
        i = 0    
        m0 = 1
        d0 = 0
        x_teor_2 = 0
        list_x =[]
        list1 = []
        self.mean_teor_2 = []
        self.std_teor_2 = []
        self.razn_mean_2 = []
        self.razn_std_2 = []
        while i < self.t1_2:
            list1.append(i)
            v = random.normalvariate(0, 1)
            w = v * math.sqrt(h) 
            #x_teor_2 = numpy.exp((self.a_2 - (self.b_2)**2 / 2) * i  + self.b_2 * w)
            #list_x.append(x_teor_2)
            m = m0 * numpy.exp(self.a_2 * i)
            self.mean_teor_2.append(m)
            #d = d0 * numpy.exp(self.a_2 * i) + ((self.b_2**2) /(2 * self.a_2)) * (numpy.exp(2 * self.a_2 * i)-1)
            d = numpy.exp(2 * self.a_2 * i) * (numpy.exp(i * self.b_2**2) - 1)
            d1 = numpy.sqrt(d)
            self.std_teor_2.append(d1)
            i += h 
        for i in range(len(self.mean_2)):
            k = numpy.abs(self.mean_teor_2[i]-self.mean_2[i])
            self.razn_mean_2.append(k)
            #print razn[i]
        for i in range(len(self.std_2)):
            k = numpy.abs(self.std_teor_2[i]-self.std_2[i])
            self.razn_std_2.append(k)
            #print razn_std[i]
        #print len(razn_mean), len(razn_std),  len(list1)
        #print self.std_teor_2,  self.std_2
        self.line_9 = self.axes_9.plot(list1 , self.mean_teor_2, label = 'График')[0]
        self.canvas_9.draw()
        self.line_10 = self.axes_10.plot(list1 , self.std_teor_2, label = 'График')[0]
        self.canvas_10.draw()
        self.line_16 = self.axes_16.plot(list1 , self.razn_mean_2, label = 'График')[0]
        self.canvas_16.draw()
        self.line_17 = self.axes_17.plot(list1 , self.razn_std_2, label = 'График')[0]
        self.canvas_17.draw()
    
    @pyqtSignature("")
    def on_pushButton_12_clicked(self):
        self.tabWidget.setCurrentIndex(5)
    
    @pyqtSignature("")
    def on_pushButton_13_clicked(self):
        self.a_3 = self.doubleSpinBox_15.value()
        self.b_3 = self.doubleSpinBox_14.value()
        self.c_3 = self.doubleSpinBox_16.value()
        self.t0_3 = self.doubleSpinBox_17.value()
        self.t1_3 = self.doubleSpinBox_18.value()
        self.n_3 = self.doubleSpinBox_19.value()
        self.x0_3 = self.doubleSpinBox_13.value()
        self.s_3 = self.spinBox_3.value()
        self.mean_3 = []
        self.std_3 = []
        self.list1_3 = []
        self.list5_3 = []
        x = self.x0_3
        i = self.t0_3
        j = 0
        T = self.t1_3 - self.t0_3
        h = T / self.n_3 
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        self.list5_3 = []
        for j in range(0, self.s_3):
            #x0 = random.normalvariate(0, 1)
            x = self.x0_3
            i = 0
            list1 = []
            list2 = []
            list3 = []
            list4 = []
            while i < self.t1_3:
                v = random.normalvariate(0, 1)
                w = v * math.sqrt(h) 
                x += self.a_3 * (self.b_3 - x) * h + self.c_3 * numpy.sqrt(x) * w  
                list1.append(i)
                list2.append(x)
                i += h   
            self.list5_3.append(list2)
        for j in range(len(self.list5_3)):
            self.line_11 = self.axes_11.plot(list1 , self.list5_3[j], label = 'График')[0]
            self.canvas_11.draw()
        self.mean_3 = [numpy.mean([self.list5_3[i][j] for i in range(len(self.list5_3))]) for j in range(len(list1))]
        self.std_3 = [numpy.std([self.list5_3[i][j] for i in range(len(self.list5_3))]) for j in range(len(list1))]
        self.line_12 = self.axes_12.plot(list1 , self.mean_3, label = 'График')[0]
        self.canvas_12.draw()
        self.line_13 = self.axes_13.plot(list1 , self.std_3, label = 'График')[0]
        self.canvas_13.draw()
    
    @pyqtSignature("")
    def on_pushButton_14_clicked(self):
        f1 = open('x_traekt_model_3.txt',  'w')
        for i in self.list5_3:
            f1.write('%s\n' % i)
        f1.close()
        f2 = open('mean_model_3.txt',  'w')
        for i in self.mean_3:
            f2.write('%s\n' % i)
        f2.close()
        f3 = open('std_model_3.txt',  'w')
        for i in self.std_3:
            f3.write('%s\n' % i)
        f3.close()
        self.fig_11.savefig('x_traekt_model_3.jpg')
        self.fig_12.savefig('mean_model_3.jpg')
        self.fig_13.savefig('std_model_3.jpg')
    
    @pyqtSignature("")
    def on_pushButton_15_clicked(self):
        self.axes_11.clear()
        self.axes_12.clear()
        self.axes_13.clear()
        self.canvas_11.draw()
        self.canvas_12.draw()
        self.canvas_13.draw()
    
    @pyqtSignature("")
    def on_pushButton_16_clicked(self):
        f1 = open('mean_teor_1.txt',  'w')
        for i in self.mean_teor_1:
            f1.write('%s\n' % i)
        f1.close()
        f2 = open('std_teor_1.txt',  'w')
        for i in self.std_teor_1:
            f2.write('%s\n' % i)
        f2.close()
        f3 = open('razn_mean.txt',  'w')
        for i in self.razn_mean_1:
            f3.write('%s\n' % i)
        f3.close()
        f4 = open('razn_std.txt',  'w')
        for i in self.razn_std_1:
            f4.write('%s\n' % i)
        f4.close()
        self.fig_7.savefig('mean_teor_1.jpg')
        self.fig_8.savefig('std_teor_1.jpg')
        self.fig_14.savefig('razn_mean_1.jpg')
        self.fig_15.savefig('razn_std_1.jpg')
    
    @pyqtSignature("")
    def on_pushButton_17_clicked(self):
        f1 = open('mean_teor_2.txt',  'w')
        for i in self.mean_teor_2:
            f1.write('%s\n' % i)
        f1.close()
        f2 = open('std_teor_2.txt',  'w')
        for i in self.std_teor_2:
            f2.write('%s\n' % i)
        f2.close()
        f3 = open('razn_mean_2.txt',  'w')
        for i in self.razn_mean_2:
            f3.write('%s\n' % i)
        f3.close()
        f4 = open('razn_std_2.txt',  'w')
        for i in self.razn_std_2:
            f4.write('%s\n' % i)
        f4.close()
        self.fig_9.savefig('mean_teor_2.jpg')
        self.fig_10.savefig('std_teor_2.jpg')
        self.fig_16.savefig('razn_mean_2.jpg')
        self.fig_17.savefig('razn_std_2.jpg')

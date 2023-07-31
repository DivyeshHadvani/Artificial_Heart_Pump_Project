# from PyQt5 import QtCore, QtGui, QtWidgets, QMainWindow, QApplication
from scipy.interpolate import CubicSpline
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

import time


import pickle
import math
import openpyxl
import os

import pandas as pd
from matplotlib import pyplot as plt  # import matplotlib.pyplot as plt
from pyqtgraph import PlotWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QCheckBox


from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QShortcut

from matplotlib.animation import FuncAnimation

import matplotlib
matplotlib.use('TkAgg')

import keyboard

from PyQt5.QtGui import QKeySequence

from Plot_Graph_Sine import sine_graph
from Import_Sine_File import import_data

# from Main_AH_NEW import Ui_MainWindow


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("Main_AH_NEW.ui", self)
        
        # self.ui = Ui_MainWindow()
        
        self.export_pressed = False
        
        # print("self.export_pressed",self.export_pressed)

        # Define Our Widgets
        self.Graph_layout = self.findChild(QVBoxLayout, "Graph_layout")

        self.OK_PB = self.findChild(QPushButton, "OK_PB")
        self.Export_PB = self.findChild(QPushButton, "Export_PB")
        self.Add_Point_PB = self.findChild(QPushButton, "Add_Point_PB")
        self.Remove_Point_PB = self.findChild(QPushButton, "Remove_Point_PB")

        self.Index_1_label = self.findChild(QLabel, "Index_1_label")
        self.Index_1_radioButton = self.findChild(
            QRadioButton, "Index_1_radioButton")
        self.CC_1_label = self.findChild(QLabel, "CC_1_label")
        self.CC_1_lineEdit = self.findChild(QLineEdit, "CC_1_lineEdit")
        self.Duty_cycle_1_label = self.findChild(QLabel, "Duty_cycle_1_label")
        self.Duty_cycle_1_lineEdit = self.findChild(
            QLineEdit, "Duty_cycle_1_lineEdit")
        self.Beat_rate_1_label = self.findChild(QLabel, "Beat_rate_1_label")
        self.Beat_rate_1_lineEdit = self.findChild(
            QLineEdit, "Beat_rate_1_lineEdit")
        self.IMPORT_1_PB = self.findChild(QPushButton, "IMPORT_1_PB")
        self.SAVE_1_PB = self.findChild(QPushButton, "SAVE_1_PB")
        self.EXPORT_1_PB = self.findChild(QPushButton, "EXPORT_1_PB")

        self.Index_2_label = self.findChild(QLabel, "Index_2_label")
        self.Index_2_radioButton = self.findChild(
            QRadioButton, "Index_2_radioButton")
        self.CC_2_label = self.findChild(QLabel, "CC_2_label")
        self.CC_2_lineEdit = self.findChild(QLineEdit, "CC_2_lineEdit")
        self.Duty_cycle_2_label = self.findChild(QLabel, "Duty_cycle_2_label")
        self.Duty_cycle_2_lineEdit = self.findChild(
            QLineEdit, "Duty_cycle_2_lineEdit")
        self.Beat_rate_2_label = self.findChild(QLabel, "Beat_rate_2_label")
        self.Beat_rate_2_lineEdit = self.findChild(
            QLineEdit, "Beat_rate_2_lineEdit")
        self.IMPORT_2_PB = self.findChild(QPushButton, "IMPORT_2_PB")
        self.SAVE_2_PB = self.findChild(QPushButton, "SAVE_2_PB")
        self.EXPORT_2_PB = self.findChild(QPushButton, "EXPORT_2_PB")

        self.Index_3_label = self.findChild(QLabel, "Index_3_label")
        self.Index_3_radioButton = self.findChild(
            QRadioButton, "Index_3_radioButton")
        self.CC_3_label = self.findChild(QLabel, "CC_3_label")
        self.CC_3_lineEdit = self.findChild(QLineEdit, "CC_3_lineEdit")
        self.Duty_cycle_3_label = self.findChild(QLabel, "Duty_cycle_3_label")
        self.Duty_cycle_3_lineEdit = self.findChild(
            QLineEdit, "Duty_cycle_3_lineEdit")
        self.Beat_rate_3_label = self.findChild(QLabel, "Beat_rate_3_label")
        self.Beat_rate_3_lineEdit = self.findChild(
            QLineEdit, "Beat_rate_3_lineEdit")
        self.IMPORT_3_PB = self.findChild(QPushButton, "IMPORT_3_PB")
        self.SAVE_3_PB = self.findChild(QPushButton, "SAVE_3_PB")
        self.EXPORT_3_PB = self.findChild(QPushButton, "EXPORT_3_PB")

        self.Index_4_label = self.findChild(QLabel, "Index_4_label")
        self.Index_4_radioButton = self.findChild(
            QRadioButton, "Index_4_radioButton")
        self.CC_4_label = self.findChild(QLabel, "CC_4_label")
        self.CC_4_lineEdit = self.findChild(QLineEdit, "CC_4_lineEdit")
        self.Duty_cycle_4_label = self.findChild(QLabel, "Duty_cycle_4_label")
        self.Duty_cycle_4_lineEdit = self.findChild(
            QLineEdit, "Duty_cycle_4_lineEdit")
        self.Beat_rate_4_label = self.findChild(QLabel, "Beat_rate_4_label")
        self.Beat_rate_4_lineEdit = self.findChild(
            QLineEdit, "Beat_rate_4_lineEdit")
        self.IMPORT_4_PB = self.findChild(QPushButton, "IMPORT_4_PB")
        self.SAVE_4_PB = self.findChild(QPushButton, "SAVE_4_PB")
        self.EXPORT_4_PB = self.findChild(QPushButton, "EXPORT_4_PB")

        self.Index_5_label = self.findChild(QLabel, "Index_5_label")
        self.Index_5_radioButton = self.findChild(
            QRadioButton, "Index_5_radioButton")
        self.CC_5_label = self.findChild(QLabel, "CC_5_label")
        self.CC_5_lineEdit = self.findChild(QLineEdit, "CC_5_lineEdit")
        self.Duty_cycle_5_label = self.findChild(QLabel, "Duty_cycle_5_label")
        self.Duty_cycle_5_lineEdit = self.findChild(
            QLineEdit, "Duty_cycle_5_lineEdit")
        self.Beat_rate_5_label = self.findChild(QLabel, "Beat_rate_5_label")
        self.Beat_rate_5_lineEdit = self.findChild(
            QLineEdit, "Beat_rate_5_lineEdit")
        self.IMPORT_5_PB = self.findChild(QPushButton, "IMPORT_5_PB")
        self.SAVE_5_PB = self.findChild(QPushButton, "SAVE_5_PB")
        self.EXPORT_5_PB = self.findChild(QPushButton, "EXPORT_5_PB")
        
        
        # self.OK_PB = QPushButton()
        # self.shortcut_pressed = QShortcut(QKeySequence('Ctrl+G'), self)
        # self.shortcut_pressed.activated.connect(self.Export_PB_CLICKED)
        
        self.shortcut_OK_PB_pressed = QShortcut(QKeySequence('ENTER'), self)
        self.shortcut_OK_PB_pressed.activated.connect(self.OK_PB_CLICKED)
        
        
        ##################################################################################################################################################

        # self.figure = plt.figure()

        # # plt.tight_layout()
        # self.canvas = FigureCanvas(self.figure)
        # self.toolbar = NavigationToolbar(self.canvas, None)

        # self.Graph_layout.addWidget(self.toolbar)
        # self.Graph_layout.addWidget(self.canvas)

        # self.graph_axes = self.figure.add_subplot(111)
        # self.Graph_layout.addWidget(self.figure.canvas)
        
        ######################################################################################################################################################
        
        self.t2 = sine_graph()
        self.t1 = import_data() 
        
                       
        self.Graph_layout.addWidget(self.t2.toolbar)
        self.Graph_layout.addWidget(self.t2.canvas)
        self.Graph_layout.addWidget(self.t2.figure.canvas)
        
        ######################################################################################################################################################
        
        self.shortcut_pressed = QShortcut(QKeySequence('Ctrl+G'), self)
        # self.shortcut_pressed.activated.connect(self.t2.Export_PB_CLICKED)

        # Do something
        self.OK_PB.clicked.connect(self.OK_PB_CLICKED)
        self.Export_PB.clicked.connect(self.t2.Export_PB_CLICKED)
        # self.Add_Point_PB.clicked.connect(self.Add_Point_PB_CLICKED)
        # self.Remove_Point_PB.clicked.connect(self.Remove_Point_PB_CLICKED)
        
        
        # Connect the toggled signal of Index_2_radioButton to the enable_import_button_2 method
        self.Index_1_radioButton.toggled.connect(self.enable_import_button_1)
        self.Index_2_radioButton.toggled.connect(self.enable_import_button_2)
        self.Index_3_radioButton.toggled.connect(self.enable_import_button_3)
        self.Index_4_radioButton.toggled.connect(self.enable_import_button_4)
        self.Index_5_radioButton.toggled.connect(self.enable_import_button_5)
        
        self.SAVE_1_PB.clicked.connect(self.t2.Export_PB_CLICKED)
        self.SAVE_2_PB.clicked.connect(self.export_button)
        self.SAVE_3_PB.clicked.connect(self.export_button)
        self.SAVE_4_PB.clicked.connect(self.export_button)
        self.SAVE_5_PB.clicked.connect(self.export_button)
        
        self.IMPORT_1_PB.clicked.connect(self.import_button)
        self.IMPORT_2_PB.clicked.connect(self.import_button)
        self.IMPORT_3_PB.clicked.connect(self.import_button)
        self.IMPORT_4_PB.clicked.connect(self.import_button)
        self.IMPORT_5_PB.clicked.connect(self.import_button)
        
        # Disable the IMPORT_2_PB by default
        self.IMPORT_1_PB.setEnabled(False)
        self.IMPORT_2_PB.setEnabled(False)
        self.IMPORT_3_PB.setEnabled(False)
        self.IMPORT_4_PB.setEnabled(False)
        self.IMPORT_5_PB.setEnabled(False)
        
        self.SAVE_1_PB.setEnabled(False)
        self.SAVE_2_PB.setEnabled(False)
        self.SAVE_3_PB.setEnabled(False)
        self.SAVE_4_PB.setEnabled(False)
        self.SAVE_5_PB.setEnabled(False)
        
        self.EXPORT_1_PB.setEnabled(False)
        self.EXPORT_2_PB.setEnabled(False)
        self.EXPORT_3_PB.setEnabled(False)
        self.EXPORT_4_PB.setEnabled(False)
        self.EXPORT_5_PB.setEnabled(False)
        
        # self.IMPORT_1_PB.clicked.connect(self.t1.import_sine_data)             #   self.IMPORT_1_PB.clicked.connect(self.import_button)            both are same
        
        x = []
        y = []
        z = []
        
        self.Beat_Rate_Text = int(60)
        self.CC_Text = int(2402)
        self.Duty_Text = int(50)
        self.Points = int(1024)
        
        # Show The App
        self.show()
    
    def enable_import_button_1(self, checked):
        # Enable the IMPORT_2_PB when Index_2_radioButton is checked and disable it otherwise
        self.IMPORT_1_PB.setEnabled(checked)
        self.SAVE_1_PB.setEnabled(checked)
        self.EXPORT_1_PB.setEnabled(checked)
        
    def enable_import_button_2(self, checked):
        # Enable the IMPORT_2_PB when Index_2_radioButton is checked and disable it otherwise
        self.IMPORT_2_PB.setEnabled(checked)
        self.SAVE_2_PB.setEnabled(checked)
        self.EXPORT_2_PB.setEnabled(checked)
        
        # self.IMPORT_2_PB.setEnabled(True)                 #   only one time working
        
    def enable_import_button_3(self, checked):
        # Enable the IMPORT_2_PB when Index_2_radioButton is checked and disable it otherwise
        self.IMPORT_3_PB.setEnabled(checked)
        self.SAVE_3_PB.setEnabled(checked)
        self.EXPORT_3_PB.setEnabled(checked)
        
    def enable_import_button_4(self, checked):
        # Enable the IMPORT_2_PB when Index_2_radioButton is checked and disable it otherwise
        self.IMPORT_4_PB.setEnabled(checked)
        self.SAVE_4_PB.setEnabled(checked)
        self.EXPORT_4_PB.setEnabled(checked)
        
    def enable_import_button_5(self, checked):
        # Enable the IMPORT_2_PB when Index_2_radioButton is checked and disable it otherwise
        self.IMPORT_5_PB.setEnabled(checked)
        self.EXPORT_1_PB.setEnabled(checked)
        self.SAVE_5_PB.setEnabled(checked)

    def OK_PB_CLICKED(self):
        self.Points = 1024

        if self.Index_1_radioButton.isChecked():
            index = 1
            
        elif self.Index_2_radioButton.isChecked():
            index = 2
            
        elif self.Index_3_radioButton.isChecked():
            index = 3
            
        elif self.Index_4_radioButton.isChecked():
            index = 4
            
        elif self.Index_4_radioButton.isChecked():
            index = 5
            
        else:
            return  # No radio button is selected, do nothing
        
        if index == 1:
            
            print(f"i am in index_{index}")
            self.CC_Text = int(getattr(self, f"CC_{index}_lineEdit").text())
            print(self.CC_Text)
            self.Duty_Text = int(getattr(self, f"Duty_cycle_{index}_lineEdit").text())
            print(self.Duty_Text)
            self.Beat_Rate_Text = int(getattr(self, f"Beat_rate_{index}_lineEdit").text())
            print(self.Beat_Rate_Text)
            
            self.t2.generate_points_by_click(self.Points, self.CC_Text, self.Duty_Text, self.Beat_Rate_Text)
        
        elif index > 1:
            
            print(f"i am in index_{index}")
            self.CC_Text = int(getattr(self, f"CC_{index}_lineEdit").text())
            print(self.CC_Text)
            self.Duty_Text = int(getattr(self, f"Duty_cycle_{index}_lineEdit").text())
            print(self.Duty_Text)
            self.Beat_Rate_Text = int(getattr(self, f"Beat_rate_{index}_lineEdit").text())
            print(self.Beat_Rate_Text)

            self.t2.plot_now(self.Points, self.CC_Text, self.Duty_Text, self.Beat_Rate_Text)
            
        else:
            pass

    def export_button(self):
        
        self.x = self.t2.Points_list
        self.y = self.t2.displacement_list
        self.z = self.t2.time_list
        
        self.t2.data_export(self.Beat_Rate_Text,self.CC_Text,self.Duty_Text,self.x, self.y, self.z)
        
    def import_button(self):
        # self.import_data_file()
        
        if self.Index_1_radioButton.isChecked():
            index = 1

        elif self.Index_2_radioButton.isChecked(): 
            index = 2
               
        elif self.Index_3_radioButton.isChecked():
            index = 3

        elif self.Index_4_radioButton.isChecked():
            index = 4

        elif self.Index_5_radioButton.isChecked():
            index = 5
            
        else:
            pass
        
        self.import_data_file()            
        print(f"i am in index_{index}")
        getattr(self, f"Beat_rate_{index}_lineEdit").setText(str(self.a))
        getattr(self, f"CC_{index}_lineEdit").setText(str(self.b))
        getattr(self, f"Duty_cycle_{index}_lineEdit").setText(str(self.c))
        
        self.d = self.t1.x_values
        self.e = self.t1.y_values
        
        self.t2.plot_graph(self.e,self.d)
        
    def import_data_file(self):
        self.t1.import_sine_data()
        self.a = self.t1.import_Beat_Rate
        self.b = self.t1.import_CC
        self.c = self.t1.import_Duty_Cycle
        
        
    
# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

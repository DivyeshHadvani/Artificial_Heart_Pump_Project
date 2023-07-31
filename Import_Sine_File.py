import pickle
import math

import openpyxl
import matplotlib.pyplot as plt

import pandas as pd

import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLabel


class import_data(QWidget):

    def __init__(self):
        super().__init__()
        
        self.import_Beat_Rate = 60
        self.import_CC = 2402
        self.import_Duty_Cycle = 50
        self.x_values = []
        self.y_values = []
    

    def import_sine_data(self):

        self.get_file_location()

    def import_complex_data(self):
        
        self.get_file_location()

    def get_file_location(self):

        options = QFileDialog.Options()
        
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select File", "", "All Files (*)", options=options)

        if file_name:
            print(file_name)

            # old_path = file_name

            # # Convert the old path to a preferred path format
            # preferred_path = os.path.normpath(old_path)

            # # Print the converted path
            # print(preferred_path)

            var = pd.read_excel(file_name)
            print(var)         

            a_values = list(var['Parameters Name'])
            b_values = list(var['Parameters Value'])
            b_values_new = b_values[:3]
            
            int_b_values_new_list = [int(x) for x in b_values_new]

            # Remove float values using the filter() function
            a_values_new = [x for x in a_values if not isinstance(x, float)]
            
            ##################################################################################################################
            #both are same and working 
            # filtered_list = list(
            #     filter(lambda x: not isinstance(x, float), a_values))
            ##################################################################################################################
            
            self.Points = 1024
            
            self.import_Beat_Rate =  int_b_values_new_list[0]
            self.import_CC=  int_b_values_new_list[1]
            self.import_Duty_Cycle =  int_b_values_new_list[2]

            self.x_values = list(var['Time (ms)'])
            self.y_values = list(var['Displacement'])

            print(a_values_new)
            # print(b_values_new)
            print(int_b_values_new_list)
            # print(x_values)
            # print(y_values)
            # print(type(y_values[1]))
            
    def complex_polinomial_graph_plot_with_import():
        pass


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QVBoxLayout, QWidget, QPushButton


# class FileDialogApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.init_ui()

#     def init_ui(self):
#         self.text_edit = QTextEdit(self)
#         self.setCentralWidget(self.text_edit)

#         self.create_actions()
#         self.create_toolbar()

#         self.setWindowTitle('File Save & Open Example')
#         self.setGeometry(100, 100, 800, 600)

#     def create_actions(self):
#         self.save_action = QAction('Save', self)
#         self.save_action.triggered.connect(self.save_file)

#         self.open_action = QAction('Open', self)
#         self.open_action.triggered.connect(self.open_file)

#     def create_toolbar(self):
#         toolbar = self.addToolBar('File Operations')
#         toolbar.addAction(self.save_action)
#         toolbar.addAction(self.open_action)

#     def save_file(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'w') as file:
#                 text = self.text_edit.toPlainText()
#                 file.write(text)

#     def open_file(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'r') as file:
#                 text = file.read()
#                 self.text_edit.setPlainText(text)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = FileDialogApp()
#     window.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLabel


# class FileLocationApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.init_ui()

#     def init_ui(self):
#         self.label = QLabel("File Location: ", self)
#         self.file_location_button = QPushButton("Select File", self)
#         self.file_location_button.clicked.connect(self.get_file_location)

#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.file_location_button)

#         central_widget = QWidget(self)
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         self.setWindowTitle('Get File Location Example')
#         self.setGeometry(100, 100, 400, 100)

#     def get_file_location(self):
#         options = QFileDialog.Options()
#         print("option")
#         print(type(options))
#         file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)

#         if file_name:
#             self.label.setText("File Location: " + file_name)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = FileLocationApp()
#     window.show()
#     sys.exit(app.exec_())

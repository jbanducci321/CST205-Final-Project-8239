'''
Title: 2nd_page.py
Author: Mohammad Shahroudi
Abstract: This file will have gui.
Date: April 21, 2025
'''

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox, 
                                  QHBoxLayout, QVBoxLayout, QPushButton, 
                                  QComboBox, QLineEdit)
from PySide6.QtCore import Slot  
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property
from questions import questions

app = QApplication([])

# excited as 5
# happy as 4
# neutral as 3
# upset as 2
# angry as 1

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
         
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())

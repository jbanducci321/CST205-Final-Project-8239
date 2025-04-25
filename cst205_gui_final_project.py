'''
Title: cst205_gui_final_project.py
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
        # self.UiComponents()
        self.my_list = ["Choose a mood: ", "Excited", "Happy",
                        "Neutral", "Upset", "Angry"]
        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_label = QLabel("")
        self.my_lbl = QLabel('')
        my_btn = QPushButton("Enter")
        my_btn.clicked.connect(self.on_click)


        vbox = QVBoxLayout()
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_label)
        vbox.add_widget(self.my_lbl)
        vbox.add_widget(my_btn)
        self.set_layout(vbox)
        #self.show()
        self.my_combo_box.currentIndexChanged.connect(self.update_text)

    @Slot()
    def update_text(self):
        my_text = self.my_combo_box.current_text
        my_index = self.my_combo_box.current_index
        self.my_label.text = f'{self.my_list[my_index]}'

    @Slot()
    def on_click(self):
        self.my_lbl.text = "You hit enter"
        


        
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Slot, Qt
from __feature__ import snake_case, true_property

app = QApplication([])

class SecondaryWindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        second_page = QLabel("Welcome to the 2nd Page")
        my_second_button = QPushButton("Return")
        self.my_lbl = QLabel()
        my_second_button.clicked.connect(self.on_click)

        vbox.add_widget(second_page)
        vbox.add_widget(my_second_button)
        vbox.add_widget(self.my_lbl)
        self.set_layout(vbox)
        self.show()

    @Slot()  
    def on_click(self):
        self.my_lbl.text = "Success!"

secondary_window = SecondaryWindow()
secondary_window.show()
sys.exit(app.exec())

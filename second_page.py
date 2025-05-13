import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox)
# from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Slot, Qt
from __feature__ import snake_case, true_property


class Page2(QWidget):
    def __init__(self):
        super().__init__()
        main_menu = QLabel("Welcome to the Second Page")
        enter_btn = QPushButton("Enter")
        self.my_label = QLabel()
        enter_btn.clicked.connect(self.on_click)

        vbox = QVBoxLayout()
        vbox.add_widget(main_menu)
        vbox.add_widget(enter_btn)
        vbox.add_widget(self.my_label)
        self.set_layout(vbox)
        self.show()


    @Slot()
    def on_click(self):
        self.my_label.text = "Success!"


# app = QApplication([])
# page_2 = Page2()
# page_2.show()
# sys.exit(app.exec())    

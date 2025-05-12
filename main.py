import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Slot, Qt
from __feature__ import snake_case, true_property

app = QApplication([])

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        main_menu = QLabel("Welcome to the Main Menu")
        my_btn = QPushButton("Enter")
        self.my_label = QLabel()
        my_btn.clicked.connect(self.on_click)

        vbox.add_widget(main_menu)
        vbox.add_widget(my_btn)
        vbox.add_widget(self.my_label)
        self.set_layout(vbox)
        self.show()

    @Slot()
    def on_click(self):
        self.my_label.text = "Button Pressed!"


main_window = MainWindow()
sys.exit(app.exec())

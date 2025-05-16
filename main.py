import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, 
                                QMainWindow, QComboBox, QStackedWidget)
# from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Slot, Qt
from __feature__ import snake_case, true_property
from first_page import Page1
from second_page import Page2

# In this file, my goal was to
# be able to change pages with the click of a button
# to either page 1 or page 2

# class AnotherWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window")
#         layout.add_widget(self.label)
#         self.set_layout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()

        # Create some pages
        self.page1 = QLabel("Page 1")
        self.page2 = QLabel("Page 2")

        # Add pages to the stacked widget
        self.stacked_widget.add_widget(self.page1)
        self.stacked_widget.add_widget(self.page2)

        # Create buttons to switch pages
        self.button1 = QPushButton("Go to Page 1")
        self.button1.clicked.connect(self.show_page1)
        self.button2 = QPushButton("Go to Page 2")
        self.button2.clicked.connect(self.show_page2)

        layout = QVBoxLayout()
        layout.add_widget(self.button1)
        layout.add_widget(self.button2)
        layout.add_widget(self.stacked_widget)
        self.set_layout(layout)

        # main_menu = QLabel("Welcome to the Main Page")
        # enter_btn = QPushButton("Enter")
        # self.my_label = QLabel()
        # enter_btn.clicked.connect(self.on_click)

        # vbox = QVBoxLayout()
        # vbox.add_widget(main_menu)
        # vbox.add_widget(enter_btn)
        # vbox.add_widget(self.my_label)
        # self.set_layout(vbox)

        

    def show_page1(self):
        self.stacked_widget.set_current_index = 0
        page_1 = Page1()
        page_1.show()
        #sys.exit(app.exec())   

    def show_page2(self):
        self.stacked_widget.set_current_index = 1
        page_2 = Page2()
        page_2.show()
        #sys.exit(app.exec())   

    # @Slot()
    # def on_click(self):
    #     self.my_label.text = "Success!"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec() 

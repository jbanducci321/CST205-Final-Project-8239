import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
from Display_Board import MainWindow
from __feature__ import snake_case, true_property
app = QApplication([])



class MyWindow(QWidget):
  def __init__(self):
    super().__init__()
    
    btn = QPushButton('CLICK ME')
    vbox = QVBoxLayout()
   
    vbox.add_widget(btn)
    self.set_layout(vbox)
    btn.clicked.connect(self.open_win)

  @Slot() 
  def open_win(self):
    self.new_win = MainWindow('sad')
    self.new_win.show()

main = MyWindow()
main.show()
sys.exit(app.exec())
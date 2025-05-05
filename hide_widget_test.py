import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
from Display_Board import MainWindow
from __feature__ import snake_case, true_property


class InputWindow(QWidget):
  def __init__(self):
    super().__init__()

    my_label = QLabel("Enter an emotion to generate a mood board")
    self.emotion_text = QLineEdit()
    btn = QPushButton("Enter")
    self.emotion_text.returnPressed.connect(self.switch_window)
    vbox = QVBoxLayout()

    vbox.add_widget(my_label)
    vbox.add_widget(self.emotion_text)
    vbox.add_widget(btn)
    self.set_layout(vbox)
    btn.clicked.connect(self.switch_window)
    self.resize(250,250)

  @Slot() 
  def switch_window(self):
    emotion = self.emotion_text.text.strip()
    if emotion:
       self.new_window = MainWindow(emotion)
       self.new_window.show()
       self.hide()

    


app = QApplication([])
main = InputWindow()
main.show()
sys.exit(app.exec())
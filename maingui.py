import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property
app = QApplication([])



mood_list = ['sad', 'neutral','happy', 'mad', 'anxious']
day_list = ['good', 'boring', 'stressful']

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.window_title = 'Mood Board Generator'

    self.label = QLabel("How are you feeling today?")
    self.combo_box = QComboBox()
    self.combo_box.add_items(mood_list)

    self.label2 = QLabel("How is your day going?")
    self.day_box = QComboBox()
    self.day_box.add_items(day_list)

    self.proceed_button = QPushButton("Show Mood Board")

    layout = QVBoxLayout()
    layout.add_widget(self.label)
    layout.add_widget(self.combo_box)
    layout.add_widget(self.label2)
    layout.add_widget(self.day_box)
    layout.add_widget(self.proceed_button)
    self.set_layout(layout)

    self.proceed_button.clicked.connect(self.open_win)

  @Slot()
  def open_win(self):
    selected_index = self.combo_box.current_index
    selected_mood = mood_list[selected_index]
    self.new_win = NewWindow(selected_mood)
    self.new_win.show()

class NewWindow(QWidget):
  def __init__(self, mood):
      super().__init__()
      mood_label = QLabel(f"You selected: {mood}")
      layout = QVBoxLayout()
      layout.add_widget(mood_label)
      self.set_layout(layout)


main = MyWindow()
main.show()
sys.exit(app.exec())

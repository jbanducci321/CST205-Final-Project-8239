import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, 
                                QHBoxLayout, QVBoxLayout, QDialog, QTextBrowser, QComboBox)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Slot, Qt
from Display_Board import MainWindow
from __feature__ import snake_case, true_property
from io import BytesIO
from get_images import search_images

app = QApplication([])


mood_list = ['Choose a mood','sad', 'neutral','happy', 'angry', 'anxious']
day_list = ['Choose an answer' , 'good', 'boring', 'stressful']
fun_list = ['Choose an answer', 'Today', 'Yesterday', 'This week', 'A while ago', 'I can\'t remember']

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.style_sheet = "background-color: white; color: black;font-size: 16px;font-family: Arial;"

    #Title
    self.window_title = 'Mood Board Generator'
    self.page_title = QLabel("Welcome to Your Mood Board Generator!")
    self.page_title.style_sheet = "font-size: 24px; font-weight: bold; margin-bottom: 20px;"

    #image
    self.image_label = QLabel()
    self.image_pixmap = QPixmap("mood2.png")
    scaled_pixmap = self.image_pixmap.scaled(500, 500,Qt.KeepAspectRatio)
    self.image_label.pixmap = scaled_pixmap   

    #question 1
    self.label = QLabel("Enter what emotion you're feeling right now (one word)")
    self.main_emotion = QLineEdit()
    #self.combo_box = QComboBox()
    #self.combo_box.add_items(mood_list)
    #self.combo_box.set_style_sheet("border: 2px solid black;")

    #question 2
    self.label2 = QLabel("How is your day going?")
    self.day_box = QComboBox()
    self.day_box.add_items(day_list)
    self.day_box.set_style_sheet("border: 2px solid black;")

    #question 3
    self.label3 = QLabel("When is the last time you did something fun?")
    self.fun_time_box = QComboBox()
    self.fun_time_box.add_items(fun_list)
    self.fun_time_box.set_style_sheet("border: 2px solid black;")


    #question 4
    self.label4 = QLabel("Do you feel more introverted or extroverted right now?")
    self.introvert_button = QPushButton("Introverted")
    self.extrovert_button = QPushButton("Extroverted")
    self.selected_social = ""

    self.introvert_button.clicked.connect(self.select_introvert)
    self.introvert_button.set_style_sheet("background-color: lightblue;")
    self.extrovert_button.clicked.connect(self.select_extrovert)
    self.extrovert_button.set_style_sheet("background-color: lightblue;")


    #question 5
    self.label5 = QLabel("How would you rate your current energy (1–10)?")
    self.energy_input = QLineEdit()
    self.energy_input.placeholder_text = "Type a number from 1 to 10"
    self.energy_input.set_style_sheet("border: 2px solid black;")


    self.proceed_button = QPushButton("Show Mood Board")
    self.proceed_button.set_style_sheet("background-color: lightblue;")

    layout = QVBoxLayout()
    layout.add_widget(self.page_title)
    layout.add_widget(self.image_label)
    layout.add_spacing(20)

    layout.add_widget(self.label)
    layout.add_widget(self.main_emotion)
    layout.add_spacing(20)

    layout.add_widget(self.label2)
    layout.add_widget(self.day_box)
    layout.add_spacing(20)

    layout.add_widget(self.label3)
    layout.add_widget(self.fun_time_box)
    layout.add_spacing(20)

    layout.add_widget(self.label4)
    layout.add_widget(self.introvert_button)
    
    layout.add_widget(self.extrovert_button)
    layout.add_spacing(10)

    layout.add_widget(self.label5)
    layout.add_widget(self.energy_input)
    layout.add_spacing(10)

    layout.add_widget(self.proceed_button)
    self.set_layout(layout)

    self.proceed_button.clicked.connect(self.open_win)

  @Slot()
  def select_introvert():
      self.selected_social = "Introverted"
      
  @Slot()
  def select_extrovert():
      self.selected_social = "Extroverted"

  @Slot()
  def open_win(self):
      emotion = self.main_emotion.text
      #selected_mood = mood_list[selected_index]
      self.new_win = MainWindow(emotion)
      self.new_win.show_maximized()
      self.hide()

main = MyWindow()
main.show()
sys.exit(app.exec())

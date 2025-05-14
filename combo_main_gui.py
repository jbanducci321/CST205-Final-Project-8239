# Course: CST 205-01
# Title: Mood Board Generator
# Abstract: The Mood Board Generator is a Pyside 6 based app that helps users reflect on how they're feeling by asking a few thoughtful questions. 
# Based on their responses, it creates a personalized mood board filled with images that match their current mood.
# It showcases GUI design, user interaction, and image based storytelling.
# Authors: 
#   - Brianna Magallon - Designed and built the main user interface, including the layout, input questions, and logic for launching the mood board window. (MyWindow and Maingui.py)
#   - Joshua Sumagang - Video get, download, and display functionality
#   - Mohammad Shahroudi - main_gui.py
#   - Jacob Banducci- Worked on the image API functions, the collage creator, background code with the emolex and MainWindow GUI
# Date: May 14, 2025

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, 
                               QComboBox, QDialog, QLineEdit, QLayout, QScrollArea)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from PySide6.QtWebEngineWidgets import QWebEngineView
from __feature__ import snake_case, true_property
from get_images import search_images
from io import BytesIO
import os
import string
from get_vid import search_youtube_videos
from dl_yt import download_video, download_audio

#Fallback incase it doesn't display the video on some systems.
if "QTWEBENGINE_CHROMIUM_FLAGS" not in os.environ:
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu"

app = QApplication([])

# The list of how is your day going.
day_list = ['Choose an answer' , 'good', 'boring', 'stressful']
# The list of when is the last time that you did something fun.
fun_list = ['Choose an answer', 'Today', 'Yesterday', 'This week', 'A while ago', 'I can\'t remember']

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    #basic style
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
    self.label = QLabel("How are you feeling today?")
    self.main_emotion = QLineEdit()
    self.main_emotion.placeholder_text = "Type a mood"
    self.main_emotion.set_style_sheet("border: 2px solid black;")

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
    self.main_emotion.returnPressed.connect(self.open_win)

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



class MainWindow(QWidget):
    def __init__(self, emotion):
        super().__init__()
        img_label = QLabel() #Creates a label object to hold an image
        
        #Cleans up the string for emotion
        emotion = emotion.strip() #Removes leading/trailing whitespace
        emotion = emotion.lower()

        if emotion:
            words = emotion.split() #Splits the string into individual words (if a sentence is passed)
            if words:
                emotion = words[0] #Takes only the first word in the list
            else:
                emotion = ''
        else:
            emotion = ''
        
        #Removes punctuation
        emotion = "".join(char for char in emotion if char not in string.punctuation)
        
        #Defaults to neutral if the string is empty
        if not emotion:
            emotion = 'neutral'

        #Calls the image search function
        pil_img, emotion_returned = search_images(emotion)
        title_label = QLabel(f'Showing Media related to: {emotion_returned.capitalize()}')
        title_label.style_sheet = 'font-size: 24px; font-weight: bold; margin-bottom: 20px;'

        self.pil_img = pil_img
        
        if pil_img:
            #Converts PIL image to QPixmap
            buffer = BytesIO()
            pil_img.save(buffer, format='PNG') #Saves image to the buffer
            qimage = QImage.from_data(buffer.getvalue())
            pixmap = QPixmap.from_image(qimage)
            
            pixmap = pixmap.scaled(1000, 600) #Sets the scale for the image label
            
            img_label.pixmap = pixmap
            img_label.alignment = Qt.AlignCenter
        
        #Creates a vbox to store the image label and related widgets
        img_vbox = QVBoxLayout()
        img_vbox.set_alignment(Qt.AlignTop)

        save_lable = QLabel("Push the button to save the mood board")
        save_lable.alignment = Qt.AlignCenter #Aligns the label to the center

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_image) #Connects the button to the save image fuction
        save_btn.set_fixed_width(200)

        #Lets you go back to the 
        back_button = QPushButton('Back to Home')
        back_button.clicked.connect(self.back_btn)

        #Add widgets to img_vbox
        img_vbox.add_widget(title_label, alignment=Qt.AlignCenter)
        img_vbox.add_widget(img_label)
        img_vbox.add_widget(save_lable, alignment=Qt.AlignCenter)
        img_vbox.add_widget(save_btn, alignment=Qt.AlignCenter)
        

        #Creates a main display vbox and adds the img_vbox to it
        main_display_vbox = QVBoxLayout()
        main_display_vbox.add_layout(img_vbox)

        #WebEngineView
        self.video_view = QWebEngineView()
        #Get video URLs
        self.vid_urls = search_youtube_videos(emotion)
        html = f'''
        <html>
          <body>
            <iframe width="100%" height="100%"
              src="https://www.youtube.com/embed/{self.vid_urls[0]}"
              frameborder="0"
              allowfullscreen>
            </iframe>
          </body>
        </html>
        '''
        self.video_view.set_html(html)
        self.video_view.set_fixed_size(800, 450)
        # Create the video download button
        download_button = QPushButton("Download Video")
        download_button.clicked.connect(self.dl_window)

        #VBox for the video view
        vid_vbox = QVBoxLayout()
        #Add widgets to vid_vbox
        vid_vbox.add_widget(self.video_view, stretch = 1, alignment=Qt.AlignCenter)
        vid_vbox.add_widget(download_button, alignment=Qt.AlignCenter)

        main_display_vbox.add_layout(vid_vbox)

        #Creates a contianer to hold the entire layout
        scroll_container = QWidget()
        scroll_container.set_layout(main_display_vbox) #Adds the main layout vbox to the new container
        main_display_vbox.set_alignment = Qt.AlignCenter

        #Creates a scroll area to enable scrolling
        scroll_area = QScrollArea()
        scroll_area.set_widget(scroll_container)
        scroll_area.widget_resizable = True #Ensures scroll area fills up the window its in
        
        #Creates the top-level layout for the display
        main_layout = QVBoxLayout()
        main_layout.add_widget(scroll_area) #Adds the scroll area to it
        main_layout.add_widget(back_button, alignment=Qt.AlignCenter)

        self.set_layout(main_layout)
        self.window_title = "Media Display"
    
    
    @Slot()
    def save_image(self): 
        dialog = SaveDialog(self.pil_img) #Passes the image object to the new window
        dialog.exec()

    @Slot()
    def dl_window(self):
        dialog = SaveVideoWindow(self.vid_urls[1])
        dialog.exec()
    
    @Slot()
    def back_btn(self):
        main_window = MyWindow()
        main_window.show()
        self.close()

#Dialog class for displaying the window for saving the image
class SaveDialog(QDialog):
    def __init__(self, image):
        super().__init__()
        self.window_title = "Save Mood Board" #Sets the window title
        self.image = image
        
        layout = QVBoxLayout() #Creates a v box for main layout
        
        #Creates the text entry lines for file name/path
        self.name_input = QLineEdit()
        self.path_input = QLineEdit()
        
        #Creates a save button and connects it to the save image method
        self.save_button = QPushButton("Save")
        self.save_button.set_default = True #Pressing enter pushes the save button
        self.save_button.clicked.connect(self.save_image)
        
        #Adds all the widgets to the v box layout
        layout.add_widget(QLabel("File Name:"))
        layout.add_widget(self.name_input)
        layout.add_widget(QLabel("Leave file name blank for default (add .png)"))
        layout.add_widget(QLabel())
        layout.add_widget(QLabel("Save Location:"))
        layout.add_widget(self.path_input)
        layout.add_widget(QLabel("Leave file path blank for default"))
        layout.add_widget(self.save_button, alignment=Qt.AlignCenter)
        self.resize(200, 200)
        
        self.set_layout(layout)

    #Method for saving the image
    @Slot()
    def save_image(self):
        #Gets the file name/path from the line edits
        filename = self.name_input.text.strip() #Strip handles issues with white space
        folder = self.path_input.text.strip()
        
        #If line edits are left blank then it sets them to default
        if not filename:
            filename = "mood_board.png"
        
        if not folder:
            folder = os.getcwd() #Selects the current working directory
        
        save_path = os.path.join(folder, filename) #Creates the save path
        
        #Checks whether the image saved or not and displays status to the user
        try:
            self.image.save(save_path) #Saves the image
            status_dialog = StatusDialog("Image saved sucessfully")
            status_dialog.exec()
        except Exception as e:
            status_dialog = StatusDialog(f'Error saving image: {e}')
            status_dialog.exec()
        finally:
            self.accept() #Closes the dialog box after try/except resolves

class SaveVideoWindow(QDialog):
    def __init__(self, vid_url):
        super().__init__()
        self.window_title = "Save Video"
        self.vid_url = vid_url

        layout = QVBoxLayout()

        self.combo_box = QComboBox()
        self.combo_box.add_items(['Download Video', 'Download Audio'])

        self.save_button = QPushButton("Save")
        self.save_button.set_default = True
        self.save_button.clicked.connect(self.dl_vid)

        layout.add_widget(self.combo_box, alignment=Qt.AlignCenter)
        layout.add_widget(self.save_button, alignment=Qt.AlignCenter)

        self.set_layout(layout)
        self.resize(200, 200)

    @Slot()
    def dl_vid(self):
        choice = self.combo_box.current_text

        try:
            if choice == 'Download Video':
                download_video(self.vid_url)
                status_text = "Video saved successfully"
            else:
                download_audio(self.vid_url)
                status_text = "Audio saved successfully"

            status_dialog = StatusDialog(status_text)
            status_dialog.exec()

        except Exception as e:
            status_dialog = StatusDialog(f"Error saving: {e}")
            status_dialog.exec()

        finally:
            self.accept()


class StatusDialog(QDialog):
    def __init__(self, status_text):
        super().__init__()
         
        self.window_title = "Save Status"
        
        layout = QVBoxLayout()
        layout.size_constraint = QLayout.SizeConstraint.SetFixedSize
        
        #Creates the status message with the passed text
        status_lbl = QLabel(status_text) 
        status_lbl.alignment = Qt.AlignCenter #Sets label alignment to center
        
        #Creates and connects the ok button
        ok_btn = QPushButton("Ok")
        ok_btn.set_default = True #Pressing enter pushes the ok button
        ok_btn.clicked.connect(self.accept) #Ends the dialog box once button is pushed
        
        #Adds the widgets to the v box layout
        layout.add_widget(status_lbl)
        layout.add_widget(ok_btn, alignment=Qt.AlignCenter)
        
        self.set_layout(layout)


main = MyWindow()
main.show()
sys.exit(app.exec())

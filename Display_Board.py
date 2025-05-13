'''Uses a string to generate and display an image and video based off of the emotion passed. Uses a scroll
bar for enhanced readability
Worked on by: Jacob Banducci and Joshua Sumagong
5/12/2025'''

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, 
                               QGroupBox, QDialog, QLineEdit, QLayout, QScrollArea)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property
from get_images import search_images
from io import BytesIO
import os
import string


class MainWindow(QWidget):
    def __init__(self, emotion):
        super().__init__()
        img_label = QLabel() #Creates a label object to hold an image
        
        #Cleans up the string for emotion
        emotion = emotion.strip() #Removes leading/trailing whitespace
        
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
        pil_img = search_images(emotion)

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

        #CREATES AN IMAGE FOR TESTING DELETE LATER
        #---------------------------------------------------------------------------------------------
        mood_board_label = QLabel()
        pixmap = QPixmap("mood_board.png").scaled(1000, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        mood_board_label.pixmap = pixmap
        mood_board_label.alignment = Qt.AlignCenter
        #-----------------------------------------------------------------------------------------------
        
        #Creates a vbox to store the image label and related widgets
        img_vbox = QVBoxLayout()
        img_vbox.set_alignment(Qt.AlignTop)

        save_lable = QLabel("Push the button to save the mood board")
        save_lable.alignment = Qt.AlignCenter

        #Creates a save button and connects it to the save image method
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_image)
        save_btn.set_fixed_width(200)

        #Adds the widgets to the vbox for the image
        img_vbox.add_widget(img_label)
        img_vbox.add_widget(save_lable, alignment=Qt.AlignCenter)
        img_vbox.add_widget(save_btn, alignment=Qt.AlignCenter)
        
        #Creates a main display vbox and adds the img_vbox to it
        main_display_vbox = QVBoxLayout()
        main_display_vbox.add_layout(img_vbox)
        
        #Creates a vbox for the video display
        vid_vbox = QVBoxLayout()
        vid_vbox.add_widget(mood_board_label) #FOR TESTING DELETE LATER
        
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

        self.set_layout(main_layout)
        self.window_title = "Media Display"
    
    
    @Slot()
    def save_image(self): 
        dialog = SaveDialog(self.pil_img) #Passes the image object to the new window
        dialog.exec()

    #Add code for method for downloading the video

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

def main():
    app = QApplication(sys.argv)
    main = MainWindow('anxious')
    main.show_maximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

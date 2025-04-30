import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, 
                               QGroupBox, QDialog, QLineEdit, QLayout)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property
from get_images import search_images
from io import BytesIO
import os

'''Look into qstacked widget'''
image_search_term = 'anxious'

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        img_label = QLabel() #Creates a label object to hold an image
        
        #Calls the image search function
        pil_img = search_images(image_search_term)
        self.pil_img = pil_img
        
        if pil_img:
            #Converts PIL image to QPixmap
            buffer = BytesIO()
            pil_img.save(buffer, format='PNG') #Saves image to the buffer
            qimage = QImage.from_data(buffer.getvalue())
            pixmap = QPixmap.from_image(qimage)
            
            pixmap = pixmap.scaled(1000, 600) #Sets the scale for the image label
            
            img_label.pixmap = pixmap
        
        #Creates a vbox to store the image label and related widgets
        img_vbox = QVBoxLayout()
        
        save_lable = QLabel("Push the button to save the mood board")
        save_lable.alignment = Qt.AlignCenter #Aligns the label to the center
        
        
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_image) #Connects the button to the save image fuction
        save_btn.set_fixed_width(200)
        

        img_vbox.add_widget(img_label)
        img_vbox.add_widget(save_lable)
        img_vbox.add_widget(save_btn, alignment=Qt.AlignCenter)

        #ADD CODE FOR DISPLAYING THE VIDEO

        self.set_layout(img_vbox)
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
        layout.add_widget(QLabel("Leave file name blank for defualt (add .png)"))
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
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, 
                               QGroupBox, QDialog, QLineEdit)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property
from get_images import search_images
from io import BytesIO
import os

'''Look into qstacked widget'''
image_search_term = 'angry'

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
        dialog = save_dialog(self.pil_img)
        dialog.exec()

    #Add code for method for downloading the video

class save_dialog(QDialog):
    def __init__(self, image):
        super().__init__()
        self.window_title = "Save Mood Board"
        self.image = image
        
        layout = QVBoxLayout()
        
        self.name_input = QLineEdit("Enter file name (e.g., my_mood_board.png)")

        
        self.path_input = QLineEdit("Enter save folder path (leave blank for default)")
        
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_image)
        
        layout.add_widget(QLabel("File Name:"))
        layout.add_widget(self.name_input)
        layout.add_widget(QLabel("Save Location:"))
        layout.add_widget(self.path_input)
        layout.add_widget(self.save_button)
        
        self.set_layout(layout)

    def save_image(self):
        filename = self.name_input.text.strip()
        folder = self.path_input.text.strip()
        
        if not filename:
            filename = "mood_board.png"
        
        if not folder:
            folder = os.getcwd() #Selects the current working directory
        
        save_path = os.path.join(folder, filename)
        
        try:
            self.image.save(save_path)
            print("Image saved successfully")
        except Exception as e:
            print(f'Error saving image: {e}')
        
        self.accept()

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

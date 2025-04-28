import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QGroupBox)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property
from get_images import search_images
from io import BytesIO

'''Look into qstacked widget'''
image_search_term = 'sad'

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        img_label = QLabel() #Creates a label object to hold an image
        
        #Calls the image search function
        pil_img = search_images(image_search_term)
        
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
        save_lable = QLabel("Push the button to save the mood board") #ADD CODE TO CENTER THE LABEL AND MAKE IT BIGGER
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_image) #Connects the button to the save image fuction

        img_vbox.add_widget(img_label)
        img_vbox.add_widget(save_lable)
        img_vbox.add_widget(save_btn) #NEED TO ADD CODE FOR THE SAVE BUTTON

        #ADD CODE FOR DISPLAYING THE VIDEO

        self.set_layout(img_vbox)
        self.window_title = "Media Display"
    
    '''May want to make this open a new small window that allows the user to enter the name of the
    image to be saved. Can also try to have it so that the user can enter the path for the image or type
    default for it to save in the same folder as the code (this can also be implemented with the video too)'''
    @Slot()
    def save_image(self): 
        pass

    #Add code for method for downloading the video

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

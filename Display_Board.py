import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property
from get_images import search_images
from io import BytesIO

image_search_term = 'Happy'

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
            
            pixmap = pixmap.scaled(500, 500)
            
            img_label.pixmap = pixmap
        
        
        self.layout = QVBoxLayout()
        self.layout.add_widget(img_label)
        self.set_layout(self.layout)

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

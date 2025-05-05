import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,
    QGroupBox, QDialog, QLineEdit, QLayout
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, Slot
from get_images import search_images
from io import BytesIO
import os

image_search_term = 'anxious'

class MainWindowCopy(QWidget):
    def __init__(self, emotion):
        super().__init__()
        self.setWindowTitle("Media Display")

        img_label = QLabel()

        pil_img = search_images(emotion)
        self.pil_img = pil_img

        if pil_img:
            buffer = BytesIO()
            pil_img.save(buffer, format='PNG')
            qimage = QImage.fromData(buffer.getvalue())
            pixmap = QPixmap.fromImage(qimage)
            pixmap = pixmap.scaled(1000, 600, Qt.KeepAspectRatio)
            img_label.setPixmap(pixmap)

        img_vbox = QVBoxLayout()

        save_label = QLabel("Push the button to save the mood board")
        save_label.setAlignment(Qt.AlignCenter)

        save_btn = QPushButton("Save")
        save_btn.setFixedWidth(200)
        save_btn.clicked.connect(self.save_image)

        img_vbox.addWidget(img_label)
        img_vbox.addWidget(save_label)
        img_vbox.addWidget(save_btn, alignment=Qt.AlignCenter)

        self.setLayout(img_vbox)

    @Slot()
    def save_image(self):
        dialog = SaveDialogCopy(self.pil_img)
        dialog.exec()


class SaveDialogCopy(QDialog):
    def __init__(self, image):
        super().__init__()
        self.setWindowTitle("Save Mood Board")
        self.image = image

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.path_input = QLineEdit()

        self.save_button = QPushButton("Save")
        self.save_button.setDefault(True)
        self.save_button.clicked.connect(self.save_image)

        layout.addWidget(QLabel("File Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Leave file name blank for default (add .png)"))
        layout.addWidget(QLabel())
        layout.addWidget(QLabel("Save Location:"))
        layout.addWidget(self.path_input)
        layout.addWidget(QLabel("Leave file path blank for default"))
        layout.addWidget(self.save_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.resize(200, 200)

    @Slot()
    def save_image(self):
        filename = self.name_input.text().strip()
        folder = self.path_input.text().strip()

        if not filename:
            filename = "mood_board.png"

        if not folder:
            folder = os.getcwd()

        save_path = os.path.join(folder, filename)

        try:
            self.image.save(save_path)
            status_dialog = StatusDialogCopy("Image saved successfully")
            status_dialog.exec()
        except Exception as e:
            status_dialog = StatusDialogCopy(f"Error saving image: {e}")
            status_dialog.exec()
        finally:
            self.accept()


class StatusDialogCopy(QDialog):
    def __init__(self, status_text):
        super().__init__()
        self.setWindowTitle("Save Status")

        layout = QVBoxLayout()
        layout.setSizeConstraint(QLayout.SetFixedSize)

        status_lbl = QLabel(status_text)
        status_lbl.setAlignment(Qt.AlignCenter)

        ok_btn = QPushButton("Ok")
        ok_btn.setDefault(True)
        ok_btn.clicked.connect(self.accept)

        layout.addWidget(status_lbl)
        layout.addWidget(ok_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindowCopy("happy")  # Replace with desired emotion
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
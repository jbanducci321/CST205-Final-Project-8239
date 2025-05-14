from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout,
    QPushButton, QComboBox, QGroupBox, QDialog, QLineEdit, QLayout
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt, Slot
import sys
import os
#Fallback incase it doesn't display the video on some systems.

if "QTWEBENGINE_CHROMIUM_FLAGS" not in os.environ:
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu"


from get_vid import search_youtube_videos
from dl_yt import download_video, download_audio


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.results = search_youtube_videos("happy video")
        
        html = f'''
        <html>
          <body>
            <iframe width="50%" height="50%"
              src="https://www.youtube.com/embed/{self.results[0]}"
              frameborder="0"
              allowfullscreen>
            </iframe>
          </body>
        </html>
        '''

        self.browser.setHtml(html)

          # Create the download button
        download_button = QPushButton("Download")
        download_button.clicked.connect(self.dl_window)

        # Combine button and browser in layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(download_button, alignment=Qt.AlignCenter)
        central_widget.setLayout(layout)


        self.setCentralWidget(central_widget)
        self.setWindowTitle("YouTube Video Embed")
        self.resize(800, 600)

    @Slot()
    def dl_window(self):
        dialog = SaveVideoWindow(self.results[1])
        dialog.exec()


class SaveVideoWindow(QDialog):
    def __init__(self, vid_url):
        super().__init__()
        self.setWindowTitle("Save Video")
        self.vid_url = vid_url

        layout = QVBoxLayout()

        self.combo_box = QComboBox()
        self.combo_box.addItems(['Download Video', 'Download Audio'])

        self.save_button = QPushButton("Save")
        self.save_button.setDefault(True)
        self.save_button.clicked.connect(self.dl_vid)

        layout.addWidget(self.combo_box, alignment=Qt.AlignCenter)
        layout.addWidget(self.save_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.resize(200, 200)

    @Slot()
    def dl_vid(self):
        choice = self.combo_box.currentText()

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
        self.setWindowTitle("Save Status")

        layout = QVBoxLayout()
        layout.setSizeConstraint(QLayout.SetFixedSize)

        status_lbl = QLabel(status_text)
        status_lbl.setAlignment(Qt.AlignCenter)

        ok_btn = QPushButton("OK")
        ok_btn.setDefault(True)
        ok_btn.clicked.connect(self.accept)

        layout.addWidget(status_lbl)
        layout.addWidget(ok_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

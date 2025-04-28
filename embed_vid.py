from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
import sys
from get_vid import search_youtube_videos

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create a WebEngineView
        self.browser = QWebEngineView()
        
        results = search_youtube_videos("happy video")

        # Embed YouTube video using iframe HTML
        html = f'''
        <html>
          <body>
            <iframe width="50%" height="50%" 
              src="https://www.youtube.com/embed/{results[1]}" 
              frameborder="0" 
              allowfullscreen>
            </iframe>
          </body>
        </html>
        '''
        
        # Set HTML content
        self.browser.setHtml(html)
        
        self.setCentralWidget(self.browser)
        self.setWindowTitle("YouTube Video Embed")
        self.resize(800, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

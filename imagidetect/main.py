import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap

from config.config import MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT, FILE_DIALOG_FILTER

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # ...
        self.setMinimumSize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout(self.centralWidget)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.open_button = QPushButton('Open File', self)
        self.open_button.clicked.connect(self.open_file)
        self.layout.addWidget(self.open_button)

    def open_file(self):
        file_dialog = QFileDialog()

        file_path, _ = file_dialog.getOpenFileName(
            self, 'Open File', '', FILE_DIALOG_FILTER)
        
        if file_path:
            self.show_preview(file_path)

    def show_preview(self, file_path):
        pixmap = QPixmap(file_path)
        self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

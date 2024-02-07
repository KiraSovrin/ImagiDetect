
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (   QAction, QMainWindow, QGridLayout, QListWidget, 
                                QWidget, QVBoxLayout, QPushButton, QFileDialog, 
                                QLabel, QLineEdit )
from PyQt5.QtGui import (QPixmap, QIcon)
from pathlib import Path
import config.config as config


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # main window config
        self.setMinimumSize(config.MIN_WINDOW_WIDTH, config.MIN_WINDOW_HEIGHT)
        self.setWindowTitle(config.TITLE)
        self.setWindowIcon(QIcon('../assets/img/elf.png'))

        # layout
        # grid = QGridLayout(self)
        # # self.setLayout(grid)

        # self.list_widget = QListWidget(self)
        # grid.addWidget(self.list_widget, 0, 0, 4, 1)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # self.layout = QVBoxLayout(self.centralWidget)
        self.layout = QGridLayout(self.centralWidget)
        self.paths = QLineEdit()
        # self.image_label = QLabel(self)
        # self.layout.addWidget(self.image_label)

        # buttons
        # self.open_button = QPushButton('Open File', self)
        # self.open_button.clicked.connect(self.open_file)
        # self.layout.addWidget(self.open_button)

        add_btn = QPushButton('Add Path')
        add_btn.clicked.connect(self.add_path)

        remove_btn = QPushButton('Remove')
        remove_btn.clicked.connect(self.remove)

        clear_btn = QPushButton('Clear')
        clear_btn.clicked.connect(self.clear)

        self.layout.addWidget(QLabel('Directory:'), 1, 0)
        self.layout.addWidget(self.paths, 1, 0)
        self.layout.addWidget(add_btn, 0, 1, alignment=config.LEFT_ALIGN)
        self.layout.addWidget(remove_btn, 1, 1, alignment=config.LEFT_ALIGN)
        self.layout.addWidget(clear_btn, 2, 1, alignment=config.LEFT_ALIGN)

        # self.show()

        # menu bar
        self.menu_bar = self.menuBar() 

        file_menu = self.menu_bar.addMenu('&File')
        open_menu = self.menu_bar.addMenu('&Open')
        help_menu = self.menu_bar.addMenu('&Help')

        # open menu item
        open_action = QAction(QIcon('./assets/img/folder_open.png'), '&Open', self)
        open_action.triggered.connect(self.open_file)
        open_action.setStatusTip('Open Folder...')
        open_action.setShortcut('Ctrl+O')
        open_menu.addAction(open_action)

    def add_path(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Open Directory")
        if dir_name:
            path = Path(dir_name)
            self.paths.setText(str(path)) 

    def remove(self):
        pass

    def clear(self):
        self.list_widget.clear()

    def open_file(self):
        file_dialog = QFileDialog()

        file_path, _ = file_dialog.getOpenFileName(
            self, 'Open File', None, config.FILE_DIALOG_FILTER)

        if file_path:
            self.show_preview(file_path)

    def show_preview(self, file_path):
        pixmap = QPixmap(file_path)
        self.image_label.setPixmap(pixmap)

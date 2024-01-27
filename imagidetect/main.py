# import os
# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk


# def search_images(folder_path):
#     image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

#     image_files = []
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             _, extension = os.path.splitext(file)
#             if extension.lower() in image_extensions:
#                 image_files.append(os.path.join(root, file))

#     return image_files


# def browse_folder(result_text):
#     folder_path = filedialog.askdirectory()
#     if folder_path:
#         image_files = search_images(folder_path)
#         result_text.delete(1.0, tk.END)  # Clear previous results

#         if image_files:
#             result_text.insert(tk.END, "Found the following image files:\n")
#             for file in image_files:
#                 result_text.insert(tk.END, f"{file}\n")
#         else:
#             result_text.insert(
#                 tk.END, "No image files found in the selected folder.")

# def show_images(images):
#     image_index = 0

#     def show_image():
#         nonlocal image_index
#         if image_files:
#             image_path = image_files[image_index]
#             img = Image.open(image_path)
#             img.thumbnail((300, 300))  # Adjust size if needed
#             tk_img = ImageTk.PhotoImage(img)

#             image_canvas.config(image=tk_img)
#             image_canvas.image = tk_img

#             info_text.delete(1.0, tk.END)
#             info_text.insert(tk.END, f"Name: {os.path.basename(image_path)}\n")
#             info_text.insert(tk.END, f"Path: {image_path}\n")
#             info_text.insert(
#                 tk.END, f"Created: {os.path.getctime(image_path)}")

#     def next_image():
#         nonlocal image_index
#         if image_files:
#             image_index = (image_index + 1) % len(image_files)
#             show_image()

#     def prev_image():
#         nonlocal image_index
#         if image_files:
#             image_index = (image_index - 1) % len(image_files)
#             show_image()

#     show_image()

#     next_button = tk.Button(root, text="Next", command=next_image)
#     next_button.pack(side=tk.RIGHT, padx=10)

#     prev_button = tk.Button(root, text="Previous", command=prev_image)
#     prev_button.pack(side=tk.LEFT, padx=10)

# def load_header():
#     header.pack_propagate(False)
#     # frame widgets
#     logo_img = ImageTk.PhotoImage(file="img/cat.png")
#     # logo_img.width(10)
#     logo_widget = tk.Label(header, image=logo_img, bg=BG_COLLOR)
#     logo_widget.image = logo_img
#     logo_widget.pack(anchor="nw")


# def load_body():
#     # body.pack_propagate(False)
#     label = tk.Label(body, text="Select a folder:",
#                         bg=BG_COLLOR, font=("TkMenuFont", 18))

#     label.pack(pady=10)
#     result_text = None
#     browse_button = tk.Button(body, text="Browse", command=browse_folder(result_text),
#                             font=("TkMenuFont", 18), 
#                             bg=BG_BTN_COLOR, 
#                             cursor="hand2", 
#                             activebackground="#badee2", 
#                             activeforeground="black",
#                             width=50)
#     browse_button.pack(pady=5)

#     result_text = tk.Text(body, height=5, width=50)
#     result_text.pack(pady=10)

# # Create the main window
# BG_COLLOR = "#424142"
# BG_BTN_COLOR = "#c9b530"
# root = tk.Tk()
# root.title("Image Search Application")
# root.geometry("1024x720")

# # Create and configure widgets
# header = tk.Frame(root, width=1024, height=200, bg=BG_COLLOR)
# body = tk.Frame(root, width=1024, bg=BG_COLLOR)
# header.grid(row=0, column=0)
# body.grid(row=1, column=0)

# # for frame in (header, body):
# #     frame.grid(row=0, column=0)






# # image_canvas = tk.Label(header)
# # image_canvas.pack(pady=10)

# # info_text = tk.Text(header, height=5, width=50)
# # info_text.pack(pady=10)

# # Start the Tkinter event loop
# load_header()
# load_body()
# root.mainloop()

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap

# sys.path.append('D:\\dev\\ImagiDetect\\config')
# print(sys.path)

# sys.path.append('D:/dev/ImagiDetect')  # Add the root directory to sys.path
from config.config import MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT, FILE_DIALOG_FILTER

# import config.config as config
# from ..config.config import *

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

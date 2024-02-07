import sys
from pathlib import Path
from core.main_window import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path(f'{sys.path[0]}/assets/qss/style.qss').read_text())
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

import sys
from PySide6.QtWidgets import QApplication
from window.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
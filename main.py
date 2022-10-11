# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

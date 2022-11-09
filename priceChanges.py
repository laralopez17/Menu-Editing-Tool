from ui_form import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QMainWindow

class priceChanges(QMainWindow):
    def __init__(self, parent=QMainWindow):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.pricePage)
        self.ui.stackedWidget.show()

#sets the screen for working with PRICES
    def clickedPRICEBUTTON(self):
        pass

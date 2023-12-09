import sys

from PyQt6.QtWidgets import QApplication
from window import PeriodicTable

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PeriodicTable()
    window.show() 

    sys.exit(app.exec())
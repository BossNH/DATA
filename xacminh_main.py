import sys
from PyQt6.QtWidgets import QApplication
from xacminh_Ext import XacMinhWindow


def main():
    app = QApplication(sys.argv)
    window = XacMinhWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

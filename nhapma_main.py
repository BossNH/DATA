import sys
from PyQt6.QtWidgets import QApplication
from nhap_ma_Ext import TheoDoiChienDichWindow


def main():
    app = QApplication(sys.argv)
    window = TheoDoiChienDichWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

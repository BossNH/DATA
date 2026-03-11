import sys

from PyQt6.QtWidgets import QApplication

from cd2_thanhcong_Ext import ThanhCongWindow


def main():
    app = QApplication(sys.argv)
    window = ThanhCongWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

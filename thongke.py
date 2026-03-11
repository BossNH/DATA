import os
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor, QFont, QPixmap, QCursor
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QFrame,
    QGraphicsDropShadowEffect, QComboBox, QLineEdit, QTableWidget,
    QTableWidgetItem, QHeaderView, QToolButton, QWidget
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def set_font(widget, size, weight=400, family="Segoe UI"):
    font = QFont(family, size)
    font.setWeight(weight)
    widget.setFont(font)


def add_shadow(widget, blur=18, x=0, y=3, color=QColor(120, 90, 110, 65)):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(blur)
    shadow.setOffset(x, y)
    shadow.setColor(color)
    widget.setGraphicsEffect(shadow)
    return shadow


def load_scaled_pixmap(path, w, h):
    full_path = os.path.join(BASE_DIR, path)
    if os.path.exists(full_path):
        pixmap = QPixmap(full_path)
        if not pixmap.isNull():
            return pixmap.scaled(
                w, h,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
    return None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(BASE_DIR, "thongke.ui"), self)
        self.setWindowTitle("Donarity - Công khai quyên góp")
        self.resize(960, 700)
        self.setMinimumSize(QSize(930, 680))

        self.pages = [
            [
                ["DN0180", "Lê Quốc Thảo", "CD0047", "890000", "2/2/2026", "01:44:31"],
                ["DN0153", "Lê Ngọc Trí", "CD0035", "200000", "1/31/2026", "14:12:44"],
                ["DN0153", "Lê Ngọc Trí", "CD0013", "50000", "1/18/2026", "01:49:04"],
                ["DN0153", "Lê Ngọc Trí", "CD0027", "50000", "1/16/2026", "07:11:13"],
                ["DN0163", "Bùi Thị Hạnh", "CD0041", "4680000", "1/3/2026", "13:47:57"],
                ["DN0154", "Đặng Minh Huyền", "CD0015", "100000", "12/27/2025", "08:31:51"],
                ["DN0194", "Võ Văn Kiên", "CD0046", "1250000", "12/22/2025", "10:33:58"],
                ["DN0199", "Phan Hoài Hà", "CD0027", "4100000", "12/21/2025", "17:27:01"],
                ["DN0153", "Lê Ngọc Trí", "CD0001", "500000", "11/18/2025", "00:34:01"],
            ],
            [
                ["DN0194", "Võ Văn Kiên", "CD0007", "90000", "11/10/2025", "00:57:47"],
                ["DN0152", "Lý Phương Thắng", "CD0005", "1000000", "11/16/2025", "23:12:55"],
                ["DN0184", "Hồ Hữu Toàn", "CD0048", "690000", "11/7/2025", "21:06:04"],
                ["DN0170", "Huỳnh Xuân Hà", "CD0010", "1290000", "10/24/2025", "13:49:54"],
                ["DN0199", "Phan Hoài Hà", "CD0019", "650000", "10/14/2025", "17:58:24"],
                ["DN0163", "Bùi Thị Hạnh", "CD0025", "920000", "10/12/2025", "18:31:12"],
                ["DN0196", "Bùi Hữu Phúc", "CD0007", "1800000", "9/27/2025", "01:41:14"],
                ["DN0194", "Võ Văn Kiên", "CD0034", "150000", "9/24/2025", "11:38:21"],
                ["DN0167", "Đặng Phương My", "CD0033", "430000", "9/12/2025", "19:08:20"],
            ],
            [
                ["DN0166", "Phạm Văn Nhi", "CD0006", "3240000", "9/3/2025", "09:47:54"],
                ["DN0174", "Dương Minh Hạnh", "CD0029", "2580000", "8/27/2025", "07:42:42"],
                ["DN0151", "Lê Hoài Trí", "CD0004", "1000000", "8/25/2025", "07:23:19"],
                ["DN0153", "Lê Ngọc Trí", "CD0016", "200000", "8/22/2025", "09:59:50"],
                ["DN0153", "Lê Ngọc Trí", "CD0012", "50000", "8/9/2025", "20:44:46"],
                ["DN0153", "Lê Ngọc Trí", "CD0002", "200000", "8/3/2025", "05:55:43"],
                ["DN0199", "Phan Hoài Hà", "CD0044", "180000", "7/28/2025", "07:13:03"],
                ["DN0186", "Phan Thành Thảo", "CD0046", "5000000", "7/4/2025", "07:26:51"],
                ["DN0177", "Ngô Văn Dũng", "CD0045", "1650000", "6/11/2025", "12:58:03"],
            ],
            [
                ["DN0152", "Lý Phương Thắng", "CD0002", "100000", "6/7/2025", "03:41:29"],
                ["DN0154", "Đặng Minh Huyền", "CD0007", "100000", "6/3/2025", "05:02:42"],
                ["DN0194", "Võ Văn Kiên", "CD0016", "780000", "6/3/2025", "17:55:57"],
                ["DN0186", "Phan Thành Thảo", "CD0034", "480000", "5/31/2025", "09:01:47"],
                ["DN0183", "Lý Hữu Long", "CD0029", "550000", "5/20/2025", "06:38:36"],
                ["DN0153", "Lê Ngọc Trí", "CD0015", "5000000", "5/18/2025", "15:44:42"],
                ["DN0155", "Huỳnh Kim Phúc", "CD0009", "10000000", "5/16/2025", "09:52:44"],
                ["DN0153", "Lê Ngọc Trí", "CD0032", "2000000", "5/5/2025", "02:56:11"],
                ["DN0152", "Lý Phương Thắng", "CD0040", "1000000", "5/1/2025", "18:46:20"],
            ],
            [
                ["DN0199", "Phan Hoài Hà", "CD0006", "8700000", "4/24/2025", "08:30:35"],
                ["DN0157", "Đặng Thị Thang", "CD0021", "500000", "4/11/2025", "18:18:30"],
                ["DN0172", "Ngô Thành Toàn", "CD0020", "2000000", "4/9/2025", "17:19:50"],
                ["DN0152", "Lý Phương Thắng", "CD0001", "200000", "4/1/2025", "03:10:21"],
                ["DN0170", "Huỳnh Xuân Hà", "CD0048", "3820000", "3/24/2025", "14:26:17"],
                ["DN0166", "Phạm Văn Nhi", "CD0028", "780000", "3/15/2025", "11:23:32"],
                ["DN0191", "Dương Minh Dũng", "CD0018", "420000", "3/9/2025", "19:47:13"],
                ["DN0155", "Huỳnh Kim Phúc", "CD00005", "50000", "3/3/2025", "00:29:22"],
                ["DN0175", "Võ Hồng Hương", "CD0004", "2890000", "3/2/2025", "21:42:37"],
            ],
        ]
        self.current_page = 1
        self._setup_ui()
        self.render_page()

    def _setup_ui(self):
        self._setup_fonts()
        self._setup_topnav_buttons()
        self._setup_filters()
        self._setup_cards()
        self._setup_table()
        self._setup_pagination()
        self.searchEdit.textChanged.connect(self.apply_filter)
        self.prevBtn.clicked.connect(self.prev_page)
        self.nextBtn.clicked.connect(self.next_page)

    def _setup_fonts(self):
        # Navbar
        set_font(self.logoLabel, 18, 900)
        set_font(self.brandLabel, 16, 900)
        set_font(self.subBrandLabel, 8, 500)

        self.brandLabel.setStyleSheet("color:#9C4F74;background:transparent;")
        self.subBrandLabel.setStyleSheet("color:#9D8A93;background:transparent;")
        self.logoLabel.setStyleSheet("background:transparent;color:#9C4F74;")

        # Badge
        set_font(self.badgeLabel, 8, 700)
        self.badgeLabel.setStyleSheet("""
            background:#E74C3C;
            color:white;
            border-radius:8px;
            padding:0px;
        """)

        # Page title
        set_font(self.pageTitle, 24, 900)
        self.pageTitle.setStyleSheet("color:#101010;background:transparent;")

        for name in ("dot1", "dot2"):
            lbl = getattr(self, name)
            set_font(lbl, 7, 700)

    def _apply_navbar_container_style(self):
        # Nếu trong file ui của bạn thanh trên là topBar thì đoạn này sẽ ăn style đúng thanh mới
        if hasattr(self, "topBar") and isinstance(self.topBar, QFrame):
            self.topBar.setStyleSheet("""
                QFrame#topBar {
                    background: #F5DCE6;
                    border: none;
                    border-radius: 18px;
                }
            """)
            add_shadow(self.topBar, blur=10, y=2, color=QColor(120, 85, 105, 30))

    def _style_icon_button(self, btn, font_size=16):
        set_font(btn, font_size, 700)
        btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn.setFixedSize(36, 36)
        btn.setStyleSheet("""
            QPushButton, QToolButton {
                background: transparent;
                border: none;
                border-radius: 18px;
                color: #2C2328;
                padding: 6px;
            }
            QPushButton:hover, QToolButton:hover {
                background: #EEC9D8;
            }
            QPushButton:pressed, QToolButton:pressed {
                background: #E2B5C7;
            }
        """)

    def _style_nav_button(self, btn, active=False):
        set_font(btn, 11, 600)
        btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn.setMinimumHeight(42)

        if active:
            btn.setStyleSheet("""
                QPushButton {
                    background: #C98AA5;
                    color: white;
                    border: none;
                    border-radius: 18px;
                    padding: 10px 18px;
                    font-weight: 700;
                    text-align: center;
                }
                QPushButton:hover {
                    background: #C98AA5;
                }
                QPushButton:pressed {
                    background: #B97895;
                }
            """)
        else:
            btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    color: #2C2328;
                    border: none;
                    border-radius: 18px;
                    padding: 10px 18px;
                    font-weight: 600;
                    text-align: center;
                }
                QPushButton:hover {
                    background: #EEC9D8;
                }
                QPushButton:pressed {
                    background: #E2B5C7;
                }
            """)

    def _setup_topnav_buttons(self):
        self._apply_navbar_container_style()

        # Đổi text đúng theo navbar mới
        self.logoLabel.setText("🕊")
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.brandLabel.setText("Donarity")
        self.subBrandLabel.setText("by group 10")

        self.homeBtn.setText("🏛 Trang chủ")
        self.createBtn.setText("🎞 Thống kê")
        self.followBtn.setText("📠 Chatbot")
        self.publicBtn.setText("👁 Công khai")

        self.bellBtn.setText("🔔")
        self.settingsBtn.setText("⚙")
        self.avatarBtn.setText("👤")
        self.badgeLabel.setText(" 0")

        # Style menu
        self.nav_buttons = [self.homeBtn, self.createBtn, self.followBtn, self.publicBtn]

        # Vì đây là trang "Công khai", nên active là publicBtn
        for btn in self.nav_buttons:
            self._style_nav_button(btn, btn is self.publicBtn)
            btn.clicked.connect(lambda _, b=btn: self.set_active_button(b))

        self._style_icon_button(self.bellBtn, 14)
        self._style_icon_button(self.settingsBtn, 14)
        self._style_icon_button(self.avatarBtn, 16)



    def _setup_filters(self):
        for combo, items, width in (
            (self.weekFilter, ["Tuần này", "Tháng này", "Năm nay"], 128),
            (self.fieldFilter, ["Tất cả lĩnh vực", "Giáo dục", "Y tế", "Cộng đồng"], 150),
        ):
            combo.clear()
            combo.addItems(items)
            combo.setFixedSize(width, 40)
            set_font(combo, 10, 700)
            combo.setStyleSheet("""
                QComboBox {
                    background: #fbfbfb;
                    border: 1px solid #d6d0d3;
                    border-radius: 8px;
                    padding: 0 12px;
                    color: #1f1f1f;
                }
                QComboBox:hover {
                    border: 1px solid #c8bac1;
                    background: #ffffff;
                }
                QComboBox:focus {
                    border: 1px solid #d998ba;
                }
                QComboBox::drop-down {
                    border: none;
                    width: 28px;
                }
                QComboBox QAbstractItemView {
                    background: white;
                    border: 1px solid #d6d0d3;
                    selection-background-color: #efc1d7;
                    selection-color: #1f1f1f;
                    outline: none;
                }
            """)

        self.exportBtn.setFixedSize(130, 40)
        set_font(self.exportBtn, 10, 800)
        self.exportBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.exportBtn.setStyleSheet("""
            QPushButton {
                background: #ef9dc7;
                color: #141414;
                border: none;
                border-radius: 8px;
                padding: 0 14px;
            }
            QPushButton:hover {
                background: #ea8ebc;
            }
            QPushButton:pressed {
                background: #df7dae;
            }
        """)
        add_shadow(self.exportBtn, blur=8, y=2, color=QColor(130, 95, 115, 40))

    def _setup_card(self, card: QFrame, icon_wrap: QLabel, title: QLabel, value: QLabel, image_name: str, fallback: str, icon_bg: str):
        card.setFixedHeight(118)
        card.setStyleSheet("""
            QFrame {
                background: #f7f6f7;
                border: 1px solid #d0cbce;
                border-radius: 14px;
            }
        """)
        add_shadow(card, blur=14, y=3, color=QColor(110, 95, 110, 45))
        icon_wrap.setStyleSheet(f"background:{icon_bg};border:none;border-radius:28px;")
        self._set_image(icon_wrap, image_name, fallback, 34, 34)
        set_font(title, 10, 400)
        title.setStyleSheet("color:#767276;background:transparent;")
        set_font(value, 18, 900)
        value.setStyleSheet("color:#111;background:transparent;")

    def _setup_cards(self):
        self._setup_card(self.card1, self.card1IconWrap, self.card1Title, self.card1Value, "tongtien.png", "$", "#fdebf4")
        self._setup_card(self.card2, self.card2IconWrap, self.card2Title, self.card2Value, "ungho.png", "◎", "#edf3fb")
        self._setup_card(self.card3, self.card3IconWrap, self.card3Title, self.card3Value, "chiendich.png", "♡", "#fdf0f7")

    def _setup_table(self):
        self.tablePanel.setStyleSheet("""
            QFrame#tablePanel {
                background: #ead4e1;
                border: 1px solid #d7b8c9;
                border-radius: 8px;
            }
        """)
        add_shadow(self.tablePanel, blur=14, y=3, color=QColor(125, 95, 115, 45))

        self.searchEdit.setFixedHeight(38)
        set_font(self.searchEdit, 10, 500)
        self.searchEdit.setStyleSheet("""
            QLineEdit {
                background: #ef9bc4;
                color: #3a3a3a;
                border: 1px solid #d47eaa;
                border-radius: 6px;
                padding: 0 12px;
            }
            QLineEdit:hover {
                background: #ee95c0;
            }
            QLineEdit:focus {
                background: #f19ec7;
                border: 1px solid #b85d8d;
            }
        """)
        add_shadow(self.searchEdit, blur=10, y=2, color=QColor(120, 85, 105, 35))

        table = self.donationTable
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["ID", "Tên", "Campaign ID", "Số tiền donate", "Ngày", "Giờ"])
        table.verticalHeader().setVisible(False)
        table.setShowGrid(True)
        table.setAlternatingRowColors(True)
        table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        table.setFrameShape(QFrame.Shape.NoFrame)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        table.setStyleSheet("""
            QTableWidget {
                background: #ead4e1;
                alternate-background-color: #e6cfdb;
                gridline-color: #d3c8cf;
                color: #282828;
                border: none;
            }
            QHeaderView::section {
                background: #f1efef;
                color: #202020;
                border: 1px solid #d9d5d7;
                padding: 7px 10px;
                font-weight: 700;
            }
            QTableWidget::item {
                padding: 10px;
                border: none;
            }
            QTableWidget::item:selected {
                background: #e8bdd2;
                color: #202020;
            }
        """)
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setMinimumHeight(42)
        table.verticalHeader().setDefaultSectionSize(40)

    def _setup_pagination(self):
        for btn in (self.prevBtn, self.nextBtn):
            btn.setFixedSize(20, 20)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            set_font(btn, 10, 900)
            btn.setStyleSheet("""
                QPushButton {
                    background:#fffdfd;
                    color:#222;
                    border:1px solid #ddd8db;
                    border-radius: 3px;
                    padding:0;
                }
                QPushButton:hover {
                    background:#f3e8ee;
                }
                QPushButton:pressed {
                    background:#ead5e1;
                }
                QPushButton:disabled {
                    color:#999;
                    background:#fafafa;
                }
            """)
        set_font(self.pageLabel, 11, 500)
        self.pageLabel.setStyleSheet("background:transparent;color:#232323;")
        self._set_dot(self.dot1, True)
        self._set_dot(self.dot2, False)

    def _set_dot(self, lbl: QLabel, active: bool):
        lbl.setStyleSheet("color:#111;background:transparent;" if active else "color:#c7b1bd;background:transparent;")

    def _set_image(self, label: QLabel, image_name: str, fallback_text: str, w=None, h=None):
        tw = w or max(label.width(), 32)
        th = h or max(label.height(), 32)
        pix = load_scaled_pixmap(image_name, tw, th)
        if pix:
            label.setPixmap(pix)
            label.setText("")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            label.setPixmap(QPixmap())
            label.setText(fallback_text)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            set_font(label, 18, 900)

    def set_active_button(self, active_btn):
        for btn in self.nav_buttons:
            self._style_nav_button(btn, btn is active_btn)

    def load_rows(self, rows):
        self.donationTable.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
                self.donationTable.setItem(r, c, item)

    def render_page(self):
        rows = self.pages[self.current_page - 1]
        self.load_rows(rows)
        self.pageLabel.setText(str(self.current_page))
        self.prevBtn.setEnabled(self.current_page > 1)
        self.nextBtn.setEnabled(self.current_page < len(self.pages))
        self._set_dot(self.dot1, True)
        self._set_dot(self.dot2, False)

    def apply_filter(self):
        keyword = self.searchEdit.text().strip().lower()
        base_rows = self.pages[self.current_page - 1]
        if not keyword:
            filtered = base_rows
        else:
            filtered = [row for row in base_rows if keyword in " ".join(map(str, row)).lower()]
        self.load_rows(filtered)

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.searchEdit.clear()
            self.render_page()

    def next_page(self):
        if self.current_page < len(self.pages):
            self.current_page += 1
            self.searchEdit.clear()
            self.render_page()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
























import os
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor, QFont, QPixmap
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QFrame,
    QHBoxLayout, QVBoxLayout, QGraphicsDropShadowEffect, QComboBox,
    QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView
)


# =========================
# Helpers
# =========================
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


# =========================
# Small Reusable Widgets
# =========================
class ImageLabel(QLabel):
    def __init__(self, image_path="", width=40, height=40, fallback_text=""):
        super().__init__()
        self.setFixedSize(width, height)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("background: transparent;")
        self.set_image(image_path, fallback_text)

    def set_image(self, image_path, fallback_text=""):
        pix = load_scaled_pixmap(image_path, self.width(), self.height())
        if pix:
            self.setPixmap(pix)
            self.setText("")
        else:
            self.setPixmap(QPixmap())
            self.setText(fallback_text)


class IconActionButton(QPushButton):
    def __init__(self, text, tooltip=""):
        super().__init__(text)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedSize(32, 32)
        self.setToolTip(tooltip)
        set_font(self, 14, 700)
        self.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                border-radius: 16px;
                color: #25272d;
            }
            QPushButton:hover {
                background: rgba(190, 130, 165, 0.16);
            }
            QPushButton:pressed {
                background: rgba(190, 130, 165, 0.26);
            }
        """)


class NavButton(QPushButton):
    def __init__(self, text, active=False):
        super().__init__(text)
        self.active = active
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedHeight(36)
        set_font(self, 11, 700)
        self.update_style()

    def set_active(self, active):
        self.active = active
        self.update_style()

    def update_style(self):
        if self.active:
            self.setStyleSheet("""
                QPushButton {
                    background: #dca9cd;
                    color: #23262c;
                    border: none;
                    border-radius: 18px;
                    padding: 0 16px;
                }
                QPushButton:hover {
                    background: #d49bc1;
                }
                QPushButton:pressed {
                    background: #ca8db2;
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    color: #2a2d33;
                    border: none;
                    border-radius: 18px;
                    padding: 0 14px;
                }
                QPushButton:hover {
                    background: rgba(214, 161, 200, 0.16);
                }
                QPushButton:pressed {
                    background: rgba(214, 161, 200, 0.26);
                }
            """)


class FilterCombo(QComboBox):
    def __init__(self, items, width=130):
        super().__init__()
        self.addItems(items)
        self.setFixedSize(width, 40)
        set_font(self, 10, 700)
        self.setStyleSheet("""
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


class ExportButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(130, 40)
        set_font(self, 10, 800)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
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
        add_shadow(self, blur=8, y=2, color=QColor(130, 95, 115, 40))


class SearchBox(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Tìm kiếm")
        self.setFixedHeight(38)
        set_font(self, 10, 500)
        self.setStyleSheet("""
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
        add_shadow(self, blur=10, y=2, color=QColor(120, 85, 105, 35))


class PageDot(QLabel):
    def __init__(self, active=False):
        super().__init__("●")
        set_font(self, 7, 700)
        self.set_active(active)

    def set_active(self, active):
        self.setStyleSheet(
            "color:#111; background:transparent;" if active
            else "color:#c7b1bd; background:transparent;"
        )


class PaginationButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(20, 20)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        set_font(self, 10, 900)
        self.setStyleSheet("""
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


# =========================
# Top Navigation
# =========================
class TopNav(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFixedHeight(54)
        self.setStyleSheet("""
            background: #FFE3EA;
            border: none;
        """)

        root = QHBoxLayout(self)
        root.setContentsMargins(18, 0, 16, 0)
        root.setSpacing(10)

        # left
        left = QWidget()
        left.setStyleSheet("background: transparent;")
        left_l = QHBoxLayout(left)
        left_l.setContentsMargins(0, 0, 0, 0)
        left_l.setSpacing(8)

        logo = ImageLabel("logo_bocau.png", 42, 32, "🕊")
        set_font(logo, 20, 700)

        brand_wrap = QWidget()
        brand_wrap.setStyleSheet("background: transparent;")
        brand_l = QVBoxLayout(brand_wrap)
        brand_l.setContentsMargins(0, 0, 0, 0)
        brand_l.setSpacing(-1)

        brand = QLabel("Donarity")
        set_font(brand, 16, 900)
        brand.setStyleSheet("color:#7a3370; background:transparent;")

        sub = QLabel("by group 10")
        set_font(sub, 7, 400)
        sub.setStyleSheet("color:#856d79; background:transparent;")

        brand_l.addWidget(brand)
        brand_l.addWidget(sub)

        left_l.addWidget(logo)
        left_l.addWidget(brand_wrap)

        # center
        center = QWidget()
        center.setStyleSheet("background: transparent;")
        center_l = QHBoxLayout(center)
        center_l.setContentsMargins(0, 0, 0, 0)
        center_l.setSpacing(6)

        self.navs = [
            NavButton("⌂ Trang chủ"),
            NavButton("✚ Tạo chiến dịch"),
            NavButton("▉ Theo dõi chiến dịch", active=True),
            NavButton("◉ Công khai"),
        ]

        for btn in self.navs:
            btn.clicked.connect(lambda _, b=btn: self.set_active_button(b))
            center_l.addWidget(btn)

        # right
        right = QWidget()
        right.setStyleSheet("background: transparent;")
        right_l = QHBoxLayout(right)
        right_l.setContentsMargins(0, 0, 0, 0)
        right_l.setSpacing(8)

        bell = QWidget()
        bell.setFixedSize(30, 30)
        bell.setStyleSheet("background: transparent;")
        bell_layout = QHBoxLayout(bell)
        bell_layout.setContentsMargins(0, 0, 0, 0)
        bell_layout.setSpacing(0)

        bell_btn = IconActionButton("🔔", "Thông báo")
        bell_layout.addWidget(bell_btn)

        badge = QLabel("0", bell)
        badge.setGeometry(16, 0, 13, 13)
        set_font(badge, 7, 800)
        badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
        badge.setStyleSheet("""
            background:#e42633;
            color:white;
            border-radius:6px;
        """)

        settings = IconActionButton("⚙", "Cài đặt")
        avatar = IconActionButton("●", "Tài khoản")
        set_font(avatar, 18, 700)

        right_l.addWidget(bell)
        right_l.addWidget(settings)
        right_l.addWidget(avatar)

        root.addWidget(left, 0, Qt.AlignmentFlag.AlignLeft)
        root.addStretch(1)
        root.addWidget(center, 0, Qt.AlignmentFlag.AlignCenter)
        root.addStretch(1)
        root.addWidget(right, 0, Qt.AlignmentFlag.AlignRight)

    def set_active_button(self, active_btn):
        for btn in self.navs:
            btn.set_active(btn is active_btn)


# =========================
# Statistic Cards
# =========================
class StatCard(QFrame):
    def __init__(self, image_name, fallback_text, icon_bg, title, value):
        super().__init__()
        self.setFixedHeight(96)
        self.shadow = add_shadow(self, blur=14, y=3, color=QColor(110, 95, 110, 45))
        self.setStyleSheet("""
            QFrame {
                background: #f7f6f7;
                border: 1px solid #d0cbce;
                border-radius: 14px;
            }
        """)

        root = QHBoxLayout(self)
        root.setContentsMargins(14, 12, 16, 12)
        root.setSpacing(14)

        icon_wrap = QLabel()
        icon_wrap.setFixedSize(56, 56)
        icon_wrap.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_wrap.setStyleSheet(f"""
            background: {icon_bg};
            border: none;
            border-radius: 28px;
        """)

        icon = ImageLabel(image_name, 34, 34, fallback_text)
        set_font(icon, 18, 900)

        icon_holder = QVBoxLayout(icon_wrap)
        icon_holder.setContentsMargins(0, 0, 0, 0)
        icon_holder.addWidget(icon, 0, Qt.AlignmentFlag.AlignCenter)

        texts = QVBoxLayout()
        texts.setContentsMargins(0, 2, 0, 0)
        texts.setSpacing(2)

        title_lbl = QLabel(title)
        set_font(title_lbl, 10, 400)
        title_lbl.setStyleSheet("color:#767276; background:transparent;")

        value_lbl = QLabel(value)
        set_font(value_lbl, 18, 900)
        value_lbl.setStyleSheet("color:#111; background:transparent;")

        texts.addWidget(title_lbl)
        texts.addWidget(value_lbl)
        texts.addStretch()

        root.addWidget(icon_wrap)
        root.addLayout(texts, 1)

    def enterEvent(self, event):
        self.setStyleSheet("""
            QFrame {
                background: #ffffff;
                border: 1px solid #d8c7d1;
                border-radius: 14px;
            }
        """)
        if self.shadow:
            self.shadow.setBlurRadius(18)
            self.shadow.setOffset(0, 4)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet("""
            QFrame {
                background: #f7f6f7;
                border: 1px solid #d0cbce;
                border-radius: 14px;
            }
        """)
        if self.shadow:
            self.shadow.setBlurRadius(14)
            self.shadow.setOffset(0, 3)
        super().leaveEvent(event)


# =========================
# Table
# =========================
class DonationTable(QTableWidget):
    def __init__(self):
        super().__init__(0, 6)
        self.setHorizontalHeaderLabels(["ID", "Tên", "Campaign ID", "Số tiền donate", "Ngày", "Giờ"])
        self.verticalHeader().setVisible(False)
        self.setShowGrid(True)
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setStyleSheet("""
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
        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setMinimumHeight(42)
        self.verticalHeader().setDefaultSectionSize(40)

    def load_rows(self, rows):
        self.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
                self.setItem(r, c, item)


class TablePanel(QFrame):
    def __init__(self, pages):
        super().__init__()
        self.pages = pages
        self.current_page = 1

        self.setStyleSheet("""
            QFrame {
                background: #ead4e1;
                border: 1px solid #d7b8c9;
                border-radius: 8px;
            }
        """)
        add_shadow(self, blur=14, y=3, color=QColor(125, 95, 115, 45))

        root = QVBoxLayout(self)
        root.setContentsMargins(10, 12, 10, 10)
        root.setSpacing(12)

        self.search = SearchBox()
        self.search.textChanged.connect(self.apply_filter)
        root.addWidget(self.search)

        self.table = DonationTable()
        root.addWidget(self.table)

        footer = QWidget()
        footer.setStyleSheet("background: transparent;")
        footer_l = QHBoxLayout(footer)
        footer_l.setContentsMargins(0, 0, 0, 0)
        footer_l.setSpacing(12)

        footer_l.addStretch()

        self.prev_btn = PaginationButton("‹")
        self.prev_btn.clicked.connect(self.prev_page)

        self.page_label = QLabel("1")
        set_font(self.page_label, 11, 500)
        self.page_label.setStyleSheet("background:transparent; color:#232323;")

        self.next_btn = PaginationButton("›")
        self.next_btn.clicked.connect(self.next_page)

        self.dot1 = PageDot(True)
        self.dot2 = PageDot(False)

        footer_l.addWidget(self.prev_btn)
        footer_l.addWidget(self.page_label)
        footer_l.addWidget(self.next_btn)
        footer_l.addWidget(self.dot1)
        footer_l.addWidget(self.dot2)

        root.addWidget(footer)

        self.render_page()

    def render_page(self):
        rows = self.pages[self.current_page - 1]
        self.table.load_rows(rows)
        self.page_label.setText(str(self.current_page))
        self.prev_btn.setEnabled(self.current_page > 1)
        self.next_btn.setEnabled(self.current_page < len(self.pages))
        self.dot1.set_active(True)
        self.dot2.set_active(False)

    def apply_filter(self):
        keyword = self.search.text().strip().lower()
        base_rows = self.pages[self.current_page - 1]

        if not keyword:
            filtered = base_rows
        else:
            filtered = []
            for row in base_rows:
                joined = " ".join(map(str, row)).lower()
                if keyword in joined:
                    filtered.append(row)

        self.table.load_rows(filtered)

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.search.clear()
            self.render_page()

    def next_page(self):
        if self.current_page < len(self.pages):
            self.current_page += 1
            self.search.clear()
            self.render_page()


# =========================
# Main Window
# =========================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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

        central = QWidget()
        self.setCentralWidget(central)
        central.setStyleSheet("background:#f4ebf0;")

        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 8)
        root.setSpacing(0)

        root.addWidget(TopNav())

        body = QWidget()
        body.setStyleSheet("background:#f4ebf0;")
        body_l = QVBoxLayout(body)
        body_l.setContentsMargins(18, 12, 18, 10)
        body_l.setSpacing(14)

        top_row = QWidget()
        top_row.setStyleSheet("background: transparent;")
        top_row_l = QHBoxLayout(top_row)
        top_row_l.setContentsMargins(0, 0, 0, 0)
        top_row_l.setSpacing(10)

        title = QLabel("Công khai quyên góp")
        set_font(title, 24, 900)
        title.setStyleSheet("color:#101010; background:transparent;")

        top_row_l.addWidget(title)
        top_row_l.addStretch()

        self.week_filter = FilterCombo(["Tuần này", "Tháng này", "Năm nay"], 128)
        self.field_filter = FilterCombo(["Tất cả lĩnh vực", "Giáo dục", "Y tế", "Cộng đồng"], 150)
        self.export_btn = ExportButton("Xuất file   ⬇")

        top_row_l.addWidget(self.week_filter)
        top_row_l.addWidget(self.field_filter)
        top_row_l.addWidget(self.export_btn)

        body_l.addWidget(top_row)

        stat_row = QWidget()
        stat_row.setStyleSheet("background: transparent;")
        stat_l = QHBoxLayout(stat_row)
        stat_l.setContentsMargins(0, 0, 0, 0)
        stat_l.setSpacing(12)

        c1 = StatCard("tongtien.png", "$", "#fdebf4", "Tổng số tiền đã quyên góp", "479.822.000")
        c2 = StatCard("ungho.png", "◎", "#edf3fb", "Tổng số lượt ủng hộ", "287")
        c3 = StatCard("chiendich.png", "♡", "#fdf0f7", "Tổng số chiến dịch", "50")

        stat_l.addWidget(c1, 1)
        stat_l.addWidget(c2, 1)
        stat_l.addWidget(c3, 1)
        body_l.addWidget(stat_row)

        self.table_panel = TablePanel(self.pages)
        body_l.addWidget(self.table_panel, 1)

        root.addWidget(body)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
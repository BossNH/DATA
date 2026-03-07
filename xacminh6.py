
import sys
from dataclasses import dataclass

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLineEdit,
)


@dataclass
class CampaignData:
    title: str
    description: str
    raised: str
    target: str
    percent: str

    activities: str
    scope: str
    founded_date: str

    campaign_id: str
    gender: str
    full_name: str
    phone: str
    cccd: str
    address: str
    email: str

    qr_path: str
    avatar_path: str


class ImageLabel(QLabel):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.setFixedSize(width, height)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("background: transparent; border: none;")

    def set_image(self, path: str):
        pix = QPixmap(path)
        if pix.isNull():
            self.setText("Không tìm thấy ảnh")
            self.setStyleSheet("""
                QLabel {
                    color: #8a5c78;
                    border: 1px dashed #e7b3c9;
                    background: #fff7fb;
                    font-size: 14px;
                }
            """)
            return

        scaled = pix.scaled(
            self.width(),
            self.height(),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )
        self.setPixmap(scaled)


class DonationPage(QWidget):
    def __init__(self, data: CampaignData):
        super().__init__()
        self.data = data
        self.setWindowTitle("Donarity")
        self.resize(1000, 740)
        self.setMinimumSize(950, 700)
        self.setStyleSheet("""
            QWidget {
                background: #f8f0f4;
                color: #241f22;
                font-family: Arial, Helvetica, sans-serif;
            }
        """)
        self.build_ui()
        self.load_data(data)

    def build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(18, 12, 18, 14)
        root.setSpacing(10)

        # Header
        header = QFrame()
        header.setFixedHeight(48)
        header.setStyleSheet("""
            QFrame {
                background: #f5d6e1;
                border: none;
            }
        """)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(14, 6, 14, 6)
        header_layout.setSpacing(20)

        brand = QLabel("🕊️ Donarity")
        brand.setStyleSheet("""
            color: #8a3b74;
            font-size: 18px;
            font-weight: 800;
        """)
        header_layout.addWidget(brand)

        sub_brand = QLabel("by group 10")
        sub_brand.setStyleSheet("color: #8e7b87; font-size: 11px;")
        header_layout.addWidget(sub_brand)
        header_layout.addSpacing(14)

        self.home_btn = self._menu_button("🏠 Trang chủ", active=True)
        self.stats_btn = self._menu_button("⌛ Thống kê")
        self.chat_btn = self._menu_button("🗨️Chatbot")
        self.public_btn = self._menu_button("👁 Công khai")

        header_layout.addWidget(self.home_btn)
        header_layout.addWidget(self.stats_btn)
        header_layout.addWidget(self.chat_btn)
        header_layout.addWidget(self.public_btn)
        header_layout.addStretch()

        bell = QLabel("🔔")
        bell.setStyleSheet("font-size: 18px;")
        settings = QLabel("⚙️")
        settings.setStyleSheet("font-size: 17px;")
        user = QLabel("👤")
        user.setStyleSheet("font-size: 22px;")

        header_layout.addWidget(bell)
        header_layout.addWidget(settings)
        header_layout.addWidget(user)

        root.addWidget(header)

        # Back button
        back_row = QHBoxLayout()
        back_row.setContentsMargins(8, 2, 0, 0)

        self.back_btn = QPushButton("← Quay lại")
        self.back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.back_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                font-size: 15px;
                font-weight: 600;
                color: #201d1f;
                text-align: left;
                padding: 4px 0;
            }
            QPushButton:hover {
                color: #7d466e;
            }
        """)
        self.back_btn.clicked.connect(lambda: print("Quay lại"))
        back_row.addWidget(self.back_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        back_row.addStretch()
        root.addLayout(back_row)

        # Main card
        self.main_card = QFrame()
        self.main_card.setObjectName("mainCard")
        self.main_card.setStyleSheet("""
            QFrame#mainCard {
                background: #f8eef3;
                border: 3px solid #f0b9ca;
                border-radius: 22px;
            }
        """)
        main_layout = QVBoxLayout(self.main_card)
        main_layout.setContentsMargins(18, 16, 18, 16)
        main_layout.setSpacing(10)

        self.title_label = QLabel()
        self.title_label.setWordWrap(True)
        self.title_label.setStyleSheet("""
            font-size: 31px;
            font-weight: 800;
            color: #734465;
        """)
        main_layout.addWidget(self.title_label)

        self.desc_label = QLabel()
        self.desc_label.setWordWrap(True)
        self.desc_label.setStyleSheet("""
            font-size: 16px;
            color: #252025;
        """)
        main_layout.addWidget(self.desc_label)

        amount_row = QHBoxLayout()
        amount_row.setContentsMargins(24, 6, 10, 0)

        self.amount_label = QLabel()
        self.amount_label.setStyleSheet("""
            font-size: 27px;
            font-weight: 800;
            color: #724464;
        """)

        self.percent_label = QLabel()
        self.percent_label.setStyleSheet("""
            font-size: 27px;
            font-weight: 800;
            color: #724464;
        """)

        amount_row.addWidget(self.amount_label)
        amount_row.addStretch()
        amount_row.addWidget(self.percent_label)
        main_layout.addLayout(amount_row)

        self.progress_bg = QFrame()
        self.progress_bg.setFixedHeight(32)
        self.progress_bg.setStyleSheet("""
            QFrame {
                background: #efd7e2;
                border: none;
                border-radius: 16px;
            }
        """)
        progress_layout = QHBoxLayout(self.progress_bg)
        progress_layout.setContentsMargins(0, 0, 0, 0)
        progress_layout.setSpacing(0)

        self.progress_fill = QFrame()
        self.progress_fill.setStyleSheet("""
            QFrame {
                background: #eca5d1;
                border: none;
                border-radius: 16px;
            }
        """)
        self.progress_fill.setFixedWidth(280)

        progress_layout.addWidget(self.progress_fill, alignment=Qt.AlignmentFlag.AlignLeft)
        progress_layout.addStretch()

        progress_wrap = QHBoxLayout()
        progress_wrap.setContentsMargins(10, 0, 10, 0)
        progress_wrap.addWidget(self.progress_bg)
        main_layout.addLayout(progress_wrap)

        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setStyleSheet("color: #f0b9ca; background: #f0b9ca; min-height: 2px;")
        main_layout.addWidget(divider)

        lower_row = QHBoxLayout()
        lower_row.setSpacing(20)

        # Left block
        left_frame = QFrame()
        left_frame.setStyleSheet("QFrame { border: none; }")
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(4)

        left_layout.addWidget(self._section_title("Hoạt động:"))
        self.activities_label = QLabel()
        self.activities_label.setWordWrap(True)
        self.activities_label.setStyleSheet("font-size: 15px;")
        left_layout.addWidget(self.activities_label)

        left_layout.addSpacing(4)
        left_layout.addWidget(self._section_title("Phạm vi:"))
        self.scope_label = QLabel()
        self.scope_label.setStyleSheet("font-size: 15px;")
        left_layout.addWidget(self.scope_label)

        left_layout.addSpacing(4)
        left_layout.addWidget(self._section_title("Ngày thành lập:"))
        self.founded_label = QLabel()
        self.founded_label.setStyleSheet("font-size: 15px;")
        left_layout.addWidget(self.founded_label)
        left_layout.addStretch()

        separator = QFrame()
        separator.setFixedWidth(2)
        separator.setStyleSheet("background: #f0b9ca; border: none;")

        # Right block
        right_frame = QFrame()
        right_frame.setStyleSheet("QFrame { border: none; }")
        right_layout = QVBoxLayout(right_frame)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(4)

        right_layout.addWidget(self._section_title("Chủ chiến dịch:"))

        info_and_avatar = QHBoxLayout()
        info_and_avatar.setSpacing(16)

        grid = QGridLayout()
        grid.setHorizontalSpacing(12)
        grid.setVerticalSpacing(10)

        self.id_value = QLabel()
        self.gender_value = QLabel()
        self.name_value = QLabel()
        self.phone_value = QLabel()
        self.cccd_value = QLabel()
        self.address_value = QLabel()
        self.email_value = QLabel()

        labels = [
            ("ID:", self.id_value, "Giới tính:", self.gender_value),
            ("Họ và tên:", self.name_value, "", None),
            ("Số điện thoại:", self.phone_value, "", None),
            ("Số CCCD:", self.cccd_value, "", None),
            ("Địa chỉ:", self.address_value, "", None),
            ("Email:", self.email_value, "", None),
        ]

        row = 0
        for left_text, left_value, right_text, right_value in labels:
            left_label = QLabel(left_text)
            left_label.setStyleSheet("font-size: 15px;")
            left_value.setStyleSheet("font-size: 15px;")
            grid.addWidget(left_label, row, 0)
            grid.addWidget(left_value, row, 1)

            if right_value is not None:
                right_label = QLabel(right_text)
                right_label.setStyleSheet("font-size: 15px;")
                right_value.setStyleSheet("font-size: 15px;")
                grid.addWidget(right_label, row, 2)
                grid.addWidget(right_value, row, 3)
            row += 1

        info_and_avatar.addLayout(grid, 1)

        self.avatar_label = ImageLabel(132, 170)
        info_and_avatar.addWidget(self.avatar_label, alignment=Qt.AlignmentFlag.AlignTop)

        right_layout.addLayout(info_and_avatar)
        right_layout.addStretch()

        lower_row.addWidget(left_frame, 4)
        lower_row.addWidget(separator)
        lower_row.addWidget(right_frame, 5)

        main_layout.addLayout(lower_row)
        root.addWidget(self.main_card)

        # Donation card
        self.donation_card = QFrame()
        self.donation_card.setObjectName("donationCard")
        self.donation_card.setFixedWidth(390)
        self.donation_card.setStyleSheet("""
            QFrame#donationCard {
                background: #f8eef3;
                border: 3px solid #f0b9ca;
                border-radius: 22px;
            }
        """)

        donation_layout = QVBoxLayout(self.donation_card)
        donation_layout.setContentsMargins(30, 18, 24, 18)
        donation_layout.setSpacing(10)

        donation_title = QLabel("Quyên góp")
        donation_title.setStyleSheet("""
            font-size: 28px;
            font-weight: 800;
            color: #734465;
        """)
        donation_layout.addWidget(donation_title, alignment=Qt.AlignmentFlag.AlignHCenter)

        waiting_row = QHBoxLayout()
        waiting_row.setContentsMargins(18, 6, 0, 6)
        waiting_row.setSpacing(14)

        waiting_icon = QLabel("⏳")

        waiting_icon.setStyleSheet("font-size: 44px;")
        waiting_row.addWidget(waiting_icon, alignment=Qt.AlignmentFlag.AlignVCenter)

        waiting_text = QLabel("Đang xác minh...")
        waiting_text.setStyleSheet("font-size: 15px; color: #2c2328;")
        waiting_row.addWidget(waiting_text, alignment=Qt.AlignmentFlag.AlignVCenter)

        waiting_row.addStretch()
        donation_layout.addLayout(waiting_row)
        donation_layout.addStretch()

        root.addWidget(self.donation_card, alignment=Qt.AlignmentFlag.AlignLeft)
        root.addStretch()

    def _menu_button(self, text: str, active: bool = False) -> QPushButton:
        btn = QPushButton(text)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        if active:
            btn.setStyleSheet("""
                QPushButton {
                    background: #e7b9d2;
                    border: none;
                    border-radius: 18px;
                    padding: 8px 14px;
                    color: #241f22;
                    font-size: 15px;
                    font-weight: 700;
                }
            """)
        else:
            btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    border: none;
                    padding: 8px 10px;
                    color: #241f22;
                    font-size: 15px;
                    font-weight: 700;
                }
                QPushButton:hover {
                    color: #7d496d;
                }
            """)
        btn.clicked.connect(lambda _, t=text: print(f"Đã bấm: {t}"))
        return btn

    def _section_title(self, text: str) -> QLabel:
        label = QLabel(text)
        label.setStyleSheet("""
            font-size: 17px;
            font-weight: 800;
            color: #2d2428;
        """)
        return label

    def load_data(self, data: CampaignData):
        self.title_label.setText(data.title)
        self.desc_label.setText(data.description)

        self.amount_label.setText(
            f"<span style='color:#714565;font-weight:800;'>{data.raised}</span>"
            f"<span style='color:#8c6a84;font-weight:700;'>/{data.target}</span>"
        )
        self.amount_label.setTextFormat(Qt.TextFormat.RichText)
        self.percent_label.setText(data.percent)

        self.activities_label.setText(data.activities)
        self.scope_label.setText(data.scope)
        self.founded_label.setText(data.founded_date)

        self.id_value.setText(data.campaign_id)
        self.gender_value.setText(data.gender)
        self.name_value.setText(data.full_name)
        self.phone_value.setText(data.phone)
        self.cccd_value.setText(data.cccd)
        self.address_value.setText(data.address)
        self.email_value.setText(data.email)

        self.avatar_label.set_image(data.avatar_path)

        # Tính chiều rộng progress từ raised/target
        try:
            raised_value = float(data.raised.replace(",", ""))
            target_value = float(data.target.replace(",", ""))
            percent = max(0.0, min(1.0, raised_value / target_value if target_value else 0.0))
        except Exception:
            percent = 0.0

        total_width = self.progress_bg.width() if self.progress_bg.width() > 0 else 860
        fill_width = max(120, int(total_width * percent))
        self.progress_fill.setFixedWidth(fill_width)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # cập nhật lại thanh progress khi resize
        try:
            raised_text = self.data.raised
            target_text = self.data.target
            raised_value = float(raised_text.replace(",", ""))
            target_value = float(target_text.replace(",", ""))
            percent = max(0.0, min(1.0, raised_value / target_value if target_value else 0.0))
            total_width = max(300, self.progress_bg.width())
            fill_width = max(120, int(total_width * percent))
            self.progress_fill.setFixedWidth(fill_width)
        except Exception:
            pass

    def handle_submit(self):
        print("Đang xác minh...")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    page6 = CampaignData(
        title="Saigon Children's Charity (Học bổng giáo dục)",
        description="Giúp trẻ em có hoàn cảnh khó khăn tiếp cận giáo dục chất lượng để vượt qua nghèo đói và phát triển tương lai.",
        raised="1000000000",
        target="7000000000",
        percent="6.67%",
        activities="Trao học bổng dài hạn cho trẻ em nghèo\nXây dựng và cải tạo trường học\nĐào tạo nghề cho thanh thiếu niên khó khăn",
        scope="Miền Nam Việt Nam",
        founded_date="1992-05-20",
        campaign_id="CC0009",
        gender="Nam",
        full_name="Damien Roberts",
        phone="0901333009",
        cccd="079080007777",
        address="Hồ Chí Minh",
        email="damien@gmail.com",
        qr_path="qr6.png",
        avatar_path="avt6.png",
    )

    window = DonationPage(page6)
    window.show()
    sys.exit(app.exec())
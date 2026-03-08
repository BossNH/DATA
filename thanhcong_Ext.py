from pathlib import Path

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QMessageBox


class ThanhCongWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.base_dir = Path(__file__).resolve().parent
        ui_path = self.base_dir / "thanhcong.ui"
        uic.loadUi(str(ui_path), self)

        self.campaign_data = {
            "title": "Quỹ Nhịp Tim Việt Nam- Vết sẹo cuộc đời",
            "description": (
                "Chương trình y tế nhân đạo nhằm hỗ trợ chi phí phẫu thuật tim cho trẻ em nghèo "
                "mắc bệnh tim bẩm sinh, giúp các em có cơ hội sống khỏe mạnh và theo đuổi ước mơ"
            ),
            "raised": 1000000000,
            "target": 15000000000,
            "percent": 6.67,
            "activities": [
                "Tài trợ chi phí phẫu thuật tim cho trẻ em nghèo",
                "Khám sàng lọc tim bẩm sinh tại các tỉnh xa",
                "Hỗ trợ hậu phẫu và dinh dưỡng cho bệnh nhi",
            ],
            "scope": "Toàn quốc",
            "founded_date": "2006-11-21",
            "campaign_id": "CC0001",
            "gender": "Nam",
            "full_name": "Rad Kivette",
            "phone": "0908555001",
            "cccd": "079070001234",
            "address": "Hồ Chí Minh",
            "email": "rad.kivette@gmail.com",
            "avatar_path": "avt1.png",
        }

        self.setup_data()
        self.setup_events()

    def setup_data(self):
        data = self.campaign_data

        if hasattr(self, "campaignTitle"):
            self.campaignTitle.setText(data["title"])
        if hasattr(self, "campaignDesc"):
            self.campaignDesc.setText(data["description"])
        if hasattr(self, "amountLabel"):
            self.amountLabel.setText(f'{data["raised"]}/{data["target"]}')
        if hasattr(self, "percentLabel"):
            self.percentLabel.setText(f'{data["percent"]:.2f}%')

        if hasattr(self, "activitiesText"):
            self.activitiesText.setText("\n".join(data["activities"]))
        if hasattr(self, "scopeText"):
            self.scopeText.setText(data["scope"])
        if hasattr(self, "dateText"):
            self.dateText.setText(data["founded_date"])

        if hasattr(self, "idValue"):
            self.idValue.setText(data["campaign_id"])
        if hasattr(self, "genderValue"):
            self.genderValue.setText(data["gender"])
        if hasattr(self, "nameValue"):
            self.nameValue.setText(data["full_name"])
        if hasattr(self, "phoneValue"):
            self.phoneValue.setText(data["phone"])
        if hasattr(self, "cccdValue"):
            self.cccdValue.setText(data["cccd"])
        if hasattr(self, "addressValue"):
            self.addressValue.setText(data["address"])
        if hasattr(self, "emailValue"):
            self.emailValue.setText(data["email"])

        avatar_path = self.base_dir / data["avatar_path"]
        if hasattr(self, "avatarLabel") and avatar_path.exists():
            avatar_pixmap = QPixmap(str(avatar_path))
            if not avatar_pixmap.isNull():
                self.avatarLabel.setPixmap(avatar_pixmap)
                self.avatarLabel.setScaledContents(True)

        self.update_progress_fill(data["percent"])

    def setup_events(self):
        if hasattr(self, "backBtn"):
            self.backBtn.clicked.connect(self.go_back)

        for button_name, message in {
            "navHome": "Bạn bấm Trang chủ.",
            "navStats": "Bạn bấm Thống kê.",
            "navChat": "Bạn bấm Chatbot.",
            "navPublic": "Bạn bấm Công khai.",
        }.items():
            if hasattr(self, button_name):
                getattr(self, button_name).clicked.connect(
                    lambda checked=False, msg=message: self.show_message(msg)
                )

    def update_progress_fill(self, percent: float):
        if not hasattr(self, "progressBg") or not hasattr(self, "progressFill"):
            return

        percent = max(0.0, min(float(percent), 100.0))
        bg_width = self.progressBg.width()
        bg_height = self.progressBg.height()
        fill_width = int(bg_width * percent / 100.0)
        self.progressFill.setGeometry(0, 0, fill_width, bg_height)

    def show_message(self, text: str):
        QMessageBox.information(self, "Thông báo", text)

    def go_back(self):
        QMessageBox.information(self, "Thông báo", "Bạn đã bấm Quay lại.")

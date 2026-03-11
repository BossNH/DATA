from pathlib import Path

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QMessageBox


class ThanhCongWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.base_dir = Path(__file__).resolve().parent
        ui_path = self.base_dir / "cd1_thanhcong.ui"
        uic.loadUi(str(ui_path), self)

        self.campaign_data = {
            "title": "Hỗ trợ nạn nhân Chất độc Da cam (VAVA)",
            "description":
                "Chăm sóc, giúp đỡ và bảo vệ quyền lợi cho các nạn nhân chất độc da cam, giúp họ vượt qua mặc cảm và cải thiện đời sống."
            ,
            "raised": 1000000000,
            "target": 8000000000,
            "percent": 12.5,
            "activities": [
                "Xây dựng nhà tình nghĩa cho gia đình nạn nhân",
                "Hỗ trợ phục hồi chức năng và dạy nghề",
                "Cung cấp trợ cấp khó khăn hàng tháng",
            ],
            "scope": "Toàn quốc",
            "founded_date": "2004-01-10",
            "campaign_id": "CC0004",
            "gender": "Nam",
            "full_name": " Nguyễn Văn Rinh ",
            "phone": "0903888004",
            "cccd": " 001042004444",
            "address": "Hà Nội",
            "email": " rinh.nguyen@gmail.com",
            "qr_path": "qr.png",
            "avatar_path": "avt2.png",
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

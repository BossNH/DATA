from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class XacMinhWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("cd1_xacminh.ui", self)

        self.campaign_data = {
            "title": "Quỹ Trò nghèo vùng cao (Cơm có thịt)",
            "description":
                "Mang lại những bữa ăn đủ chất dinh dưỡng cho học sinh vùng cao, giúp giảm tỷ lệ bỏ học và nâng cao thể trạng cho trẻ em."
            ,
            "raised": 1000000000,
            "target": 12000000000,
            "percent": 8.33,
            "activities": [
                " Tài trợ bữa ăn trưa dinh dưỡng tại trường",
                "Cung cấp quần áo ấm, chăn màn cho học sinh",
                "Xây dựng phòng học và ký túc xá",
            ],
            "scope": "Miền núi phía Bắc",
            "founded_date": "2014-02-25",
            "campaign_id": "CC0005",
            "gender": "Nam",
            "full_name": "  Trần Đăng Tuấn ",
            "phone": "0912999005",
            "cccd": "001057003333",
            "address": "Hà Nội",
            "email": "tuan.tran@gmail.com",
            "qr_path": "qr.png",
            "avatar_path": "avt3.png",
        }

        self.setup_data()
        self.setup_events()

    def setup_data(self):
        data = self.campaign_data
        self.campaignTitle.setText(data["title"])
        self.campaignDesc.setText(data["description"])
        self.amountLabel.setText(f'{data["raised"]}/{data["target"]}')
        self.percentLabel.setText(f'{data["percent"]:.2f}%')
        self.activitiesText.setText("\n".join(data["activities"]))
        self.scopeText.setText(data["scope"])
        self.dateText.setText(data["founded_date"])
        self.idValue.setText(data["campaign_id"])
        self.genderValue.setText(data["gender"])
        self.nameValue.setText(data["full_name"])
        self.phoneValue.setText(data["phone"])
        self.cccdValue.setText(data["cccd"])
        self.addressValue.setText(data["address"])
        self.emailValue.setText(data["email"])

        avatar_pixmap = QPixmap(data["avatar_path"])
        if not avatar_pixmap.isNull():
            self.avatarLabel.setPixmap(avatar_pixmap)
            self.avatarLabel.setScaledContents(True)
            self.avatarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.update_progress_fill(data["percent"])

    def setup_events(self):
        self.backBtn.clicked.connect(lambda: self.show_message("Bạn đã bấm Quay lại."))
        self.navHome.clicked.connect(lambda: self.show_message("Bạn bấm Trang chủ"))
        self.navStats.clicked.connect(lambda: self.show_message("Bạn bấm Thống kê"))
        self.navChat.clicked.connect(lambda: self.show_message("Bạn bấm Chatbot"))
        self.navPublic.clicked.connect(lambda: self.show_message("Bạn bấm Công khai"))

    def update_progress_fill(self, percent):
        percent = max(0, min(percent, 100))
        bg_width = self.progressBg.width()
        fill_width = int(bg_width * percent / 100)
        self.progressFill.setGeometry(0, 0, fill_width, self.progressBg.height())

    def show_message(self, text):
        QMessageBox.information(self, "Thông báo", text)

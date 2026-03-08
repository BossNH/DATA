from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class TheoDoiChienDichWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("theodoi_chiendich.ui", self)

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
            "qr_path": "qr.png",
            "avatar_path": "avt1.png",
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

        qr_pixmap = QPixmap(data["qr_path"])
        if not qr_pixmap.isNull():
            self.qrLabel.setPixmap(qr_pixmap)
            self.qrLabel.setScaledContents(True)

        avatar_pixmap = QPixmap(data["avatar_path"])
        if not avatar_pixmap.isNull():
            self.avatarLabel.setPixmap(avatar_pixmap)
            self.avatarLabel.setScaledContents(True)
            self.avatarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.update_progress_fill(data["percent"])

    def setup_events(self):
        self.sendBtn.clicked.connect(self.gui_ma_giao_dich)
        self.backBtn.clicked.connect(lambda: self.thong_bao("Bạn đã bấm Quay lại."))
        self.navHome.clicked.connect(lambda: self.thong_bao("Bạn bấm Trang chủ"))
        self.navStats.clicked.connect(lambda: self.thong_bao("Bạn bấm Thống kê"))
        self.navChat.clicked.connect(lambda: self.thong_bao("Bạn bấm Chatbot"))
        self.navPublic.clicked.connect(lambda: self.thong_bao("Bạn bấm Công khai"))

    def update_progress_fill(self, percent):
        percent = max(0, min(percent, 100))
        bg_width = self.progressBg.width()
        fill_width = int(bg_width * percent / 100)
        self.progressFill.setGeometry(0, 0, fill_width, self.progressBg.height())

    def gui_ma_giao_dich(self):
        ma = self.codeEdit.text().strip()
        if not ma:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập mã giao dịch.")
            return

        QMessageBox.information(self, "Xác nhận", f"Đã gửi mã giao dịch: {ma}")
        self.codeEdit.clear()

    def thong_bao(self, noi_dung):
        QMessageBox.information(self, "Thông báo", noi_dung)

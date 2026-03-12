# Form implementation generated from reading ui file 'C:\\Users\\ADMIN\\PycharmProjects\\DoAnKTLT\\welcome_campaign.ui'
#
# Đã chỉnh lại navbar theo file test.py
#

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 760)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 760))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 760))
        MainWindow.setStyleSheet("""
QMainWindow, QWidget#centralwidget {
    background: #ECECEC;
    font-family: "Segoe UI";
}

QFrame#mainPanel {
    background: #FDF3F9;
    border: none;
}

/* ===== NAVBAR MỚI từ file test ===== */
QFrame#navFrame {
    background: #F5DCE6;
    border: none;
    border-radius: 18px;
}

QLabel#logoImage {
    background: transparent;
    border: none;
}

QLabel#brandTitle {
    color: #9C4F74;
    font-size: 18pt;
    font-weight: 800;
    background: transparent;
}

QLabel#brandSubtitle {
    color: #9D8A93;
    font-size: 8pt;
    font-weight: 500;
    background: transparent;
}

QPushButton#btnHome,
QPushButton#btnCreate,
QPushButton#btnFollow,
QPushButton#btnPublic {
    background: transparent;
    border: none;
    border-radius: 18px;
    padding: 10px 18px;
    color: #2C2328;
    font-size: 11pt;
    font-weight: 600;
    text-align: center;
}

QPushButton#btnHome:hover,
QPushButton#btnCreate:hover,
QPushButton#btnFollow:hover,
QPushButton#btnPublic:hover {
    background: #EEC9D8;
}

QPushButton#btnHome:pressed,
QPushButton#btnCreate:pressed,
QPushButton#btnFollow:pressed,
QPushButton#btnPublic:pressed {
    background: #E2B5C7;
}

QPushButton#btnHome {
    background: #C98AA5;
    color: white;
    font-weight: 700;
}

QToolButton#btnNotify,
QToolButton#btnSetting,
QToolButton#btnProfile {
    background: transparent;
    border: none;
    border-radius: 18px;
    color: #2C2328;
    font-size: 16pt;
    padding: 6px;
}

QToolButton#btnNotify:hover,
QToolButton#btnSetting:hover,
QToolButton#btnProfile:hover {
    background: #EEC9D8;
}

QLabel#notifyBadge {
    background: #E74C3C;
    color: white;
    border-radius: 8px;
    font-size: 8pt;
    font-weight: 700;
    padding: 0px;
}

/* ===== PHẦN NỘI DUNG WELCOME ===== */
QLabel#heroTitle {
    color: #6E3F63;
    font-size: 58px;
    font-weight: 900;
    background: transparent;
}

QLabel#heroText1,
QLabel#heroText2,
QLabel#heroText3 {
    color: #222222;
    font-size: 18px;
    font-weight: 400;
    background: transparent;
}

QPushButton#createBtn {
    background: #E9B8CB;
    color: #6A3E63;
    font-size: 26px;
    font-weight: 800;
    border: 1px solid #6D5061;
    border-radius: 28px;
    padding: 12px 24px;
}

QPushButton#createBtn:hover {
    background: #E4AFC5;
}

QLabel#decorLabel {
    background: transparent;
}
""")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainPanel = QtWidgets.QFrame(parent=self.centralwidget)
        self.mainPanel.setGeometry(QtCore.QRect(40, 25, 1120, 690))
        self.mainPanel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.mainPanel.setObjectName("mainPanel")

        # ===== NAVBAR MỚI =====
        self.navFrame = QtWidgets.QFrame(parent=self.mainPanel)
        self.navFrame.setGeometry(QtCore.QRect(12, 12, 1096, 72))
        self.navFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.navFrame.setObjectName("navFrame")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.navFrame)
        self.horizontalLayout.setContentsMargins(18, 10, 18, 10)
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.logoLayout = QtWidgets.QHBoxLayout()
        self.logoLayout.setSpacing(8)
        self.logoLayout.setObjectName("logoLayout")

        self.logoImage = QtWidgets.QLabel(parent=self.navFrame)
        self.logoImage.setMinimumSize(QtCore.QSize(54, 54))
        self.logoImage.setMaximumSize(QtCore.QSize(54, 54))
        self.logoImage.setObjectName("logoImage")
        self.logoLayout.addWidget(self.logoImage)

        self.brandLayout = QtWidgets.QVBoxLayout()
        self.brandLayout.setSpacing(0)
        self.brandLayout.setObjectName("brandLayout")

        self.brandTitle = QtWidgets.QLabel(parent=self.navFrame)
        self.brandTitle.setObjectName("brandTitle")
        self.brandLayout.addWidget(self.brandTitle)

        self.brandSubtitle = QtWidgets.QLabel(parent=self.navFrame)
        self.brandSubtitle.setObjectName("brandSubtitle")
        self.brandLayout.addWidget(self.brandSubtitle)

        self.logoLayout.addLayout(self.brandLayout)
        self.horizontalLayout.addLayout(self.logoLayout)

        self.menuLayout = QtWidgets.QHBoxLayout()
        self.menuLayout.setSpacing(10)
        self.menuLayout.setObjectName("menuLayout")

        self.btnHome = QtWidgets.QPushButton(parent=self.navFrame)
        self.btnHome.setMinimumSize(QtCore.QSize(0, 42))
        self.btnHome.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnHome.setObjectName("btnHome")
        self.menuLayout.addWidget(self.btnHome)

        self.btnCreate = QtWidgets.QPushButton(parent=self.navFrame)
        self.btnCreate.setMinimumSize(QtCore.QSize(0, 42))
        self.btnCreate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnCreate.setObjectName("btnCreate")
        self.menuLayout.addWidget(self.btnCreate)

        self.btnFollow = QtWidgets.QPushButton(parent=self.navFrame)
        self.btnFollow.setMinimumSize(QtCore.QSize(0, 42))
        self.btnFollow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnFollow.setObjectName("btnFollow")
        self.menuLayout.addWidget(self.btnFollow)

        self.btnPublic = QtWidgets.QPushButton(parent=self.navFrame)
        self.btnPublic.setMinimumSize(QtCore.QSize(0, 42))
        self.btnPublic.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnPublic.setObjectName("btnPublic")
        self.menuLayout.addWidget(self.btnPublic)

        self.horizontalLayout.addLayout(self.menuLayout)
        self.horizontalLayout.addStretch()

        self.rightActionsWidget = QtWidgets.QWidget(parent=self.navFrame)
        self.rightActionsWidget.setMinimumSize(QtCore.QSize(150, 50))
        self.rightActionsWidget.setObjectName("rightActionsWidget")

        self.rightActionsLayout = QtWidgets.QHBoxLayout(self.rightActionsWidget)
        self.rightActionsLayout.setContentsMargins(0, 0, 0, 0)
        self.rightActionsLayout.setSpacing(8)
        self.rightActionsLayout.setObjectName("rightActionsLayout")

        self.notifyWrapper = QtWidgets.QWidget(parent=self.rightActionsWidget)
        self.notifyWrapper.setMinimumSize(QtCore.QSize(36, 36))
        self.notifyWrapper.setMaximumSize(QtCore.QSize(36, 36))
        self.notifyWrapper.setObjectName("notifyWrapper")

        self.btnNotify = QtWidgets.QToolButton(parent=self.notifyWrapper)
        self.btnNotify.setGeometry(QtCore.QRect(0, -7, 41, 41))
        self.btnNotify.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnNotify.setObjectName("btnNotify")

        self.notifyBadge = QtWidgets.QLabel(parent=self.notifyWrapper)
        self.notifyBadge.setGeometry(QtCore.QRect(20, 0, 16, 16))
        self.notifyBadge.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.notifyBadge.setObjectName("notifyBadge")

        self.rightActionsLayout.addWidget(self.notifyWrapper)

        self.btnSetting = QtWidgets.QToolButton(parent=self.rightActionsWidget)
        self.btnSetting.setMinimumSize(QtCore.QSize(36, 36))
        self.btnSetting.setMaximumSize(QtCore.QSize(36, 36))
        self.btnSetting.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnSetting.setObjectName("btnSetting")
        self.rightActionsLayout.addWidget(self.btnSetting)

        self.btnProfile = QtWidgets.QToolButton(parent=self.rightActionsWidget)
        self.btnProfile.setMinimumSize(QtCore.QSize(40, 40))
        self.btnProfile.setMaximumSize(QtCore.QSize(40, 40))
        self.btnProfile.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnProfile.setObjectName("btnProfile")
        self.rightActionsLayout.addWidget(self.btnProfile)

        self.horizontalLayout.addWidget(self.rightActionsWidget)

        # ===== NỘI DUNG CŨ CỦA WELCOME =====
        self.decorLabel = QtWidgets.QLabel(parent=self.mainPanel)
        self.decorLabel.setGeometry(QtCore.QRect(0, 300, 1120, 360))
        self.decorLabel.setText("")
        self.decorLabel.setScaledContents(True)
        self.decorLabel.setObjectName("decorLabel")

        self.heroTitle = QtWidgets.QLabel(parent=self.mainPanel)
        self.heroTitle.setGeometry(QtCore.QRect(150, 130, 340, 78))
        self.heroTitle.setObjectName("heroTitle")

        self.heroText1 = QtWidgets.QLabel(parent=self.mainPanel)
        self.heroText1.setGeometry(QtCore.QRect(150, 225, 700, 30))
        self.heroText1.setObjectName("heroText1")

        self.heroText2 = QtWidgets.QLabel(parent=self.mainPanel)
        self.heroText2.setGeometry(QtCore.QRect(150, 268, 850, 30))
        self.heroText2.setObjectName("heroText2")

        self.heroText3 = QtWidgets.QLabel(parent=self.mainPanel)
        self.heroText3.setGeometry(QtCore.QRect(150, 311, 850, 30))
        self.heroText3.setObjectName("heroText3")

        self.createBtn = QtWidgets.QPushButton(parent=self.mainPanel)
        self.createBtn.setGeometry(QtCore.QRect(355, 430, 410, 72))
        self.createBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.createBtn.setObjectName("createBtn")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Unhi - Donarity"))

        self.logoImage.setText(_translate(
            "MainWindow",
            "<html><head/><body><p><span style=\" font-size:28pt; color:#9c4f74;\">🕊</span></p></body></html>"
        ))
        self.brandTitle.setText(_translate("MainWindow", "Donarity"))
        self.brandSubtitle.setText(_translate("MainWindow", "by group 10"))

        self.btnHome.setText(_translate("MainWindow", "🏛 Trang chủ"))
        self.btnCreate.setText(_translate("MainWindow", "+  Tạo chiến dịch"))
        self.btnFollow.setText(_translate("MainWindow", "🎞  Theo dõi chiến dịch"))
        self.btnPublic.setText(_translate("MainWindow", "👁 Công khai"))

        self.btnNotify.setText(_translate("MainWindow", "🔔"))
        self.notifyBadge.setText(_translate("MainWindow", "0"))
        self.btnSetting.setText(_translate("MainWindow", "⚙"))
        self.btnProfile.setText(_translate("MainWindow", "👤"))

        self.heroTitle.setText(_translate("MainWindow", "Xin chào!"))
        self.heroText1.setText(_translate("MainWindow", "Chào mừng bạn đến với hành trình lan tỏa yêu thương."))
        self.heroText2.setText(_translate("MainWindow", "Mỗi chiến dịch bạn tạo hôm nay có thể trở thành hy vọng của một ai đó ngày mai."))
        self.heroText3.setText(_translate("MainWindow", "Hãy tạo chiến dịch từ thiện của bạn và bắt đầu hành trình ý nghĩa ngay hôm nay."))
        self.createBtn.setText(_translate("MainWindow", "Tạo chiến dịch mới"))

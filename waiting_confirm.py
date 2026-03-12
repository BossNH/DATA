from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 760)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 760))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 760))
        MainWindow.setStyleSheet("""
QMainWindow, QWidget {
    background-color: #FDF1F7;
    color: #222222;
    font-family: "Segoe UI";
}

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

QPushButton#btnCreate {
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

QLabel#backLabel {
    color: #111111;
    font-size: 14px;
    font-weight: 600;
    background: transparent;
}

QFrame#mainCard {
    background-color: #FCFAFC;
    border: none;
    border-radius: 24px;
}

QLabel#mainTitle {
    color: #7B456F;
    font-size: 35px;
    font-weight: 800;
    background: transparent;
}

QLabel#subText1, QLabel#subText2, QLabel#bottomText {
    color: #1F1F1F;
    font-size: 16px;
    font-weight: 400;
    background: transparent;
}

QLabel#hourglassLabel {
    color: #F2C8D8;
    font-size: 165px;
    background: transparent;
}

QLabel#dot1, QLabel#dot2, QLabel#dot3 {
    color: #D7CFD5;
    font-size: 30px;
    background: transparent;
}

QLabel#dot2 {
    color: #BEB3BD;
}
""")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ===== NAVBAR MỚI =====
        self.navFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.navFrame.setGeometry(QtCore.QRect(22, 12, 1156, 72))
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
        self.logoImage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
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
        self.rightActionsWidget.setMaximumSize(QtCore.QSize(150, 50))
        self.rightActionsWidget.setObjectName("rightActionsWidget")

        self.rightActionsWidget.setStyleSheet("background: transparent; border: none;")

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
        self.notifyBadge.setStyleSheet("""
            background: #E74C3C;
            color: white;
            border-radius: 8px;
            font-size: 8pt;
            font-weight: 700;
            border: none;
        """)
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

        # ===== CONTENT =====
        self.backLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.backLabel.setGeometry(QtCore.QRect(30, 95, 100, 24))
        self.backLabel.setObjectName("backLabel")

        self.mainCard = QtWidgets.QFrame(parent=self.centralwidget)
        self.mainCard.setGeometry(QtCore.QRect(90, 130, 1040, 590))
        self.mainCard.setObjectName("mainCard")

        self.mainTitle = QtWidgets.QLabel(parent=self.mainCard)
        self.mainTitle.setGeometry(QtCore.QRect(245, 40, 550, 58))
        self.mainTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainTitle.setObjectName("mainTitle")

        self.subText1 = QtWidgets.QLabel(parent=self.mainCard)
        self.subText1.setGeometry(QtCore.QRect(165, 125, 710, 28))
        self.subText1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.subText1.setObjectName("subText1")

        self.subText2 = QtWidgets.QLabel(parent=self.mainCard)
        self.subText2.setGeometry(QtCore.QRect(255, 170, 530, 30))
        self.subText2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.subText2.setObjectName("subText2")

        self.hourglassLabel = QtWidgets.QLabel(parent=self.mainCard)
        self.hourglassLabel.setGeometry(QtCore.QRect(385, 225, 270, 190))
        self.hourglassLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hourglassLabel.setObjectName("hourglassLabel")

        self.dot1 = QtWidgets.QLabel(parent=self.mainCard)
        self.dot1.setGeometry(QtCore.QRect(486, 430, 20, 28))
        self.dot1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dot1.setObjectName("dot1")

        self.dot2 = QtWidgets.QLabel(parent=self.mainCard)
        self.dot2.setGeometry(QtCore.QRect(510, 430, 20, 28))
        self.dot2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dot2.setObjectName("dot2")

        self.dot3 = QtWidgets.QLabel(parent=self.mainCard)
        self.dot3.setGeometry(QtCore.QRect(534, 430, 20, 28))
        self.dot3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dot3.setObjectName("dot3")

        self.bottomText = QtWidgets.QLabel(parent=self.mainCard)
        self.bottomText.setGeometry(QtCore.QRect(180, 505, 680, 32))
        self.bottomText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bottomText.setObjectName("bottomText")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Donarity - Chờ xác nhận chiến dịch"))

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

        self.backLabel.setText(_translate("MainWindow", "← Quay lại"))
        self.mainTitle.setText(_translate("MainWindow", "Chờ xác nhận chiến dịch"))
        self.subText1.setText(_translate("MainWindow", "Chiến dịch của bạn đang được xem xét và sẽ sớm được xác nhận."))
        self.subText2.setText(_translate("MainWindow", "Cảm ơn bạn đã kiên nhẫn chờ đợi!"))
        self.hourglassLabel.setText(_translate("MainWindow", "⌛"))
        self.dot1.setText(_translate("MainWindow", "•"))
        self.dot2.setText(_translate("MainWindow", "•"))
        self.dot3.setText(_translate("MainWindow", "•"))
        self.bottomText.setText(_translate("MainWindow", "Chúng tôi sẽ thông báo đến bạn ngay khi có cập nhật mới."))

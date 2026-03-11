

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 760)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 760))
        MainWindow.setStyleSheet("""QMainWindow, QWidget {
    background: #F3E8ED;
    font-family: "Segoe UI";
}
QFrame#topBar {
    background: #F5DDE6;
    border: none;
}
QPushButton#navHome, QPushButton#navChatbot, QPushButton#navPublic {
    background: transparent;
    border: none;
    color: #222222;
    font-size: 12pt;
    font-weight: 700;
    border-radius: 18px;
    padding: 8px 16px;
}
QPushButton#navHome:hover, QPushButton#navChatbot:hover, QPushButton#navPublic:hover {
    background: rgba(205,156,181,0.18);
}
QPushButton#navStat {
    background: #E7B5CF;
    border: none;
    color: #5F3556;
    font-size: 12pt;
    font-weight: 700;
    border-radius: 18px;
    padding: 8px 16px;
}
QLabel#brandTitle {
    color: #7A3B71;
    font-size: 18pt;
    font-weight: 800;
}
QLabel#brandSub {
    color: #7F6D79;
    font-size: 8pt;
}
QFrame#heroFrame {
    border: none;
    border-bottom-left-radius: 14px;
    border-bottom-right-radius: 14px;
    background-image: url(hero_pg.png);
    background-repeat: no-repeat;
    background-position: center;
}
QLabel#heroTitle {
    color: #6C3D65;
    font-size: 34pt;
    font-weight: 900;
    background: transparent;
}
QFrame#statCard1, QFrame#statCard2, QFrame#statCard3 {
    background: rgba(255,255,255,0.68);
    border: 2px solid #EFBFD2;
    border-radius: 22px;
}
QLabel.statTitle {
    color: #6F4767;
    font-size: 16pt;
    font-weight: 700;
    background: transparent;
}
QLabel.statValue {
    color: #9A7695;
    font-size: 24pt;
    font-weight: 800;
    background: transparent;
}
QPushButton#historyBtn, QPushButton#monthBtn, QPushButton#exportBtn {
    background: #E8BFD0;
    color: #6D4767;
    border: 1.5px solid #6A4C64;
    border-radius: 18px;
    font-size: 12pt;
    font-weight: 700;
    padding: 6px 18px;
}
QFrame.txCard {
    background: rgba(255,255,255,0.62);
    border: 2px solid #F0BFD2;
    border-radius: 20px;
}
QLabel.txTitle {
    color: #6B4364;
    font-size: 20pt;
    font-weight: 800;
    background: transparent;
}
QLabel.txTime {
    color: #9A7B94;
    font-size: 11pt;
    font-weight: 700;
    background: transparent;
}
QLabel.txAmount {
    color: #9A7B94;
    font-size: 24pt;
    font-weight: 800;
    background: transparent;
}
QScrollArea {
    border: none;
    background: transparent;
}
QScrollBar:vertical {
    background: rgba(230, 202, 216, 0.45);
    width: 10px;
    border-radius: 5px;
    margin: 4px 0 4px 0;
}
QScrollBar::handle:vertical {
    background: #D9A9BE;
    border-radius: 5px;
    min-height: 34px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: transparent;
}""")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 6, 0, 8)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.topBar = QtWidgets.QFrame(parent=self.centralwidget)
        self.topBar.setMinimumSize(QtCore.QSize(0, 50))
        self.topBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.topBar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.topBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.topBar.setObjectName("topBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topBar)
        self.horizontalLayout.setContentsMargins(18, 0, 18, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logoIcon = QtWidgets.QLabel(parent=self.topBar)
        self.logoIcon.setObjectName("logoIcon")
        self.horizontalLayout.addWidget(self.logoIcon)
        self.verticalLayout_brand = QtWidgets.QVBoxLayout()
        self.verticalLayout_brand.setSpacing(0)
        self.verticalLayout_brand.setObjectName("verticalLayout_brand")
        self.brandTitle = QtWidgets.QLabel(parent=self.topBar)
        self.brandTitle.setObjectName("brandTitle")
        self.verticalLayout_brand.addWidget(self.brandTitle)
        self.brandSub = QtWidgets.QLabel(parent=self.topBar)
        self.brandSub.setObjectName("brandSub")
        self.verticalLayout_brand.addWidget(self.brandSub)
        self.horizontalLayout.addLayout(self.verticalLayout_brand)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.navHome = QtWidgets.QPushButton(parent=self.topBar)
        self.navHome.setObjectName("navHome")
        self.horizontalLayout.addWidget(self.navHome)
        self.navStat = QtWidgets.QPushButton(parent=self.topBar)
        self.navStat.setObjectName("navStat")
        self.horizontalLayout.addWidget(self.navStat)
        self.navChatbot = QtWidgets.QPushButton(parent=self.topBar)
        self.navChatbot.setObjectName("navChatbot")
        self.horizontalLayout.addWidget(self.navChatbot)
        self.navPublic = QtWidgets.QPushButton(parent=self.topBar)
        self.navPublic.setObjectName("navPublic")
        self.horizontalLayout.addWidget(self.navPublic)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bellBtn = QtWidgets.QToolButton(parent=self.topBar)
        self.bellBtn.setObjectName("bellBtn")
        self.horizontalLayout.addWidget(self.bellBtn)
        self.settingBtn = QtWidgets.QToolButton(parent=self.topBar)
        self.settingBtn.setObjectName("settingBtn")
        self.horizontalLayout.addWidget(self.settingBtn)
        self.avatarBtn = QtWidgets.QToolButton(parent=self.topBar)
        self.avatarBtn.setObjectName("avatarBtn")
        self.horizontalLayout.addWidget(self.avatarBtn)
        self.verticalLayout_9.addWidget(self.topBar)

        self.heroFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.heroFrame.setMinimumSize(QtCore.QSize(0, 390))
        self.heroFrame.setMaximumSize(QtCore.QSize(16777215, 390))
        self.heroFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.heroFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.heroFrame.setObjectName("heroFrame")
        self.verticalLayout_hero = QtWidgets.QVBoxLayout(self.heroFrame)
        self.verticalLayout_hero.setContentsMargins(34, 28, 34, 18)
        self.verticalLayout_hero.setObjectName("verticalLayout_hero")
        self.backLabel = QtWidgets.QLabel(parent=self.heroFrame)
        self.backLabel.setObjectName("backLabel")
        self.verticalLayout_hero.addWidget(self.backLabel, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.heroTitle = QtWidgets.QLabel(parent=self.heroFrame)
        self.heroTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heroTitle.setObjectName("heroTitle")
        self.verticalLayout_hero.addWidget(self.heroTitle)
        spacerItem2 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_hero.addItem(spacerItem2)
        self.horizontalLayout_stats = QtWidgets.QHBoxLayout()
        self.horizontalLayout_stats.setSpacing(14)
        self.horizontalLayout_stats.setObjectName("horizontalLayout_stats")

        self.statCard1 = QtWidgets.QFrame(parent=self.heroFrame)
        self.statCard1.setObjectName("statCard1")
        self.verticalLayout_card1 = QtWidgets.QVBoxLayout(self.statCard1)
        self.verticalLayout_card1.setContentsMargins(18, 18, 18, 18)
        self.labelStatTitle1 = QtWidgets.QLabel(parent=self.statCard1)
        self.labelStatTitle1.setProperty("class", "statTitle")
        self.labelStatTitle1.setObjectName("labelStatTitle1")
        self.verticalLayout_card1.addWidget(self.labelStatTitle1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_card1.addItem(spacerItem3)
        self.labelStatValue1 = QtWidgets.QLabel(parent=self.statCard1)
        self.labelStatValue1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelStatValue1.setProperty("class", "statValue")
        self.labelStatValue1.setObjectName("labelStatValue1")
        self.verticalLayout_card1.addWidget(self.labelStatValue1)
        self.horizontalLayout_stats.addWidget(self.statCard1)

        self.statCard2 = QtWidgets.QFrame(parent=self.heroFrame)
        self.statCard2.setObjectName("statCard2")
        self.verticalLayout_card2 = QtWidgets.QVBoxLayout(self.statCard2)
        self.verticalLayout_card2.setContentsMargins(18, 18, 18, 18)
        self.labelStatTitle2 = QtWidgets.QLabel(parent=self.statCard2)
        self.labelStatTitle2.setProperty("class", "statTitle")
        self.labelStatTitle2.setObjectName("labelStatTitle2")
        self.verticalLayout_card2.addWidget(self.labelStatTitle2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_card2.addItem(spacerItem4)
        self.labelStatValue2 = QtWidgets.QLabel(parent=self.statCard2)
        self.labelStatValue2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelStatValue2.setProperty("class", "statValue")
        self.labelStatValue2.setObjectName("labelStatValue2")
        self.verticalLayout_card2.addWidget(self.labelStatValue2)
        self.horizontalLayout_stats.addWidget(self.statCard2)

        self.statCard3 = QtWidgets.QFrame(parent=self.heroFrame)
        self.statCard3.setObjectName("statCard3")
        self.verticalLayout_card3 = QtWidgets.QVBoxLayout(self.statCard3)
        self.verticalLayout_card3.setContentsMargins(18, 18, 18, 18)
        self.labelStatTitle3 = QtWidgets.QLabel(parent=self.statCard3)
        self.labelStatTitle3.setProperty("class", "statTitle")
        self.labelStatTitle3.setObjectName("labelStatTitle3")
        self.verticalLayout_card3.addWidget(self.labelStatTitle3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_card3.addItem(spacerItem5)
        self.labelStatValue3 = QtWidgets.QLabel(parent=self.statCard3)
        self.labelStatValue3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelStatValue3.setProperty("class", "statValue")
        self.labelStatValue3.setObjectName("labelStatValue3")
        self.verticalLayout_card3.addWidget(self.labelStatValue3)
        self.horizontalLayout_stats.addWidget(self.statCard3)

        self.verticalLayout_hero.addLayout(self.horizontalLayout_stats)
        self.verticalLayout_9.addWidget(self.heroFrame)

        self.controlWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.controlWidget.setObjectName("controlWidget")
        self.horizontalLayout_control = QtWidgets.QHBoxLayout(self.controlWidget)
        self.horizontalLayout_control.setContentsMargins(32, 24, 32, 18)
        self.horizontalLayout_control.setObjectName("horizontalLayout_control")
        self.historyBtn = QtWidgets.QPushButton(parent=self.controlWidget)
        self.historyBtn.setMinimumSize(QtCore.QSize(220, 36))
        self.historyBtn.setMaximumSize(QtCore.QSize(220, 36))
        self.historyBtn.setObjectName("historyBtn")
        self.horizontalLayout_control.addWidget(self.historyBtn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_control.addItem(spacerItem6)

        self.exportBtn = QtWidgets.QPushButton(parent=self.controlWidget)
        self.exportBtn.setMinimumSize(QtCore.QSize(140, 36))
        self.exportBtn.setMaximumSize(QtCore.QSize(140, 36))
        self.exportBtn.setObjectName("exportBtn")
        self.horizontalLayout_control.addWidget(self.exportBtn)

        self.monthBtn = QtWidgets.QPushButton(parent=self.controlWidget)
        self.monthBtn.setMinimumSize(QtCore.QSize(175, 36))
        self.monthBtn.setMaximumSize(QtCore.QSize(175, 36))
        self.monthBtn.setObjectName("monthBtn")
        self.horizontalLayout_control.addWidget(self.monthBtn)
        self.verticalLayout_9.addWidget(self.controlWidget)

        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1030, 300))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_scroll = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_scroll.setContentsMargins(32, 0, 24, 10)
        self.verticalLayout_scroll.setSpacing(14)
        self.verticalLayout_scroll.setObjectName("verticalLayout_scroll")

        self.txCard1 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.txCard1.setMinimumSize(QtCore.QSize(0, 92))
        self.txCard1.setMaximumSize(QtCore.QSize(16777215, 92))
        self.txCard1.setProperty("class", "txCard")
        self.txCard1.setObjectName("txCard1")
        self.horizontalLayout_tx1 = QtWidgets.QHBoxLayout(self.txCard1)
        self.horizontalLayout_tx1.setContentsMargins(18, 12, 24, 12)
        self.verticalLayout_tx1_text = QtWidgets.QVBoxLayout()
        self.verticalLayout_tx1_text.setSpacing(4)
        self.txTitle1 = QtWidgets.QLabel(parent=self.txCard1)
        self.txTitle1.setProperty("class", "txTitle")
        self.txTitle1.setObjectName("txTitle1")
        self.verticalLayout_tx1_text.addWidget(self.txTitle1)
        self.txTime1 = QtWidgets.QLabel(parent=self.txCard1)
        self.txTime1.setProperty("class", "txTime")
        self.txTime1.setObjectName("txTime1")
        self.verticalLayout_tx1_text.addWidget(self.txTime1)
        self.horizontalLayout_tx1.addLayout(self.verticalLayout_tx1_text)
        self.txAmount1 = QtWidgets.QLabel(parent=self.txCard1)
        self.txAmount1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txAmount1.setProperty("class", "txAmount")
        self.txAmount1.setObjectName("txAmount1")
        self.horizontalLayout_tx1.addWidget(self.txAmount1)
        self.verticalLayout_scroll.addWidget(self.txCard1)

        self.txCard2 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.txCard2.setMinimumSize(QtCore.QSize(0, 92))
        self.txCard2.setMaximumSize(QtCore.QSize(16777215, 92))
        self.txCard2.setProperty("class", "txCard")
        self.txCard2.setObjectName("txCard2")
        self.horizontalLayout_tx2 = QtWidgets.QHBoxLayout(self.txCard2)
        self.horizontalLayout_tx2.setContentsMargins(18, 12, 24, 12)
        self.verticalLayout_tx2_text = QtWidgets.QVBoxLayout()
        self.verticalLayout_tx2_text.setSpacing(4)
        self.txTitle2 = QtWidgets.QLabel(parent=self.txCard2)
        self.txTitle2.setProperty("class", "txTitle")
        self.txTitle2.setObjectName("txTitle2")
        self.verticalLayout_tx2_text.addWidget(self.txTitle2)
        self.txTime2 = QtWidgets.QLabel(parent=self.txCard2)
        self.txTime2.setProperty("class", "txTime")
        self.txTime2.setObjectName("txTime2")
        self.verticalLayout_tx2_text.addWidget(self.txTime2)
        self.horizontalLayout_tx2.addLayout(self.verticalLayout_tx2_text)
        self.txAmount2 = QtWidgets.QLabel(parent=self.txCard2)
        self.txAmount2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txAmount2.setProperty("class", "txAmount")
        self.txAmount2.setObjectName("txAmount2")
        self.horizontalLayout_tx2.addWidget(self.txAmount2)
        self.verticalLayout_scroll.addWidget(self.txCard2)

        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_scroll.addItem(spacerItem7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_9.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exportBtn.clicked.connect(self.show_donation_history)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_donation_history(self):
        history_text = (
            "LỊCH SỬ QUYÊN GÓP\n\n"
            "1. Dự án xây trường cho em (vùng cao)\n"
            "   Thời gian: 09:45:18  20/10/2025\n"
            "   Số tiền: 250,000\n\n"
            "2. Chương trình vì phụ nữ nghèo nông thôn\n"
            "   Thời gian: 09:06:18  10/12/2025\n"
            "   Số tiền: 250,000\n\n"
            "Tổng số giao dịch: 2\n"
            "Tổng số tiền đã quyên góp: 500,000"
        )

        QtWidgets.QMessageBox.information(
            self.exportBtn.window(),
            "Lịch sử quyên góp",
            history_text
        )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Donarity - Lịch sử giao dịch"))
        self.logoIcon.setText(_translate("MainWindow", "🕊"))
        self.brandTitle.setText(_translate("MainWindow", "Donarity"))
        self.brandSub.setText(_translate("MainWindow", "by group 10"))
        self.navHome.setText(_translate("MainWindow", "⌂ Trang chủ"))
        self.navStat.setText(_translate("MainWindow", "⚗ Thống kê"))
        self.navChatbot.setText(_translate("MainWindow", "◉ Chatbot"))
        self.navPublic.setText(_translate("MainWindow", "◉ Công khai"))
        self.bellBtn.setText(_translate("MainWindow", "🔔"))
        self.settingBtn.setText(_translate("MainWindow", "⚙"))
        self.avatarBtn.setText(_translate("MainWindow", "◉"))
        self.backLabel.setText(_translate("MainWindow", "← Quay lại"))
        self.heroTitle.setText(_translate("MainWindow", "LỊCH SỬ GIAO DỊCH"))
        self.labelStatTitle1.setText(_translate("MainWindow", "Tổng số tiền ủng hộ"))
        self.labelStatValue1.setText(_translate("MainWindow", "1,000,000"))
        self.labelStatTitle2.setText(_translate("MainWindow", "Chiến dịch ủng hộ"))
        self.labelStatValue2.setText(_translate("MainWindow", "4 Chiến dịch"))
        self.labelStatTitle3.setText(_translate("MainWindow", "Khoản ủng hộ trung bình"))
        self.labelStatValue3.setText(_translate("MainWindow", "250,000"))
        self.historyBtn.setText(_translate("MainWindow", "Lịch sử quyên góp"))
        self.exportBtn.setText(_translate("MainWindow", "Xuất file"))
        self.monthBtn.setText(_translate("MainWindow", "Trong tháng này ⌄"))
        self.txTitle1.setText(_translate("MainWindow", "Dự án xây trường cho em (vùng cao)"))
        self.txTime1.setText(_translate("MainWindow", "🗓 09:45:18  20/10/2025"))
        self.txAmount1.setText(_translate("MainWindow", "250,000"))
        self.txTitle2.setText(_translate("MainWindow", "Chương trình vì phụ nữ nghèo nông thôn"))
        self.txTime2.setText(_translate("MainWindow", "🗓 09:06:18  10/12/2025"))
        self.txAmount2.setText(_translate("MainWindow", "250,000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
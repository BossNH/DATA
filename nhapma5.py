

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 760)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 760))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 760))
        MainWindow.setStyleSheet("QMainWindow, QWidget {\n"
"    background: #FCEEF4;\n"
"    font-family: \"Segoe UI\";\n"
"    color: #3B2D35;\n"
"}\n"
"\n"
"QFrame#topBar {\n"
"    background: #F2D5E0;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 16px;\n"
"    padding: 6px 14px;\n"
"    background: transparent;\n"
"    color: #2F2A2E;\n"
"}\n"
"\n"
"QPushButton#activeNavBtn {\n"
"    background: #E8B8CF;\n"
"    color: #442C3E;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QPushButton#donateBtn {\n"
"    background: #E89BC5;\n"
"    color: white;\n"
"    font-weight: 700;\n"
"    border-radius: 18px;\n"
"    min-height: 34px;\n"
"}\n"
"\n"
"QPushButton#sendBtn {\n"
"    background: #E89BC5;\n"
"    color: white;\n"
"    font-weight: 700;\n"
"    border-radius: 14px;\n"
"    min-width: 70px;\n"
"    max-width: 70px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QFrame#campaignCard, QFrame#donateCard {\n"
"    background: #F9EFF3;\n"
"    border: 2px solid #F0B8CD;\n"
"    border-radius: 24px;\n"
"}\n"
"\n"
"QFrame#lineTop, QFrame#lineBottom, QFrame#lineVertical {\n"
"    background: #F0B8CD;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#titleLabel {\n"
"    color: #6A3C64;\n"
"    font-size: 26px;\n"
"    font-weight: 800;\n"
"}\n"
"\n"
"QLabel#descLabel {\n"
"    color: #2F2A2E;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLabel#amountLabel, QLabel#percentLabel {\n"
"    color: #6A4568;\n"
"    font-size: 22px;\n"
"    font-weight: 800;\n"
"}\n"
"\n"
"QLabel#sectionTitle, QLabel#ownerTitle, QLabel#donateTitle {\n"
"    color: #442C3E;\n"
"    font-size: 16px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QLabel#fieldTitle {\n"
"    color: #442C3E;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"QLabel#fieldValue {\n"
"    color: #3F3740;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLabel#logoText {\n"
"    color: #8B3F80;\n"
"    font-size: 24px;\n"
"    font-weight: 800;\n"
"}\n"
"\n"
"QLabel#logoSubText {\n"
"    color: #9B7284;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QLabel#backLabel {\n"
"    color: #1F1B1D;\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QLineEdit#transactionEdit {\n"
"    background: white;\n"
"    border: 1px solid #CDA8B7;\n"
"    border-radius: 18px;\n"
"    padding: 9px 14px;\n"
"    color: #4A4046;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background: #F3DDE8;\n"
"    border: none;\n"
"    border-radius: 14px;\n"
"    text-align: center;\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background: #E9A4CF;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"QLabel#avatarLabel, QLabel#qrLabel {\n"
"    background: #E7EEF6;\n"
"    border: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(18, 18, 18, 18)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topBar = QtWidgets.QFrame(parent=self.centralwidget)
        self.topBar.setMinimumSize(QtCore.QSize(0, 54))
        self.topBar.setMaximumSize(QtCore.QSize(16777215, 54))
        self.topBar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.topBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.topBar.setObjectName("topBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topBar)
        self.horizontalLayout.setContentsMargins(16, 8, 16, 8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logoLayout = QtWidgets.QHBoxLayout()
        self.logoLayout.setSpacing(6)
        self.logoLayout.setObjectName("logoLayout")
        self.logoIcon = QtWidgets.QLabel(parent=self.topBar)
        self.logoIcon.setMinimumSize(QtCore.QSize(36, 36))
        self.logoIcon.setMaximumSize(QtCore.QSize(36, 36))
        self.logoIcon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logoIcon.setObjectName("logoIcon")
        self.logoLayout.addWidget(self.logoIcon)
        self.logoTextLayout = QtWidgets.QVBoxLayout()
        self.logoTextLayout.setSpacing(0)
        self.logoTextLayout.setObjectName("logoTextLayout")
        self.logoText = QtWidgets.QLabel(parent=self.topBar)
        self.logoText.setObjectName("logoText")
        self.logoTextLayout.addWidget(self.logoText)
        self.logoSubText = QtWidgets.QLabel(parent=self.topBar)
        self.logoSubText.setObjectName("logoSubText")
        self.logoTextLayout.addWidget(self.logoSubText)
        self.logoLayout.addLayout(self.logoTextLayout)
        self.horizontalLayout.addLayout(self.logoLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.activeNavBtn = QtWidgets.QPushButton(parent=self.topBar)
        self.activeNavBtn.setObjectName("activeNavBtn")
        self.horizontalLayout.addWidget(self.activeNavBtn)
        self.statsBtn = QtWidgets.QPushButton(parent=self.topBar)
        self.statsBtn.setObjectName("statsBtn")
        self.horizontalLayout.addWidget(self.statsBtn)
        self.chatBtn = QtWidgets.QPushButton(parent=self.topBar)
        self.chatBtn.setObjectName("chatBtn")
        self.horizontalLayout.addWidget(self.chatBtn)
        self.publicBtn = QtWidgets.QPushButton(parent=self.topBar)
        self.publicBtn.setObjectName("publicBtn")
        self.horizontalLayout.addWidget(self.publicBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.notifyLabel = QtWidgets.QLabel(parent=self.topBar)
        self.notifyLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.notifyLabel.setObjectName("notifyLabel")
        self.horizontalLayout.addWidget(self.notifyLabel)
        self.settingsLabel = QtWidgets.QLabel(parent=self.topBar)
        self.settingsLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.settingsLabel.setObjectName("settingsLabel")
        self.horizontalLayout.addWidget(self.settingsLabel)
        self.profileLabel = QtWidgets.QLabel(parent=self.topBar)
        self.profileLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.profileLabel.setObjectName("profileLabel")
        self.horizontalLayout.addWidget(self.profileLabel)
        self.verticalLayout_2.addWidget(self.topBar)
        self.bodyWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.bodyWidget.setObjectName("bodyWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.bodyWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.backLabel = QtWidgets.QLabel(parent=self.bodyWidget)
        self.backLabel.setObjectName("backLabel")
        self.verticalLayout.addWidget(self.backLabel)
        self.campaignCard = QtWidgets.QFrame(parent=self.bodyWidget)
        self.campaignCard.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.campaignCard.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.campaignCard.setObjectName("campaignCard")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.campaignCard)
        self.verticalLayout_3.setContentsMargins(18, 12, 18, 12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titleLabel = QtWidgets.QLabel(parent=self.campaignCard)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_3.addWidget(self.titleLabel)
        self.descLabel = QtWidgets.QLabel(parent=self.campaignCard)
        self.descLabel.setWordWrap(True)
        self.descLabel.setObjectName("descLabel")
        self.verticalLayout_3.addWidget(self.descLabel)
        self.lineTop = QtWidgets.QFrame(parent=self.campaignCard)
        self.lineTop.setMinimumSize(QtCore.QSize(0, 4))
        self.lineTop.setMaximumSize(QtCore.QSize(16777215, 4))
        self.lineTop.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lineTop.setObjectName("lineTop")
        self.verticalLayout_3.addWidget(self.lineTop)
        self.amountLayout = QtWidgets.QHBoxLayout()
        self.amountLayout.setContentsMargins(18, 8, 18, 0)
        self.amountLayout.setObjectName("amountLayout")
        self.amountLabel = QtWidgets.QLabel(parent=self.campaignCard)
        self.amountLabel.setObjectName("amountLabel")
        self.amountLayout.addWidget(self.amountLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.amountLayout.addItem(spacerItem2)
        self.percentLabel = QtWidgets.QLabel(parent=self.campaignCard)
        self.percentLabel.setObjectName("percentLabel")
        self.amountLayout.addWidget(self.percentLabel)
        self.verticalLayout_3.addLayout(self.amountLayout)
        self.progressBar = QtWidgets.QProgressBar(parent=self.campaignCard)
        self.progressBar.setProperty("value", 33)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.lineBottom = QtWidgets.QFrame(parent=self.campaignCard)
        self.lineBottom.setMinimumSize(QtCore.QSize(0, 2))
        self.lineBottom.setMaximumSize(QtCore.QSize(16777215, 2))
        self.lineBottom.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lineBottom.setObjectName("lineBottom")
        self.verticalLayout_3.addWidget(self.lineBottom)
        self.detailLayout = QtWidgets.QHBoxLayout()
        self.detailLayout.setSpacing(16)
        self.detailLayout.setObjectName("detailLayout")
        self.leftInfoWidget = QtWidgets.QWidget(parent=self.campaignCard)
        self.leftInfoWidget.setObjectName("leftInfoWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.leftInfoWidget)
        self.verticalLayout_4.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sectionTitle = QtWidgets.QLabel(parent=self.leftInfoWidget)
        self.sectionTitle.setObjectName("sectionTitle")
        self.verticalLayout_4.addWidget(self.sectionTitle)
        self.activitiesText = QtWidgets.QLabel(parent=self.leftInfoWidget)
        self.activitiesText.setWordWrap(True)
        self.activitiesText.setObjectName("activitiesText")
        self.verticalLayout_4.addWidget(self.activitiesText)
        spacerItem3 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_4.addItem(spacerItem3)
        self.fieldTitle_scope = QtWidgets.QLabel(parent=self.leftInfoWidget)
        self.fieldTitle_scope.setStyleSheet("color:#442C3E;font-size:16px;font-weight:700;")
        self.fieldTitle_scope.setObjectName("fieldTitle_scope")
        self.verticalLayout_4.addWidget(self.fieldTitle_scope)
        self.scopeText = QtWidgets.QLabel(parent=self.leftInfoWidget)
        self.scopeText.setObjectName("scopeText")
        self.verticalLayout_4.addWidget(self.scopeText)
        self.fieldTitle_date = QtWidgets.QLabel(parent=self.leftInfoWidget)
        self.fieldTitle_date.setStyleSheet("color:#442C3E;font-size:16px;font-weight:700;")
        self.fieldTitle_date.setObjectName("fieldTitle_date")
        self.verticalLayout_4.addWidget(self.fieldTitle_date)
        self.dateText = QtWidgets.QLabel(parent=self.leftInfoWidget)
        self.dateText.setObjectName("dateText")
        self.verticalLayout_4.addWidget(self.dateText)
        self.detailLayout.addWidget(self.leftInfoWidget)
        self.lineVertical = QtWidgets.QFrame(parent=self.campaignCard)
        self.lineVertical.setMinimumSize(QtCore.QSize(2, 0))
        self.lineVertical.setMaximumSize(QtCore.QSize(2, 16777215))
        self.lineVertical.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lineVertical.setObjectName("lineVertical")
        self.detailLayout.addWidget(self.lineVertical)
        self.ownerInfoWidget = QtWidgets.QWidget(parent=self.campaignCard)
        self.ownerInfoWidget.setObjectName("ownerInfoWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ownerInfoWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(16)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ownerTextLayout = QtWidgets.QVBoxLayout()
        self.ownerTextLayout.setSpacing(6)
        self.ownerTextLayout.setObjectName("ownerTextLayout")
        self.ownerTitle = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.ownerTitle.setObjectName("ownerTitle")
        self.ownerTextLayout.addWidget(self.ownerTitle)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.labelIdTitle = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelIdTitle.setStyleSheet("color:#4B4147;font-size:14px;")
        self.labelIdTitle.setObjectName("labelIdTitle")
        self.gridLayout.addWidget(self.labelIdTitle, 0, 0, 1, 1)
        self.labelIdValue = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelIdValue.setStyleSheet("color:#3F3740;font-size:14px;")
        self.labelIdValue.setObjectName("labelIdValue")
        self.gridLayout.addWidget(self.labelIdValue, 0, 1, 1, 1)
        self.labelGenderTitle = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelGenderTitle.setStyleSheet("color:#4B4147;font-size:14px;")
        self.labelGenderTitle.setObjectName("labelGenderTitle")
        self.gridLayout.addWidget(self.labelGenderTitle, 0, 2, 1, 1)
        self.labelGenderValue = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelGenderValue.setStyleSheet("color:#3F3740;font-size:14px;")
        self.labelGenderValue.setObjectName("labelGenderValue")
        self.gridLayout.addWidget(self.labelGenderValue, 0, 3, 1, 1)
        self.labelNameTitle = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelNameTitle.setStyleSheet("color:#4B4147;font-size:14px;")
        self.labelNameTitle.setObjectName("labelNameTitle")
        self.gridLayout.addWidget(self.labelNameTitle, 1, 0, 1, 1)
        self.labelNameValue = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelNameValue.setStyleSheet("color:#3F3740;font-size:14px;")
        self.labelNameValue.setObjectName("labelNameValue")
        self.gridLayout.addWidget(self.labelNameValue, 1, 1, 1, 3)
        self.labelPhoneTitle = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelPhoneTitle.setStyleSheet("color:#4B4147;font-size:14px;")
        self.labelPhoneTitle.setObjectName("labelPhoneTitle")
        self.gridLayout.addWidget(self.labelPhoneTitle, 2, 0, 1, 1)
        self.labelPhoneValue = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelPhoneValue.setStyleSheet("color:#3F3740;font-size:14px;")
        self.labelPhoneValue.setObjectName("labelPhoneValue")
        self.gridLayout.addWidget(self.labelPhoneValue, 2, 1, 1, 3)
        self.labelCccdTitle = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelCccdTitle.setStyleSheet("color:#4B4147;font-size:14px;")
        self.labelCccdTitle.setObjectName("labelCccdTitle")
        self.gridLayout.addWidget(self.labelCccdTitle, 3, 0, 1, 1)
        self.labelCccdValue = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelCccdValue.setStyleSheet("color:#3F3740;font-size:14px;")
        self.labelCccdValue.setObjectName("labelCccdValue")
        self.gridLayout.addWidget(self.labelCccdValue, 3, 1, 1, 3)
        self.labelAddressTitle = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelAddressTitle.setStyleSheet("color:#4B4147;font-size:14px;")
        self.labelAddressTitle.setObjectName("labelAddressTitle")
        self.gridLayout.addWidget(self.labelAddressTitle, 4, 0, 1, 1)
        self.labelAddressValue = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelAddressValue.setStyleSheet("color:#3F3740;font-size:14px;")
        self.labelAddressValue.setObjectName("labelAddressValue")
        self.gridLayout.addWidget(self.labelAddressValue, 4, 1, 1, 3)
        self.labelEmailTitle = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelEmailTitle.setStyleSheet("color:#4B4147;font-size:14px;")
        self.labelEmailTitle.setObjectName("labelEmailTitle")
        self.gridLayout.addWidget(self.labelEmailTitle, 5, 0, 1, 1)
        self.labelEmailValue = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.labelEmailValue.setStyleSheet("color:#3F3740;font-size:14px;")
        self.labelEmailValue.setObjectName("labelEmailValue")
        self.gridLayout.addWidget(self.labelEmailValue, 5, 1, 1, 3)
        self.ownerTextLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.ownerTextLayout)
        self.avatarLabel = QtWidgets.QLabel(parent=self.ownerInfoWidget)
        self.avatarLabel.setMinimumSize(QtCore.QSize(170, 190))
        self.avatarLabel.setMaximumSize(QtCore.QSize(170, 190))
        self.avatarLabel.setText("")
        self.avatarLabel.setScaledContents(True)
        self.avatarLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.avatarLabel.setObjectName("avatarLabel")
        self.horizontalLayout_2.addWidget(self.avatarLabel)
        self.detailLayout.addWidget(self.ownerInfoWidget)
        self.verticalLayout_3.addLayout(self.detailLayout)
        self.verticalLayout.addWidget(self.campaignCard)
        self.donateCard = QtWidgets.QFrame(parent=self.bodyWidget)
        self.donateCard.setMinimumSize(QtCore.QSize(0, 180))
        self.donateCard.setMaximumSize(QtCore.QSize(480, 200))
        self.donateCard.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.donateCard.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.donateCard.setObjectName("donateCard")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.donateCard)
        self.horizontalLayout_3.setContentsMargins(22, 16, 22, 16)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.donateLeftLayout = QtWidgets.QVBoxLayout()
        self.donateLeftLayout.setSpacing(8)
        self.donateLeftLayout.setObjectName("donateLeftLayout")
        self.donateTitle = QtWidgets.QLabel(parent=self.donateCard)
        self.donateTitle.setStyleSheet("color:#7A3E6A;font-size:28px;font-weight:800;")
        self.donateTitle.setObjectName("donateTitle")
        self.donateLeftLayout.addWidget(self.donateTitle)
        self.transactionLabel = QtWidgets.QLabel(parent=self.donateCard)
        self.transactionLabel.setObjectName("transactionLabel")
        self.donateLeftLayout.addWidget(self.transactionLabel)
        self.transactionEdit = QtWidgets.QLineEdit(parent=self.donateCard)
        self.transactionEdit.setMinimumSize(QtCore.QSize(170, 40))
        self.transactionEdit.setObjectName("transactionEdit")
        self.donateLeftLayout.addWidget(self.transactionEdit)
        self.sendBtn = QtWidgets.QPushButton(parent=self.donateCard)
        self.sendBtn.setObjectName("sendBtn")
        self.donateLeftLayout.addWidget(self.sendBtn)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.donateLeftLayout.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.donateLeftLayout)
        self.qrLabel = QtWidgets.QLabel(parent=self.donateCard)
        self.qrLabel.setMinimumSize(QtCore.QSize(125, 125))
        self.qrLabel.setMaximumSize(QtCore.QSize(125, 125))
        self.qrLabel.setText("")
        self.qrLabel.setScaledContents(True)
        self.qrLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qrLabel.setObjectName("qrLabel")
        self.horizontalLayout_3.addWidget(self.qrLabel)
        self.verticalLayout.addWidget(self.donateCard)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.bodyWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self._load_images()
        self.sendBtn.clicked.connect(self._handle_send_transaction)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Donarity - Chi tiết chiến dịch"))
        self.logoIcon.setText(_translate("MainWindow", "🤍"))
        self.logoText.setText(_translate("MainWindow", "Donarity"))
        self.logoSubText.setText(_translate("MainWindow", "by group 10"))
        self.activeNavBtn.setText(_translate("MainWindow", "🏠 Trang chủ"))
        self.statsBtn.setText(_translate("MainWindow", "⌛ Thống kê"))
        self.chatBtn.setText(_translate("MainWindow", "🗨️ Chatbot"))
        self.publicBtn.setText(_translate("MainWindow", "👁️ Công khai"))
        self.notifyLabel.setText(_translate("MainWindow", "🔔"))
        self.settingsLabel.setText(_translate("MainWindow", "⚙️"))
        self.profileLabel.setText(_translate("MainWindow", "👤"))
        self.backLabel.setText(_translate("MainWindow", "← Quay lại"))
        self.titleLabel.setText(_translate("MainWindow", "Saigon Children's Charity (Học bổng giáo dục)"))
        self.descLabel.setText(_translate("MainWindow", "Giúp trẻ em có hoàn cảnh khó khăn tiếp cận giáo dục chất lượng để vượt qua nghèo đói và phát triển tương lai."))
        self.amountLabel.setText(_translate("MainWindow", "1000000000/7000000000"))
        self.percentLabel.setText(_translate("MainWindow", "6.67%"))
        self.sectionTitle.setText(_translate("MainWindow", "Hoạt động:"))
        self.activitiesText.setText(_translate("MainWindow", "Trao học bổng dài hạn cho trẻ em nghèo\nXây dựng và cải tạo trường học\nĐào tạo nghề cho thanh thiếu niên khó khăn"))
        self.fieldTitle_scope.setText(_translate("MainWindow", "Phạm vi:"))
        self.scopeText.setText(_translate("MainWindow", "Miền Nam Việt Nam"))
        self.fieldTitle_date.setText(_translate("MainWindow", "Ngày thành lập:"))
        self.dateText.setText(_translate("MainWindow", "1992-05-20"))
        self.ownerTitle.setText(_translate("MainWindow", "Chủ chiến dịch:"))
        self.labelIdTitle.setText(_translate("MainWindow", "ID:"))
        self.labelIdValue.setText(_translate("MainWindow", "CC0009"))
        self.labelGenderTitle.setText(_translate("MainWindow", "Giới tính:"))
        self.labelGenderValue.setText(_translate("MainWindow", "Nam"))
        self.labelNameTitle.setText(_translate("MainWindow", "Họ và tên:"))
        self.labelNameValue.setText(_translate("MainWindow", "Damien Roberts"))
        self.labelPhoneTitle.setText(_translate("MainWindow", "Số điện thoại:"))
        self.labelPhoneValue.setText(_translate("MainWindow", "0901333009"))
        self.labelCccdTitle.setText(_translate("MainWindow", "Số CCCD:"))
        self.labelCccdValue.setText(_translate("MainWindow", "079080007777"))
        self.labelAddressTitle.setText(_translate("MainWindow", "Địa chỉ:"))
        self.labelAddressValue.setText(_translate("MainWindow", "Hồ Chí Minh"))
        self.labelEmailTitle.setText(_translate("MainWindow", "Email:"))
        self.labelEmailValue.setText(_translate("MainWindow", "damien@gmail.com"))
        self.donateTitle.setText(_translate("MainWindow", "Quyên góp"))
        self.transactionLabel.setText(_translate("MainWindow", "Mã giao dịch"))
        self.transactionEdit.setPlaceholderText(_translate("MainWindow", "Nhập mã giao dịch"))
        self.sendBtn.setText(_translate("MainWindow", "Gửi"))

    def _load_images(self):
        avatar = QtGui.QPixmap("avt5")
        if not avatar.isNull():
            self.avatarLabel.setPixmap(avatar)
        qr = QtGui.QPixmap("qr5")
        if not qr.isNull():
            self.qrLabel.setPixmap(qr)

    def _handle_send_transaction(self):
        transaction_code = self.transactionEdit.text().strip()
        if transaction_code:
            QtWidgets.QMessageBox.information(
                self.sendBtn.window(),
                "Thông báo",
                "Đã gửi thành công"
            )
            self.transactionEdit.clear()
        else:
            QtWidgets.QMessageBox.warning(
                self.sendBtn.window(),
                "Thông báo",
                "Hãy nhập mã giao dịch"
            )



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

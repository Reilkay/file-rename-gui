# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(746, 463)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.select_list = QListView(self.centralwidget)
        self.select_list.setObjectName(u"select_list")
        self.select_list.setMinimumSize(QSize(340, 0))

        self.gridLayout.addWidget(self.select_list, 6, 3, 1, 1)

        self.suffix_layout = QHBoxLayout()
        self.suffix_layout.setObjectName(u"suffix_layout")
        self.suffix_box = QGroupBox(self.centralwidget)
        self.suffix_box.setObjectName(u"suffix_box")
        self.horizontalLayout_5 = QHBoxLayout(self.suffix_box)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.suffix_false = QRadioButton(self.suffix_box)
        self.suffix_false.setObjectName(u"suffix_false")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suffix_false.sizePolicy().hasHeightForWidth())
        self.suffix_false.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.suffix_false)

        self.suffix_true = QRadioButton(self.suffix_box)
        self.suffix_true.setObjectName(u"suffix_true")
        sizePolicy.setHeightForWidth(self.suffix_true.sizePolicy().hasHeightForWidth())
        self.suffix_true.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.suffix_true)

        self.suffix = QLineEdit(self.suffix_box)
        self.suffix.setObjectName(u"suffix")
        sizePolicy.setHeightForWidth(self.suffix.sizePolicy().hasHeightForWidth())
        self.suffix.setSizePolicy(sizePolicy)
        self.suffix.setMaximumSize(QSize(300, 400))

        self.horizontalLayout_5.addWidget(self.suffix)


        self.suffix_layout.addWidget(self.suffix_box)


        self.gridLayout.addLayout(self.suffix_layout, 8, 3, 1, 1)

        self.control_layout = QHBoxLayout()
        self.control_layout.setObjectName(u"control_layout")
        self.name_box = QGroupBox(self.centralwidget)
        self.name_box.setObjectName(u"name_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name_box.sizePolicy().hasHeightForWidth())
        self.name_box.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.name_box)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.name_layout = QHBoxLayout()
        self.name_layout.setObjectName(u"name_layout")
        self.name_label = QLabel(self.name_box)
        self.name_label.setObjectName(u"name_label")

        self.name_layout.addWidget(self.name_label)

        self.name_input = QLineEdit(self.name_box)
        self.name_input.setObjectName(u"name_input")

        self.name_layout.addWidget(self.name_input)


        self.verticalLayout_5.addLayout(self.name_layout)

        self.no_layout = QHBoxLayout()
        self.no_layout.setObjectName(u"no_layout")
        self.no_label = QLabel(self.name_box)
        self.no_label.setObjectName(u"no_label")

        self.no_layout.addWidget(self.no_label)

        self.no_input = QLineEdit(self.name_box)
        self.no_input.setObjectName(u"no_input")

        self.no_layout.addWidget(self.no_input)


        self.verticalLayout_5.addLayout(self.no_layout)


        self.control_layout.addWidget(self.name_box)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.rename = QPushButton(self.centralwidget)
        self.rename.setObjectName(u"rename")

        self.verticalLayout.addWidget(self.rename)


        self.control_layout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.control_layout, 9, 1, 1, 3)

        self.nav_layout = QHBoxLayout()
        self.nav_layout.setObjectName(u"nav_layout")
        self.address = QLineEdit(self.centralwidget)
        self.address.setObjectName(u"address")

        self.nav_layout.addWidget(self.address)

        self.address_select = QPushButton(self.centralwidget)
        self.address_select.setObjectName(u"address_select")

        self.nav_layout.addWidget(self.address_select)


        self.gridLayout.addLayout(self.nav_layout, 0, 1, 1, 3)

        self.file_list = QListView(self.centralwidget)
        self.file_list.setObjectName(u"file_list")
        self.file_list.setMinimumSize(QSize(340, 0))

        self.gridLayout.addWidget(self.file_list, 6, 1, 1, 1)

        self.all_select_layout = QHBoxLayout()
        self.all_select_layout.setObjectName(u"all_select_layout")
        self.suffix_select = QComboBox(self.centralwidget)
        self.suffix_select.setObjectName(u"suffix_select")

        self.all_select_layout.addWidget(self.suffix_select)

        self.all_select = QPushButton(self.centralwidget)
        self.all_select.setObjectName(u"all_select")
        sizePolicy.setHeightForWidth(self.all_select.sizePolicy().hasHeightForWidth())
        self.all_select.setSizePolicy(sizePolicy)

        self.all_select_layout.addWidget(self.all_select)


        self.gridLayout.addLayout(self.all_select_layout, 1, 1, 1, 1)

        self.in_out_layout = QVBoxLayout()
        self.in_out_layout.setObjectName(u"in_out_layout")
        self.select_in = QPushButton(self.centralwidget)
        self.select_in.setObjectName(u"select_in")
        sizePolicy.setHeightForWidth(self.select_in.sizePolicy().hasHeightForWidth())
        self.select_in.setSizePolicy(sizePolicy)
        self.select_in.setMaximumSize(QSize(30, 30))

        self.in_out_layout.addWidget(self.select_in)

        self.select_out = QPushButton(self.centralwidget)
        self.select_out.setObjectName(u"select_out")
        sizePolicy.setHeightForWidth(self.select_out.sizePolicy().hasHeightForWidth())
        self.select_out.setSizePolicy(sizePolicy)
        self.select_out.setMaximumSize(QSize(30, 30))

        self.in_out_layout.addWidget(self.select_out)


        self.gridLayout.addLayout(self.in_out_layout, 6, 2, 1, 1)

        self.iteration_layout = QHBoxLayout()
        self.iteration_layout.setObjectName(u"iteration_layout")
        self.iteration_box = QGroupBox(self.centralwidget)
        self.iteration_box.setObjectName(u"iteration_box")
        self.horizontalLayout_3 = QHBoxLayout(self.iteration_box)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.iteration_false = QRadioButton(self.iteration_box)
        self.iteration_false.setObjectName(u"iteration_false")
        sizePolicy.setHeightForWidth(self.iteration_false.sizePolicy().hasHeightForWidth())
        self.iteration_false.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.iteration_false)

        self.iteration_true = QRadioButton(self.iteration_box)
        self.iteration_true.setObjectName(u"iteration_true")
        sizePolicy.setHeightForWidth(self.iteration_true.sizePolicy().hasHeightForWidth())
        self.iteration_true.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.iteration_true)


        self.iteration_layout.addWidget(self.iteration_box)


        self.gridLayout.addLayout(self.iteration_layout, 8, 1, 1, 1)

        self.file_number = QLabel(self.centralwidget)
        self.file_number.setObjectName(u"file_number")

        self.gridLayout.addWidget(self.file_number, 7, 1, 1, 1)

        self.select_number = QLabel(self.centralwidget)
        self.select_number.setObjectName(u"select_number")

        self.gridLayout.addWidget(self.select_number, 7, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.suffix_box.setTitle(QCoreApplication.translate("MainWindow", u"\u540e\u7f00", None))
        self.suffix_false.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u4fee\u6539\u540e\u7f00", None))
        self.suffix_true.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u540e\u7f00\u4e3a\uff1a", None))
        self.name_box.setTitle(QCoreApplication.translate("MainWindow", u"\u540d\u79f0\u8bbe\u7f6e", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d\u79f0", None))
        self.no_label.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u59cb\u5e8f\u6570", None))
        self.rename.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u91cd\u547d\u540d", None))
        self.address_select.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.all_select.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
        self.select_in.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.select_out.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.iteration_box.setTitle(QCoreApplication.translate("MainWindow", u"\u8fed\u4ee3\u6dfb\u52a0", None))
        self.iteration_false.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.iteration_true.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.file_number.setText(QCoreApplication.translate("MainWindow", u"\u603b\u8ba1\uff1a", None))
        self.select_number.setText(QCoreApplication.translate("MainWindow", u"\u603b\u8ba1\uff1a", None))
    # retranslateUi


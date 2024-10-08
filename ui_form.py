# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(790, 600))
        MainWindow.setMaximumSize(QSize(796, 612))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(796, 612))
        self.centralwidget.setMaximumSize(QSize(796, 612))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, -10, 822, 621))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(800, 600))
        self.verticalLayoutWidget_2 = QWidget(self.widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(150, 500, 502, 81))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(500, 40))
        self.lineEdit.setStyleSheet(u"background-color: rgb(249, 240, 107);")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchButton = QPushButton(self.verticalLayoutWidget_2)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setStyleSheet(u"border-color: rgb(220, 138, 221);")

        self.horizontalLayout_2.addWidget(self.searchButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.w_desc = QLabel(self.widget)
        self.w_desc.setObjectName(u"w_desc")
        self.w_desc.setGeometry(QRect(390, 60, 320, 30))
        self.w_desc.setMaximumSize(QSize(750, 50))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        self.w_desc.setFont(font)
        self.w_desc.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.city_label = QLabel(self.widget)
        self.city_label.setObjectName(u"city_label")
        self.city_label.setGeometry(QRect(30, 0, 741, 50))
        sizePolicy.setHeightForWidth(self.city_label.sizePolicy().hasHeightForWidth())
        self.city_label.setSizePolicy(sizePolicy)
        self.city_label.setMaximumSize(QSize(750, 50))
        font1 = QFont()
        font1.setFamilies([u"Titillium Web"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.city_label.setFont(font1)
        self.city_label.setLayoutDirection(Qt.LeftToRight)
        self.city_label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.city_label.setAlignment(Qt.AlignCenter)
        self.w_icon = QLabel(self.widget)
        self.w_icon.setObjectName(u"w_icon")
        self.w_icon.setGeometry(QRect(260, 50, 50, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.w_icon.sizePolicy().hasHeightForWidth())
        self.w_icon.setSizePolicy(sizePolicy1)
        self.w_icon.setMaximumSize(QSize(50, 50))
        self.w_icon.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.temp = QLabel(self.widget)
        self.temp.setObjectName(u"temp")
        self.temp.setGeometry(QRect(310, 60, 80, 30))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.temp.sizePolicy().hasHeightForWidth())
        self.temp.setSizePolicy(sizePolicy2)
        self.temp.setMaximumSize(QSize(80, 30))
        self.temp.setFont(font)
        self.temp.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.temp.setAlignment(Qt.AlignCenter)
        self.temp.setMargin(0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 120, 751, 371))
        self.gridLayoutWidget = QWidget(self.widget_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 731, 351))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.day4_nine = QLabel(self.gridLayoutWidget)
        self.day4_nine.setObjectName(u"day4_nine")

        self.gridLayout.addWidget(self.day4_nine, 4, 5, 1, 1)

        self.day4_twelve = QLabel(self.gridLayoutWidget)
        self.day4_twelve.setObjectName(u"day4_twelve")

        self.gridLayout.addWidget(self.day4_twelve, 4, 6, 1, 1)

        self.Day_3 = QLabel(self.gridLayoutWidget)
        self.Day_3.setObjectName(u"Day_3")
        font2 = QFont()
        font2.setFamilies([u"URW Gothic"])
        font2.setPointSize(13)
        font2.setBold(False)
        self.Day_3.setFont(font2)
        self.Day_3.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.Day_3, 3, 0, 1, 1)

        self.day2_six = QLabel(self.gridLayoutWidget)
        self.day2_six.setObjectName(u"day2_six")

        self.gridLayout.addWidget(self.day2_six, 2, 4, 1, 1)

        self.day5_three = QLabel(self.gridLayoutWidget)
        self.day5_three.setObjectName(u"day5_three")

        self.gridLayout.addWidget(self.day5_three, 5, 3, 1, 1)

        self.Day_1 = QLabel(self.gridLayoutWidget)
        self.Day_1.setObjectName(u"Day_1")
        self.Day_1.setFont(font2)
        self.Day_1.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.Day_1, 1, 0, 1, 1)

        self.day3_eighteen = QLabel(self.gridLayoutWidget)
        self.day3_eighteen.setObjectName(u"day3_eighteen")

        self.gridLayout.addWidget(self.day3_eighteen, 3, 8, 1, 1)

        self.twelve = QLabel(self.gridLayoutWidget)
        self.twelve.setObjectName(u"twelve")
        font3 = QFont()
        font3.setFamilies([u"URW Gothic"])
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        self.twelve.setFont(font3)
        self.twelve.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.twelve, 0, 6, 1, 1)

        self.twentyone = QLabel(self.gridLayoutWidget)
        self.twentyone.setObjectName(u"twentyone")
        self.twentyone.setFont(font3)
        self.twentyone.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.twentyone, 0, 9, 1, 1)

        self.Day_4 = QLabel(self.gridLayoutWidget)
        self.Day_4.setObjectName(u"Day_4")
        self.Day_4.setFont(font2)
        self.Day_4.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.Day_4, 4, 0, 1, 1)

        self.day1_nine = QLabel(self.gridLayoutWidget)
        self.day1_nine.setObjectName(u"day1_nine")

        self.gridLayout.addWidget(self.day1_nine, 1, 5, 1, 1)

        self.day1_three = QLabel(self.gridLayoutWidget)
        self.day1_three.setObjectName(u"day1_three")

        self.gridLayout.addWidget(self.day1_three, 1, 3, 1, 1)

        self.day2_three = QLabel(self.gridLayoutWidget)
        self.day2_three.setObjectName(u"day2_three")

        self.gridLayout.addWidget(self.day2_three, 2, 3, 1, 1)

        self.day4_eighteen = QLabel(self.gridLayoutWidget)
        self.day4_eighteen.setObjectName(u"day4_eighteen")

        self.gridLayout.addWidget(self.day4_eighteen, 4, 8, 1, 1)

        self.day2_midnight = QLabel(self.gridLayoutWidget)
        self.day2_midnight.setObjectName(u"day2_midnight")

        self.gridLayout.addWidget(self.day2_midnight, 2, 2, 1, 1)

        self.Day_5 = QLabel(self.gridLayoutWidget)
        self.Day_5.setObjectName(u"Day_5")
        self.Day_5.setFont(font2)
        self.Day_5.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.Day_5, 5, 0, 1, 1)

        self.day5_twelve = QLabel(self.gridLayoutWidget)
        self.day5_twelve.setObjectName(u"day5_twelve")

        self.gridLayout.addWidget(self.day5_twelve, 5, 6, 1, 1)

        self.three = QLabel(self.gridLayoutWidget)
        self.three.setObjectName(u"three")
        self.three.setFont(font3)
        self.three.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.three, 0, 3, 1, 1)

        self.day2_twelve = QLabel(self.gridLayoutWidget)
        self.day2_twelve.setObjectName(u"day2_twelve")

        self.gridLayout.addWidget(self.day2_twelve, 2, 6, 1, 1)

        self.day4_twentyone = QLabel(self.gridLayoutWidget)
        self.day4_twentyone.setObjectName(u"day4_twentyone")

        self.gridLayout.addWidget(self.day4_twentyone, 4, 9, 1, 1)

        self.day4_three = QLabel(self.gridLayoutWidget)
        self.day4_three.setObjectName(u"day4_three")

        self.gridLayout.addWidget(self.day4_three, 4, 3, 1, 1)

        self.day1_twentyone = QLabel(self.gridLayoutWidget)
        self.day1_twentyone.setObjectName(u"day1_twentyone")

        self.gridLayout.addWidget(self.day1_twentyone, 1, 9, 1, 1)

        self.day5_fifteen = QLabel(self.gridLayoutWidget)
        self.day5_fifteen.setObjectName(u"day5_fifteen")

        self.gridLayout.addWidget(self.day5_fifteen, 5, 7, 1, 1)

        self.day2_eighteen = QLabel(self.gridLayoutWidget)
        self.day2_eighteen.setObjectName(u"day2_eighteen")

        self.gridLayout.addWidget(self.day2_eighteen, 2, 8, 1, 1)

        self.day3_nine = QLabel(self.gridLayoutWidget)
        self.day3_nine.setObjectName(u"day3_nine")

        self.gridLayout.addWidget(self.day3_nine, 3, 5, 1, 1)

        self.day3_twelve = QLabel(self.gridLayoutWidget)
        self.day3_twelve.setObjectName(u"day3_twelve")

        self.gridLayout.addWidget(self.day3_twelve, 3, 6, 1, 1)

        self.day4_fifteen = QLabel(self.gridLayoutWidget)
        self.day4_fifteen.setObjectName(u"day4_fifteen")

        self.gridLayout.addWidget(self.day4_fifteen, 4, 7, 1, 1)

        self.day1_twelve = QLabel(self.gridLayoutWidget)
        self.day1_twelve.setObjectName(u"day1_twelve")

        self.gridLayout.addWidget(self.day1_twelve, 1, 6, 1, 1)

        self.eighteen = QLabel(self.gridLayoutWidget)
        self.eighteen.setObjectName(u"eighteen")
        self.eighteen.setFont(font3)
        self.eighteen.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.eighteen, 0, 8, 1, 1)

        self.day5_six = QLabel(self.gridLayoutWidget)
        self.day5_six.setObjectName(u"day5_six")

        self.gridLayout.addWidget(self.day5_six, 5, 4, 1, 1)

        self.day3_fifteen = QLabel(self.gridLayoutWidget)
        self.day3_fifteen.setObjectName(u"day3_fifteen")

        self.gridLayout.addWidget(self.day3_fifteen, 3, 7, 1, 1)

        self.six = QLabel(self.gridLayoutWidget)
        self.six.setObjectName(u"six")
        self.six.setFont(font3)
        self.six.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.six, 0, 4, 1, 1)

        self.day3_twentyone = QLabel(self.gridLayoutWidget)
        self.day3_twentyone.setObjectName(u"day3_twentyone")

        self.gridLayout.addWidget(self.day3_twentyone, 3, 9, 1, 1)

        self.fifteen = QLabel(self.gridLayoutWidget)
        self.fifteen.setObjectName(u"fifteen")
        self.fifteen.setFont(font3)
        self.fifteen.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.fifteen, 0, 7, 1, 1)

        self.day1_six = QLabel(self.gridLayoutWidget)
        self.day1_six.setObjectName(u"day1_six")

        self.gridLayout.addWidget(self.day1_six, 1, 4, 1, 1)

        self.day4_midnight = QLabel(self.gridLayoutWidget)
        self.day4_midnight.setObjectName(u"day4_midnight")

        self.gridLayout.addWidget(self.day4_midnight, 4, 2, 1, 1)

        self.day5_twentyone = QLabel(self.gridLayoutWidget)
        self.day5_twentyone.setObjectName(u"day5_twentyone")

        self.gridLayout.addWidget(self.day5_twentyone, 5, 9, 1, 1)

        self.day3_midnight = QLabel(self.gridLayoutWidget)
        self.day3_midnight.setObjectName(u"day3_midnight")

        self.gridLayout.addWidget(self.day3_midnight, 3, 2, 1, 1)

        self.day5_eighteen = QLabel(self.gridLayoutWidget)
        self.day5_eighteen.setObjectName(u"day5_eighteen")

        self.gridLayout.addWidget(self.day5_eighteen, 5, 8, 1, 1)

        self.day4_six = QLabel(self.gridLayoutWidget)
        self.day4_six.setObjectName(u"day4_six")

        self.gridLayout.addWidget(self.day4_six, 4, 4, 1, 1)

        self.day5_midnight = QLabel(self.gridLayoutWidget)
        self.day5_midnight.setObjectName(u"day5_midnight")

        self.gridLayout.addWidget(self.day5_midnight, 5, 2, 1, 1)

        self.none = QLabel(self.gridLayoutWidget)
        self.none.setObjectName(u"none")

        self.gridLayout.addWidget(self.none, 0, 0, 1, 1)

        self.nine = QLabel(self.gridLayoutWidget)
        self.nine.setObjectName(u"nine")
        self.nine.setFont(font3)
        self.nine.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.nine, 0, 5, 1, 1)

        self.day3_three = QLabel(self.gridLayoutWidget)
        self.day3_three.setObjectName(u"day3_three")

        self.gridLayout.addWidget(self.day3_three, 3, 3, 1, 1)

        self.Day_2 = QLabel(self.gridLayoutWidget)
        self.Day_2.setObjectName(u"Day_2")
        self.Day_2.setFont(font2)
        self.Day_2.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.Day_2, 2, 0, 1, 1)

        self.day1_midnight = QLabel(self.gridLayoutWidget)
        self.day1_midnight.setObjectName(u"day1_midnight")
        self.day1_midnight.setStyleSheet(u"")

        self.gridLayout.addWidget(self.day1_midnight, 1, 2, 1, 1)

        self.day2_fifteen = QLabel(self.gridLayoutWidget)
        self.day2_fifteen.setObjectName(u"day2_fifteen")

        self.gridLayout.addWidget(self.day2_fifteen, 2, 7, 1, 1)

        self.day2_twentyone = QLabel(self.gridLayoutWidget)
        self.day2_twentyone.setObjectName(u"day2_twentyone")

        self.gridLayout.addWidget(self.day2_twentyone, 2, 9, 1, 1)

        self.day3_six = QLabel(self.gridLayoutWidget)
        self.day3_six.setObjectName(u"day3_six")

        self.gridLayout.addWidget(self.day3_six, 3, 4, 1, 1)

        self.day5_nine = QLabel(self.gridLayoutWidget)
        self.day5_nine.setObjectName(u"day5_nine")

        self.gridLayout.addWidget(self.day5_nine, 5, 5, 1, 1)

        self.day1_fifteen = QLabel(self.gridLayoutWidget)
        self.day1_fifteen.setObjectName(u"day1_fifteen")

        self.gridLayout.addWidget(self.day1_fifteen, 1, 7, 1, 1)

        self.day2_nine = QLabel(self.gridLayoutWidget)
        self.day2_nine.setObjectName(u"day2_nine")

        self.gridLayout.addWidget(self.day2_nine, 2, 5, 1, 1)

        self.midnight = QLabel(self.gridLayoutWidget)
        self.midnight.setObjectName(u"midnight")
        font4 = QFont()
        font4.setFamilies([u"URW Gothic"])
        font4.setPointSize(13)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setKerning(True)
        self.midnight.setFont(font4)
        self.midnight.setToolTipDuration(-1)
        self.midnight.setStyleSheet(u"color: rgb(246, 245, 244);")

        self.gridLayout.addWidget(self.midnight, 0, 2, 1, 1)

        self.day1_eighteen = QLabel(self.gridLayoutWidget)
        self.day1_eighteen.setObjectName(u"day1_eighteen")

        self.gridLayout.addWidget(self.day1_eighteen, 1, 8, 1, 1)

        self.animated_bg = QLabel(self.widget)
        self.animated_bg.setObjectName(u"animated_bg")
        self.animated_bg.setGeometry(QRect(-20, 0, 821, 621))
        self.animated_bg.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.w_desc.raise_()
        self.city_label.raise_()
        self.w_icon.raise_()
        self.temp.raise_()
        self.widget_2.raise_()

        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search a city..", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.w_desc.setText("")
        self.city_label.setText("")
        self.w_icon.setText("")
        self.temp.setText("")
        self.day4_nine.setText("")
        self.day4_twelve.setText("")
        self.Day_3.setText("")
        self.day2_six.setText("")
        self.day5_three.setText("")
        self.Day_1.setText("")
        self.day3_eighteen.setText("")
        self.twelve.setText("")
        self.twentyone.setText("")
        self.Day_4.setText("")
        self.day1_nine.setText("")
        self.day1_three.setText("")
        self.day2_three.setText("")
        self.day4_eighteen.setText("")
        self.day2_midnight.setText("")
        self.Day_5.setText("")
        self.day5_twelve.setText("")
        self.three.setText("")
        self.day2_twelve.setText("")
        self.day4_twentyone.setText("")
        self.day4_three.setText("")
        self.day1_twentyone.setText("")
        self.day5_fifteen.setText("")
        self.day2_eighteen.setText("")
        self.day3_nine.setText("")
        self.day3_twelve.setText("")
        self.day4_fifteen.setText("")
        self.day1_twelve.setText("")
        self.eighteen.setText("")
        self.day5_six.setText("")
        self.day3_fifteen.setText("")
        self.six.setText("")
        self.day3_twentyone.setText("")
        self.fifteen.setText("")
        self.day1_six.setText("")
        self.day4_midnight.setText("")
        self.day5_twentyone.setText("")
        self.day3_midnight.setText("")
        self.day5_eighteen.setText("")
        self.day4_six.setText("")
        self.day5_midnight.setText("")
        self.none.setText("")
        self.nine.setText("")
        self.day3_three.setText("")
        self.Day_2.setText("")
        self.day1_midnight.setText("")
        self.day2_fifteen.setText("")
        self.day2_twentyone.setText("")
        self.day3_six.setText("")
        self.day5_nine.setText("")
        self.day1_fifteen.setText("")
        self.day2_nine.setText("")
#if QT_CONFIG(tooltip)
        self.midnight.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.midnight.setText("")
        self.day1_eighteen.setText("")
        self.animated_bg.setText("")
    # retranslateUi


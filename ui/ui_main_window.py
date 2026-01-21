# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowuNagGC.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(640, 480))
        MainWindow.setMaximumSize(QSize(640, 480))
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3b3b3b;\n"
"    border: 1px solid #555;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4a4a4a;\n"
"    box-shadow: 0 4px 12px rgba(0,0,0,0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a2a2a;\n"
"    box-shadow: 0 2px 6px rgba(0,0,0,0.4);\n"
"}\n"
"\n"
"QLineEdit, QTextEdit {\n"
"    background-color: #3b3b3b;\n"
"    border: 2px solid #555;\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"    selection-background-color: #5a5a5a;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus {\n"
"    border-color: #66ccff;\n"
"    box-shadow: 0 0 8px rgba(102,204,255,0.3);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #e0e0e0;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #3b3b3b;\n"
"    border: 2px solid #555;\n"
"  "
                        "  border-radius: 6px;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 30px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #3b3b3b;\n"
"    border: 1px solid #555;\n"
"    selection-background-color: #5a5a5a;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Add_Button = QPushButton(self.centralwidget)
        self.Add_Button.setObjectName(u"Add_Button")
        self.Add_Button.setGeometry(QRect(545, 40, 86, 27))
        self.Price = QLineEdit(self.centralwidget)
        self.Price.setObjectName(u"Price")
        self.Price.setGeometry(QRect(366, 40, 159, 26))
        self.Price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Mileage = QLineEdit(self.centralwidget)
        self.Mileage.setObjectName(u"Mileage")
        self.Mileage.setGeometry(QRect(188, 40, 159, 26))
        self.Mileage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Name = QLineEdit(self.centralwidget)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(9, 40, 159, 26))
        sizePolicy.setHeightForWidth(self.Name.sizePolicy().hasHeightForWidth())
        self.Name.setSizePolicy(sizePolicy)
        self.Name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 10, 159, 26))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(188, 10, 159, 26))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(366, 10, 159, 26))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 80, 620, 311))
        self.Delete_Button = QPushButton(self.centralwidget)
        self.Delete_Button.setObjectName(u"Delete_Button")
        self.Delete_Button.setGeometry(QRect(545, 400, 86, 27))
        self.deleted_index = QLineEdit(self.centralwidget)
        self.deleted_index.setObjectName(u"deleted_index")
        self.deleted_index.setGeometry(QRect(366, 400, 159, 26))
        self.deleted_index.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.filtered_btn = QPushButton(self.centralwidget)
        self.filtered_btn.setObjectName(u"filtered_btn")
        self.filtered_btn.setGeometry(QRect(189, 400, 86, 27))
        self.filter = QLineEdit(self.centralwidget)
        self.filter.setObjectName(u"filter")
        self.filter.setGeometry(QRect(10, 400, 159, 26))
        self.filter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(295, 400, 50, 26))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Car Cost Controller", None))
        self.Add_Button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.Price.setInputMask("")
        self.Price.setText("")
        self.Mileage.setInputMask("")
        self.Mileage.setText("")
        self.Name.setInputMask("")
        self.Name.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0431\u0435\u0433", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.Delete_Button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.deleted_index.setInputMask("")
        self.deleted_index.setText("")
        self.filtered_btn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043a\u0430\u0442\u044c", None))
        self.filter.setInputMask("")
        self.filter.setText("")
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi


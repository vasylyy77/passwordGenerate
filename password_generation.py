# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,QFileDialog,
    QVBoxLayout, QWidget)
from random import choice
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(567, 562)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"padding:10;\n"
"font: 75 12pt \"Rubik\";\n"
"")
        self.file_path = ""

        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)
#lineEdit
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setPlaceholderText('Resurs')

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setPlaceholderText('Number')

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setPlaceholderText('Login')

        self.verticalLayout.addWidget(self.lineEdit_3)

# push
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.create_password)

        self.verticalLayout.addWidget(self.pushButton)

        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setPlaceholderText('Result')

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(self.save_password)

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Resurs", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Count symbols", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create password", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save result", None))
    # retranslateUi

    def create_password(self):
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
        resurs = self.lineEdit.text()
        number = self.lineEdit_2.text()
        login = self.lineEdit_3.text()
        len_password = int(number)
        entry_password = []
        for i in range(int(len_password)):
            entry_password.insert(0, choice(alphabet))

        self.lineEdit_4.setText(f"resurs: {resurs} password: {''.join(entry_password)} login: {login}""")
        return f""" 
         resurs: {resurs}
         password: {''.join(entry_password)} 
         login: {login}\n"""

    def save_password(self):
        if not self.file_path:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
            if not file_path:
                return
            self.file_path = file_path


        with open(self.file_path, 'a', encoding='utf-8') as file:
            text = self.create_password()
            print(text)
            file.write(text)






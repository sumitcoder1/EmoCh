# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PySide2 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(350, 350)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.ProgressBar = QtWidgets.QFrame(self.centralwidget)
        self.ProgressBar.setGeometry(QtCore.QRect(10, 10, 350, 350))
        self.ProgressBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ProgressBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProgressBar.setObjectName("ProgressBar")
        self.Progress = QtWidgets.QFrame(self.ProgressBar)
        self.Progress.setGeometry(QtCore.QRect(10, 10, 325, 325))
        self.Progress.setStyleSheet("QFrame {\n"
"    border-radius: 160px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0 rgba(15, 32, 39, 98), stop:1 rgba(44, 83, 100, 255));\n"
"}")
        self.Progress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Progress.setObjectName("Progress")
        self.Background = QtWidgets.QFrame(self.ProgressBar)
        self.Background.setGeometry(QtCore.QRect(10, 10, 325, 325))
        self.Background.setStyleSheet("QFrame { \n"
"    border-radius: 160px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(67, 67, 67, 255));\n"
"}")
        self.Background.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Background.setObjectName("Background")
        self.Info = QtWidgets.QFrame(self.ProgressBar)
        self.Info.setGeometry(QtCore.QRect(35, 35, 275, 275))
        self.Info.setStyleSheet("QFrame {\n"
"    border-radius: 135px;    \n"
"    background-color: rgba(21, 101, 192, 250);\n"
"}")
        self.Info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info.setObjectName("Info")
        self.Name = QtWidgets.QLabel(self.Info)
        self.Name.setGeometry(QtCore.QRect(10, 60, 251, 161))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(47)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Name.setFont(font)
        self.Name.setStyleSheet("background-color: none;\n"
"color: rgb(54, 60, 100);")
        self.Name.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Name.setObjectName("Name")
        self.label = QtWidgets.QLabel(self.Info)
        self.label.setGeometry(QtCore.QRect(60, 230, 151, 20))
        self.label.setObjectName("label")
        self.Background.raise_()
        self.Progress.raise_()
        self.Info.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "SplashScreen"))
        self.Name.setText(_translate("SplashScreen", "EmoCh"))
        self.label.setText(_translate("SplashScreen", "Made by Rakshan Sharma"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())

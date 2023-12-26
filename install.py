# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'install.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Installer(object):
    
    def setupUi(self, Installer):
        Installer.setObjectName("Installer") #### HERE
        Installer.resize(530, 394)
        Installer.setMouseTracking(True)
        self.Accept_Button = QtWidgets.QPushButton(Installer)
        self.Accept_Button.setGeometry(QtCore.QRect(430, 360, 89, 25))
        self.Accept_Button.setMouseTracking(True)
        self.Accept_Button.setObjectName("Accept_Button")
        self.Decline_Button = QtWidgets.QPushButton(Installer)
        self.Decline_Button.setGeometry(QtCore.QRect(10, 360, 89, 25))
        self.Decline_Button.setObjectName("Decline_Button")
        self.TermsAndConditions = QtWidgets.QTextBrowser(Installer)
        self.TermsAndConditions.setGeometry(QtCore.QRect(0, 0, 531, 351))
        self.TermsAndConditions.setObjectName("TermsAndConditions")

        self.retranslateUi(Installer)
        QtCore.QMetaObject.connectSlotsByName(Installer)
        ### HEREEEE
        self.Accept_Button.clicked.connect(self.accept)
        self.Decline_Button.clicked.connect(self.exit)

    def retranslateUi(self, Installer):
        _translate = QtCore.QCoreApplication.translate
        Installer.setWindowTitle(_translate("Installer", "Dialog"))
        self.Accept_Button.setText(_translate("Installer", "Accept"))
        self.Decline_Button.setText(_translate("Installer", "Decline"))
        self.TermsAndConditions.setHtml(_translate("Installer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")) ##HERE
    
    def accept(self):
        print(0)

    def exit(self):
        ## SURITY
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Installer = QtWidgets.QDialog()
    ui = Ui_Installer()
    ui.setupUi(Installer)
    Installer.setWindowTitle("Installer")
    Installer.setWindowIcon(QtGui.QIcon("//home/pranav/Downloads/main/repairing-service.ico"))
    Installer.setWindowIconText("/home/pranav/Downloads/main/repairing-service.ico") ##PATH
    Installer.show()
    sys.exit(app.exec_())
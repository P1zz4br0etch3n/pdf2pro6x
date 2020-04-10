# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poppler_not_installed_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_PopplerNotInstalledDialog(object):
    def setupUi(self, PopplerNotInstalledDialog):
        PopplerNotInstalledDialog.setObjectName("PopplerNotInstalledDialog")
        PopplerNotInstalledDialog.resize(381, 96)
        self.buttonBox = QtWidgets.QDialogButtonBox(PopplerNotInstalledDialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtWidgets.QLabel(PopplerNotInstalledDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(PopplerNotInstalledDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.retranslateUi(PopplerNotInstalledDialog)
        self.buttonBox.accepted.connect(PopplerNotInstalledDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(PopplerNotInstalledDialog)

    def retranslateUi(self, PopplerNotInstalledDialog):
        _translate = QtCore.QCoreApplication.translate
        PopplerNotInstalledDialog.setWindowTitle(_translate("PopplerNotInstalledDialog", "Poppler not installed"))
        self.label.setText(_translate("PopplerNotInstalledDialog", "Seems you have not installed poppler. Please see install instructions here:"))
        self.label_3.setText(_translate("PopplerNotInstalledDialog", "<a href=\"https://github.com/Belval/pdf2image#how-to-install\">https://github.com/Belval/pdf2image#how-to-install</a>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopplerNotInstalledDialog = QtWidgets.QDialog()
    ui = Ui_PopplerNotInstalledDialog()
    ui.setupUi(PopplerNotInstalledDialog)
    PopplerNotInstalledDialog.show()
    sys.exit(app.exec_())

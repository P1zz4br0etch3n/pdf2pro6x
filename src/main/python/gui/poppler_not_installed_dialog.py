# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/python/gui/poppler_not_installed_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopplerNotInstalledDialog(object):
    def setupUi(self, PopplerNotInstalledDialog):
        PopplerNotInstalledDialog.setObjectName("PopplerNotInstalledDialog")
        PopplerNotInstalledDialog.resize(372, 79)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        PopplerNotInstalledDialog.setFont(font)
        PopplerNotInstalledDialog.setSizeGripEnabled(False)
        PopplerNotInstalledDialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(PopplerNotInstalledDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(PopplerNotInstalledDialog)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(PopplerNotInstalledDialog)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(PopplerNotInstalledDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PopplerNotInstalledDialog)
        self.buttonBox.accepted.connect(PopplerNotInstalledDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(PopplerNotInstalledDialog)

    def retranslateUi(self, PopplerNotInstalledDialog):
        _translate = QtCore.QCoreApplication.translate
        PopplerNotInstalledDialog.setWindowTitle(_translate("PopplerNotInstalledDialog", "Poppler not installed"))
        self.label.setText(_translate("PopplerNotInstalledDialog", "Seems you have not installed poppler. Please see install instructions here:"))
        self.label_2.setText(_translate("PopplerNotInstalledDialog", "<a href=\"https://github.com/Belval/pdf2image#how-to-install\">https://github.com/Belval/pdf2image#how-to-install</a>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopplerNotInstalledDialog = QtWidgets.QDialog()
    ui = Ui_PopplerNotInstalledDialog()
    ui.setupUi(PopplerNotInstalledDialog)
    PopplerNotInstalledDialog.show()
    sys.exit(app.exec_())

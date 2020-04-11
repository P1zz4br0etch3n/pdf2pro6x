# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'success_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_SuccessDialog(object):
    def setupUi(self, SuccessDialog):
        SuccessDialog.setObjectName("SuccessDialog")
        SuccessDialog.resize(154, 71)
        self.buttonBox = QtWidgets.QDialogButtonBox(SuccessDialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 30, 71, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(SuccessDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.label.setObjectName("label")

        self.retranslateUi(SuccessDialog)
        self.buttonBox.accepted.connect(SuccessDialog.accept)
        self.buttonBox.rejected.connect(SuccessDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SuccessDialog)

    def retranslateUi(self, SuccessDialog):
        _translate = QtCore.QCoreApplication.translate
        SuccessDialog.setWindowTitle(_translate("SuccessDialog", "Success"))
        self.label.setText(_translate("SuccessDialog", "Conversion was successfull!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SuccessDialog = QtWidgets.QDialog()
    ui = Ui_SuccessDialog()
    ui.setupUi(SuccessDialog)
    SuccessDialog.show()
    sys.exit(app.exec_())

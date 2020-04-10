import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from pdf2image.exceptions import PDFInfoNotInstalledError

from gui.main import Ui_MainWindow
from gui.poppler_not_installed_dialog import Ui_PopplerNotInstalledDialog
from gui.success_dialog import Ui_SuccessDialog
from pdf2pro6x import main


class HideOnAcceptDialog(QtWidgets.QDialog):

    def accept(self):
        self.hide()


class MainWindow(QMainWindow):

    @staticmethod
    def set_path_to_pdf(path_to_pdf):
        ui.lineEdit.setText(path_to_pdf)

    @staticmethod
    def browse_slot():
        file_name, _ = QtWidgets.QFileDialog().getOpenFileName()
        ui.lineEdit.setText(file_name)

    @staticmethod
    def convert_slot():
        path_to_pdf = ui.lineEdit.text()
        if os.path.exists(path_to_pdf):
            dialog = HideOnAcceptDialog()

            try:
                main(path_to_pdf)
                ui_dialog = Ui_SuccessDialog()
            except PDFInfoNotInstalledError:
                ui_dialog = Ui_PopplerNotInstalledDialog()

            ui_dialog.setupUi(dialog)
            dialog.exec()


if __name__ == '__main__':
    path_to_pdf = sys.argv[1] if len(sys.argv) > 1 else None

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    if path_to_pdf:
        MainWindow.set_path_to_pdf(path_to_pdf)
    MainWindow.show()
    sys.exit(app.exec_())
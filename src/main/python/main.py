import os
import subprocess
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.platform import is_mac
from pdf2image.exceptions import PDFInfoNotInstalledError

from gui.main import Ui_MainWindow
from gui.poppler_not_installed_dialog import Ui_PopplerNotInstalledDialog
from gui.success_dialog import Ui_SuccessDialog
from pdf2pro6x import main


def _get_poppler_path_on_mac():
    process = subprocess.run(['which', 'pdfinfo'], stdout=subprocess.PIPE)
    print('try to find poppler path. return code is %d' % process.returncode)
    if process.returncode == 0:
        path = process.stdout.decode('utf-8').replace('/pdfinfo\n', '')
        print('path is %s' % path)
        return path
    else:
        return None


class HideOnAcceptDialog(QtWidgets.QDialog):

    def accept(self):
        self.hide()


class MainWindow(QMainWindow):

    @staticmethod
    def set_path_to_pdf(path_to_pdf):
        ui.lineEdit.setText(path_to_pdf)

    @staticmethod
    def browse_slot():
        file_name, _ = QtWidgets.QFileDialog().getOpenFileName(filter='*.pdf')
        if file_name:
            ui.lineEdit.setText(file_name)

    @staticmethod
    def convert_slot():
        path_to_pdf = ui.lineEdit.text()
        if os.path.exists(path_to_pdf):
            dialog = HideOnAcceptDialog()
            ui_dialog = None

            try:
                path_to_pro6x, _ = QtWidgets.QFileDialog().getSaveFileName(filter='*.pro6x')
                if path_to_pro6x:
                    main(path_to_pdf, path_to_pro6x, poppler_path)
                    ui_dialog = Ui_SuccessDialog()
            except PDFInfoNotInstalledError:
                ui_dialog = Ui_PopplerNotInstalledDialog()

            if ui_dialog:
                ui_dialog.setupUi(dialog)
                dialog.exec()


if __name__ == '__main__':
    path_to_pdf = sys.argv[1] if len(sys.argv) > 1 else None
    poppler_path = _get_poppler_path_on_mac() if is_mac() else None

    appctxt = ApplicationContext()
    MainWindow = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    if path_to_pdf:
        MainWindow.set_path_to_pdf(path_to_pdf)
    MainWindow.show()
    sys.exit(appctxt.app.exec_())

import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.platform import is_mac
from pdf2image.exceptions import PDFInfoNotInstalledError

from gui.main import Ui_MainWindow
from gui.poppler_not_installed_dialog import Ui_PopplerNotInstalledDialog
from gui.success_dialog import Ui_SuccessDialog
from pdf2pro6x import main, change_extension


class HideOnAcceptDialog(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # noinspection PyTypeChecker
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

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
                directory = change_extension(path_to_pdf, 'pro6x')
                path_to_pro6x, _ = QtWidgets.QFileDialog().getSaveFileName(filter='*.pro6x', directory=directory)
                if path_to_pro6x:
                    main(path_to_pdf, path_to_pro6x, poppler_path)
                    ui_dialog = Ui_SuccessDialog()
            except PDFInfoNotInstalledError:
                ui_dialog = Ui_PopplerNotInstalledDialog()

            if ui_dialog:
                ui_dialog.setupUi(dialog)
                dialog.exec()


def enable_file_drag(line_edit: QLineEdit) -> None:
    line_edit.setDragEnabled(True)

    def drag_enter_event(event: QDragEnterEvent) -> None:
        data = event.mimeData()
        url = data.urls()[0]
        if url and url.isLocalFile() and url.fileName().endswith('.pdf'):
            event.acceptProposedAction()

    def drop_event(event: QDropEvent) -> None:
        data = event.mimeData()
        url = data.urls()[0]
        if url and url.isLocalFile() and url.fileName().endswith('.pdf'):
            line_edit.setText(url.toLocalFile())

    line_edit.dragEnterEvent = drag_enter_event
    line_edit.dropEvent = drop_event


if __name__ == '__main__':
    path_to_pdf = sys.argv[1] if len(sys.argv) > 1 else None
    poppler_path = '/usr/local/bin' if is_mac() else None

    appctxt = ApplicationContext()
    MainWindow = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    enable_file_drag(ui.lineEdit)
    if path_to_pdf and os.path.exists(path_to_pdf):
        MainWindow.set_path_to_pdf(path_to_pdf)
    MainWindow.show()
    sys.exit(appctxt.app.exec_())

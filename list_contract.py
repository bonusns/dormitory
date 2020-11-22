# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_contract.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_list_contract(object):

    def openContract(self):
        from contract import Ui_contract
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_contract()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, list_contract):
        list_contract.setObjectName("list_contract")
        list_contract.resize(480, 491)
        list_contract.setMinimumSize(QtCore.QSize(300, 300))
        list_contract.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(list_contract)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 452, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_contract_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.import_contract_btn.setMinimumSize(QtCore.QSize(213, 40))
        self.import_contract_btn.setMaximumSize(QtCore.QSize(213, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.import_contract_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.import_contract_btn.setFont(font)
        self.import_contract_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.import_contract_btn.setObjectName("import_contract_btn")
        self.horizontalLayout.addWidget(self.import_contract_btn)
        self.back_to_contract_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.back_to_contract_btn.setMinimumSize(QtCore.QSize(220, 40))
        self.back_to_contract_btn.setMaximumSize(QtCore.QSize(220, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.back_to_contract_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_to_contract_btn.setFont(font)
        self.back_to_contract_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.back_to_contract_btn.setObjectName("back_to_contract_btn")

        self.back_to_contract_btn.clicked.connect(self.openContract)
        self.back_to_contract_btn.clicked.connect(list_contract.close)

        self.horizontalLayout.addWidget(self.back_to_contract_btn)
        self.Contract_info = QtWidgets.QListWidget(self.centralwidget)
        self.Contract_info.setGeometry(QtCore.QRect(20, 89, 440, 371))
        self.Contract_info.setAutoFillBackground(False)
        self.Contract_info.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"selection-color: rgb(85, 170, 255);")
        self.Contract_info.setObjectName("Contract_info")
        item = QtWidgets.QListWidgetItem()
        self.Contract_info.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Contract_info.addItem(item)
        list_contract.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(list_contract)
        self.statusbar.setObjectName("statusbar")
        list_contract.setStatusBar(self.statusbar)

        self.retranslateUi(list_contract)
        QtCore.QMetaObject.connectSlotsByName(list_contract)

    def retranslateUi(self, list_contract):
        _translate = QtCore.QCoreApplication.translate
        list_contract.setWindowTitle(_translate("list_contract", "Список договоров"))
        self.import_contract_btn.setText(_translate("list_contract", "Импортировать в Excel"))
        self.back_to_contract_btn.setText(_translate("list_contract", "Вернуться в меню договора"))
        __sortingEnabled = self.Contract_info.isSortingEnabled()
        self.Contract_info.setSortingEnabled(False)
        item = self.Contract_info.item(0)
        item.setText(_translate("list_contract", "addawd"))
        item = self.Contract_info.item(1)
        item.setText(_translate("list_contract", "dtyjhn"))
        self.Contract_info.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    list_contract = QtWidgets.QMainWindow()
    ui = Ui_list_contract()
    ui.setupUi(list_contract)
    list_contract.show()
    sys.exit(app.exec_())

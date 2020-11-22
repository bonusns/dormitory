# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_cost.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_list_cost(object):

    def openCost(self):
        from cost import Ui_Cost
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Cost()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, list_cost):
        list_cost.setObjectName("list_cost")
        list_cost.resize(480, 291)
        list_cost.setMinimumSize(QtCore.QSize(300, 291))
        list_cost.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(list_cost)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(8, 20, 461, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_cost_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.import_cost_btn.setMinimumSize(QtCore.QSize(200, 40))
        self.import_cost_btn.setMaximumSize(QtCore.QSize(190, 16777215))
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
        self.import_cost_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.import_cost_btn.setFont(font)
        self.import_cost_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.import_cost_btn.setObjectName("import_cost_btn")
        self.horizontalLayout.addWidget(self.import_cost_btn)
        self.back_to_cost_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.back_to_cost_btn.setMinimumSize(QtCore.QSize(240, 40))
        self.back_to_cost_btn.setMaximumSize(QtCore.QSize(230, 16777215))
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
        self.back_to_cost_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_to_cost_btn.setFont(font)
        self.back_to_cost_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.back_to_cost_btn.setObjectName("back_to_cost_btn")

        self.back_to_cost_btn.clicked.connect(self.openCost)
        self.back_to_cost_btn.clicked.connect(list_cost.close)

        self.horizontalLayout.addWidget(self.back_to_cost_btn)
        self.Cost_info = QtWidgets.QListWidget(self.centralwidget)
        self.Cost_info.setGeometry(QtCore.QRect(20, 89, 440, 171))
        self.Cost_info.setAutoFillBackground(False)
        self.Cost_info.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"selection-color: rgb(85, 170, 255);")
        self.Cost_info.setObjectName("Cost_info")
        item = QtWidgets.QListWidgetItem()
        self.Cost_info.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Cost_info.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Cost_info.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Cost_info.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Cost_info.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Cost_info.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Cost_info.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Cost_info.addItem(item)
        list_cost.setCentralWidget(self.centralwidget)

        self.retranslateUi(list_cost)
        QtCore.QMetaObject.connectSlotsByName(list_cost)

    def retranslateUi(self, list_cost):
        _translate = QtCore.QCoreApplication.translate
        list_cost.setWindowTitle(_translate("list_cost", "Список стоимостей"))
        self.import_cost_btn.setText(_translate("list_cost", "Импортировать в Excel"))
        self.back_to_cost_btn.setText(_translate("list_cost", "Вернуться в меню стоимостей"))
        __sortingEnabled = self.Cost_info.isSortingEnabled()
        self.Cost_info.setSortingEnabled(False)
        item = self.Cost_info.item(0)
        item.setText(_translate("list_cost", "Стоимость: 560 р; Льготы: Без льгот"))
        item = self.Cost_info.item(1)
        item.setText(_translate("list_cost", "Стоимость: 600 р; Льготы: Без льгот"))
        item = self.Cost_info.item(2)
        item.setText(_translate("list_cost", "Стоимость: 0 р; Льготы: Инвалид"))
        item = self.Cost_info.item(3)
        item.setText(_translate("list_cost", "Стоимость: 0 р; Льготы: Сирота"))
        item = self.Cost_info.item(4)
        item.setText(_translate("list_cost", "Стоимость: 0 р; Льготы: ЧАЭС"))
        item = self.Cost_info.item(5)
        item.setText(_translate("list_cost", "Стоимость: 280 р; Льготы: Без льгот"))
        item = self.Cost_info.item(6)
        item.setText(_translate("list_cost", "Стоимость: 300 р; Льготы: Без льгот"))
        item = self.Cost_info.item(7)
        item.setText(_translate("list_cost", "Стоимость: 0 р; Льготы: Инвалид, Сирота"))
        self.Cost_info.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    list_cost = QtWidgets.QMainWindow()
    ui = Ui_list_cost()
    ui.setupUi(list_cost)
    list_cost.show()
    sys.exit(app.exec_())
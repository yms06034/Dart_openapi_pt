# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(433, 346)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 411, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.get_corpcode_excel_btn = QtWidgets.QPushButton(self.tab_2)
        self.get_corpcode_excel_btn.setGeometry(QtCore.QRect(70, 90, 271, 91))
        self.get_corpcode_excel_btn.setObjectName("get_corpcode_excel_btn")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(70, 20, 131, 41))
        self.label_24.setObjectName("label_24")
        self.btn_del_corpcode = QtWidgets.QPushButton(self.tab)
        self.btn_del_corpcode.setGeometry(QtCore.QRect(300, 20, 41, 30))
        self.btn_del_corpcode.setObjectName("btn_del_corpcode")
        self.corpcode_list = QtWidgets.QListWidget(self.tab)
        self.corpcode_list.setGeometry(QtCore.QRect(70, 60, 271, 141))
        self.corpcode_list.setObjectName("corpcode_list")
        self.btn_start = QtWidgets.QPushButton(self.tab)
        self.btn_start.setGeometry(QtCore.QRect(70, 220, 271, 31))
        self.btn_start.setObjectName("btn_start")
        self.btn_get_corpcode = QtWidgets.QPushButton(self.tab)
        self.btn_get_corpcode.setGeometry(QtCore.QRect(180, 20, 111, 31))
        self.btn_get_corpcode.setObjectName("btn_get_corpcode")
        self.tabWidget.addTab(self.tab, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.total_num = QtWidgets.QLabel(self.widget)
        self.total_num.setGeometry(QtCore.QRect(480, 210, 61, 41))
        self.total_num.setText("")
        self.total_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_num.setObjectName("total_num")
        self.btn_get_corpcode_2 = QtWidgets.QPushButton(self.widget)
        self.btn_get_corpcode_2.setGeometry(QtCore.QRect(180, 20, 111, 31))
        self.btn_get_corpcode_2.setObjectName("btn_get_corpcode_2")
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setGeometry(QtCore.QRect(70, 20, 131, 41))
        self.label_25.setObjectName("label_25")
        self.corpcode_list_2 = QtWidgets.QListWidget(self.widget)
        self.corpcode_list_2.setGeometry(QtCore.QRect(70, 60, 271, 141))
        self.corpcode_list_2.setObjectName("corpcode_list_2")
        self.btn_del_corpcode_2 = QtWidgets.QPushButton(self.widget)
        self.btn_del_corpcode_2.setGeometry(QtCore.QRect(300, 20, 41, 30))
        self.btn_del_corpcode_2.setObjectName("btn_del_corpcode_2")
        self.btn_start_2 = QtWidgets.QPushButton(self.widget)
        self.btn_start_2.setGeometry(QtCore.QRect(70, 220, 271, 31))
        self.btn_start_2.setObjectName("btn_start_2")
        self.tabWidget.addTab(self.widget, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.get_corpcode_excel_btn.setText(_translate("MainWindow", "가져오기"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "회사코드 GET"))
        self.label_24.setText(_translate("MainWindow", "회사 코드 리스트"))
        self.btn_del_corpcode.setText(_translate("MainWindow", "제거"))
        self.btn_start.setText(_translate("MainWindow", "시작"))
        self.btn_get_corpcode.setText(_translate("MainWindow", "불러오기"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "다중회사 주요계정"))
        self.btn_get_corpcode_2.setText(_translate("MainWindow", "불러오기"))
        self.label_25.setText(_translate("MainWindow", "회사 코드 리스트"))
        self.btn_del_corpcode_2.setText(_translate("MainWindow", "제거"))
        self.btn_start_2.setText(_translate("MainWindow", "시작"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "단일회사 전체 재무제표"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

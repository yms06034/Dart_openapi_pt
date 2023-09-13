import sys
import os
import pandas as pd

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from main1 import Ui_MainWindow

import getCorpCode as gcc
from multipleMajorAccounts import start_multipleMajorAccounts
from financialStatement import start_financialStatement

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


main_ui = Ui_MainWindow()

NAME = 'Dart OpenApi'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        main_ui.setupUi(self)
        self.setWindowTitle(NAME)
        
        favicon = resource_path('favicon.png')
        self.setWindowIcon(QIcon(favicon))
        
        self.timer = QTimer(self)
        
        self.corpcode_list = []
        self.corpcode_list_2 = []
        
        main_ui.get_corpcode_excel_btn.clicked.connect(self.get_corpcode_start)
        
        main_ui.btn_get_corpcode.clicked.connect(self.btn_get_corpcode_click)
        main_ui.btn_get_corpcode_2.clicked.connect(self.btn_get_corpcode_2click)
        
        main_ui.btn_del_corpcode.clicked.connect(self.btn_del_corpcode_click)
        main_ui.btn_del_corpcode_2.clicked.connect(self.btn_del_corpcode_2click)
        
        main_ui.btn_start.clicked.connect(self.btn_start_click)
        main_ui.btn_start_2.clicked.connect(self.btn_start_2click)
        
        
    def get_corpcode_start(self):
        result = gcc.get_corpcode_start()
        if result:
            QMessageBox.information(self, NAME, "엑셀로 추출이 완료되었습니다.")
        
# ---------------------------------------------------------------------------------------------------------------------------

        
    def btn_get_corpcode_click(self):
        path, _ = QFileDialog.getOpenFileNames(self)
        
        try:
            if path[0].split('.')[-1] == 'xlsx':
                df_code = pd.read_excel(path[0], dtype=str)
                df_list = df_code[0].to_list()
                print(df_list)
                main_ui.corpcode_list.addItems(df_list)
                self.corpcode_list.append(df_list)
            else:
                QMessageBox.information(self,NAME,'파일의 확장자가 xlsx 아닙니다.')
                return
        except:
            QMessageBox.information(self, NAME, "파일 양식을 확인 후 다시 시도해주세요.")
            return
                
    def btn_del_corpcode_click(self):
        option = QMessageBox.warning(self, NAME, "회사 코드 리스트를 삭제하겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if option == QMessageBox.Yes:
            self.corpcode_list = []
            main_ui.corpcode_list.clear()
            return
        
    def btn_start_click(self):
        result = start_multipleMajorAccounts(self.corpcode_list)
        if result:
            QMessageBox.information(self, NAME, "추출이 완료되었습니다.")
            return
        else:
            QMessageBox.information(self, NAME, "추출할 데이터가 없습니다.")
            return
    
    
# ---------------------------------------------------------------------------------------------------------------------------


    def btn_get_corpcode_2click(self):
        path, _ = QFileDialog.getOpenFileNames(self)
        try:
            if path[0].split('.')[-1] == 'xlsx':
                df_code = pd.read_excel(path[0], dtype=str)
                df_list = df_code[0].to_list()
                print(df_list)
                main_ui.corpcode_list_2.addItems(df_list)
                self.corpcode_list_2.append(df_list)
            else:
                QMessageBox.information(self,NAME,'파일의 확장자가 xlsx 아닙니다.')
                return
        except:
            QMessageBox.information(self, NAME, "파일 양식을 확인 후 다시 시도해주세요.")
            return
                
    def btn_del_corpcode_2click(self):
        option = QMessageBox.warning(self, NAME, "회사 코드 리스트를 삭제하겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if option == QMessageBox.Yes:
            self.corpcode_list_2 = []
            main_ui.corpcode_list_2.clear()
            return
        
    def btn_start_2click(self):
        result = start_financialStatement(self.corpcode_list_2)
        if result:
            QMessageBox.information(self, NAME, "추출이 완료되었습니다.")
            return
                
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
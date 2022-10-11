# -*- coding: utf-8 -*-
"""
@Time:2021/11/2 22:20
@Auth"JunLin615
@File:maintext.py
@IDE:PyCharm
@Motto:With the wind light cloud light mentality, do insatiable things
@email:ljjjun123@gmail.com 
"""
# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog
from untitled import Ui_MainWindow
import sys
import os
import bjsb


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        demo格式：
        b'1SVVVVFDDDDDE'：byte格式，第一位1，意思是经典加工；第二位对应speed1，旋转速度，单位Hz；
        3-6：共4位，对应velocity2，单位10um/s；7位：+ or -，displacement的正负；8-12：displacement的绝对值，单位10um
        13：E，意味END，命令结束。
        """
        super(MainWindow, self).__init__(parent)#继承父类的构造函数
        self.setupUi(self)
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        #QMetaObject.connectSlotsByName(self)#别加这句话，会导致触发两次
        #self.matplotlibwidget_dynamic.setVisible(False)
        #self.matplotlibwidget_static.setVisible(False)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        读取图片
        """
        self.slot_btn_chooseFile()


    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        读取轨迹文件
        """
        print(2)
        self.slot_btn_saveFile()

    def slot_btn_chooseFile(self):
        self.fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                self.cwd,  # 起始路径
                                                                "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,用双分号间隔

        if self.fileName_choose == "":
            print("\n取消选择")
            return

        print("\n你选择的文件为:")
        print(self.fileName_choose)
        print("文件筛选器类型: ", filetype)
        self.textEdit.setText(self.fileName_choose)

    def slot_btn_saveFile(self):




        self.save_fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                    "文件保存",
                                    self.cwd, # 起始路径
                                    "All Files (*);;Text Files (*.txt)")

        if self.save_fileName_choose == "":
            print("\n取消选择")
            return

        print("\n你选择要保存的文件为:")
        print(self.save_fileName_choose)
        print("文件筛选器类型: ",filetype)
        self.textEdit_2.setText("Wait a minute")
        bjsb.conversion(self.fileName_choose,self.save_fileName_choose)
        self.textEdit_2.setText(self.fileName_choose)

    #def conversion(self):

    # 当窗口非继承QtWidgets.QDialog时，self需替换成 None
	#当窗口非继承QtWidgets.QDialog时，self需替换成 None

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

#getCodeList 시작
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kiwoom = QAxWidget("KHOPENAPI.KGOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.setWindowTitle("종목 코드")
        self.setGeometry(300,300,300,150)

        btn1 = QPushButton("종목코드 얻기",self)
        btn1.move(190, 10)
        btn1.clicked.connect(self.btn1_clicked)

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(10,10,170,130)

    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("GetMasterCodeName(QString)",[x])
        kospi_code_list = ret.split(';')
        #Code이름 추가할 빈 리스트
        kospi_code_name_list =[]


        for x in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString",[x])
            kospi_code_name_list.append(x + " : " + name)

        self.listWidget.addItems(kospi_code_name_list)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec())

# start = datetime.datetime(2016,2,19)
# end = datetime.datetime(2019,3,4)
# data_test = web.DataReader("AAPL","yahoo",start,end)
#
# plt.plot(data_test.index,data_test['Adj Close'])
# plt.show()
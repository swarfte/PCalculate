'''
Author: Swarfte
Date: 2021-08-09 21:36:18
LastEditors: Chau Lap Tou
LastEditTime: 2021-08-30 21:14:07
FilePath: \calculate\start.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
'''

import PyQt5 as PQ
import sys
import main

def start_gui():
    #*下方為啟動GUI視窗
    app = PQ.QtWidgets.QApplication(sys.argv)#創建進程(?)
    start = main.MainWindow()#實例化
    start.show()#展示畫面
    sys.exit(app.exec_())#關閉進程(?)
    
if __name__ == '__main__':
    start_gui()

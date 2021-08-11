import PyQt5 as PQ
import Ui_gui as GUI
import local_button as LB
import local_keybroad as LK

#& main.py檔案作為終端控制台,處理不同部件的交互功能
class MainWindow(PQ.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()#*繼承PQ.QtWidgets.QMainWindow的屬性
        
        #*獲取GUI檔案的內容
        self.ui = GUI.Ui_MainWindow()#!繼承界面檔案(ui轉py後)的屬性,把UI下的方法繼承到ui
        self.ui.setupUi(self)#*GUI初始化
        self.button = LB.button_event(self.ui)#*利用local_button.py的方法初始化並綁定按鈕事件
        self.keyboard = LK.keybroad_event(self.ui)#*利用local_keybroad.py的方法初始化並綁定按鈕事件
'''
Author: Swarfte
Date: 2021-08-09 21:36:18
LastEditors: Swarfte
LastEditTime: 2021-08-10 23:25:36
FilePath: \calculate\local_keybroad.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
'''

class keybroad_event (object):
    def __init__(self,gui):
        super().__init__()
        self.keybroad = gui
        self.input = ""

        #&在button那邊已綁定了對應按鈕的函數
        #?關於1~9的快捷鍵
        
        self.number =[
            self.keybroad.zero,#*0
            self.keybroad.one,#*1
            self.keybroad.two,#*2
            self.keybroad.three,#*3
            self.keybroad.four,#*4
            self.keybroad.five,#*5
            self.keybroad.six,#*6
            self.keybroad.seven,#*7
            self.keybroad.eight,#*8
            self.keybroad.nine#*9
        ]
        
        for x in range(len(self.number)) :
            self.number[x].setShortcut(str(x))
        
        #?關於運算符號的部份(除等號)
        self.calculating_signs =[
            self.keybroad.addition,#*加號
            self.keybroad.subtraction,#*減號
            self.keybroad.multiplication,#*乘號
            self.keybroad.division,#*除號
            self.keybroad.point,#*小數點
            self.keybroad.comma,#*逗號
            self.keybroad.index,#*次方號
            self.keybroad.leftparenthesis,#*左括號
            self.keybroad.closingparenthesis,#*右括號
            self.keybroad.remainder,#*餘號
            self.keybroad.log
        ]
        
        self.calculating_signs_value = [
            "+","-","*","./",".",",","Shift+6","Shift+9","Shift+0","Shift+5","l"
        ]
        
        for x in range(len(self.calculating_signs)):
            self.calculating_signs[x].setShortcut(self.calculating_signs_value[x])
        
        #?功能類的部份
        self.Tool =[
            self.keybroad.clean,#*CLS(刷新鍵)
            self.keybroad.equal,#*等號
            self.keybroad.deletenum,#*剛除最尾的數字
            self.keybroad.randommath,#*生成隨機數字
            self.keybroad.randomenglish,#*生成隨機英文
            self.keybroad.lastnumber#*記憶鍵(顯示上一個等號後的結果)
        ]
        
        self.Tool_value=[
            "Ctrl+Backspace","Enter","Backspace","d","a","Tab"
        ]
        
        for x in range(len(self.Tool)):
            self.Tool[x].setShortcut(self.Tool_value[x])
        
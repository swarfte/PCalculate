'''
Author: Swarfte
Date: 2021-08-09 21:36:18
LastEditors: Swarfte
LastEditTime: 2021-08-11 00:23:36
FilePath: \calculate\local_function.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
'''
import random as rd
import math
import re

Lastnumber = ""#*用作記憶功能,即紀錄結果

def CalcLog(sentence):#*計算對數
    get_num = sentence
    log_base = 10
    ans = 0
    if "," in get_num:#*輸入底數的情況
        number = get_num.split(",")
        log_base = float(number[0])#*用前面那個數為底
        logarithm = float(number[1])#*逗號後的為對數
    else:#*沒有輸入底數的情況
        logarithm = float(sentence)
    ans = math.log(logarithm,log_base)#*log() 函式接受兩個引數。第一個引數是數字，第二個引數是基值
    return ans

class function(object):
    def __init__(self,gui):
        super().__init__()
        self.function = gui#*獲取傳入的gui
        self.input = self.function.InputLine.text()#*獲取當前輸入端的資料
        self.output = self.function.OutputLine.text()#*獲取當前輸出端的資料
        
    def Test(self):
        print("hello")
        
    def Printf(self,push,string):#*輸出新增的文字
        self.input = push.text()#*獲取傳入的元件的資料(針對Line)
        self.input += string
        push.setText(self.input)
        
    def Clean(self,inputline,outputline) :#*清除line的資料
        self.input = inputline.text()
        self.input = ""#*重置輸入欄
        inputline.setText(self.input)
        outputline.setText(self.input)
        
    def Delete(self,push):#*用作清除不需要的字元
        self.input = push.text()
        self.input = self.input[:-1]#*刪除最後的字元
        push.setText(self.input)
        
    def RandomMath(self,inputline,outputline):#*獲取隨機數字
        try:
            global Lastnumber
            num = 0
            self.input = inputline.text()
            if len(self.input) == 0 :#*沒有輸入數字時,則像普體骰子一樣輸出1~6
                num = rd.randint(1,6)
            else:
                if "," in self.input :#*輸入區間的話則骰出區間內的數字
                    numlist = self.input.split(",")
                    num = rd.randint(int(numlist[0]),int(numlist[1]))
                else:#*只輸入一個數字的話則為1~該數字隨機骰出一個
                    num = rd.randint(1,int(self.input))
            Lastnumber = str(num)
            outputline.setText(str(num))
        except :
            outputline.setText("error")
    
    def RandomEnglish(self,inputline,outputline):#*隨機生成英文
        try:
            global Lastnumber
            english =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            eng = ""
            self.input = inputline.text()
            if len(self.input) == 0 :#*沒有輸入數字時,則像普體選擇題一樣輸出A~D
                eng = english[rd.randint(0,3)]
            else:#*輸入區間的話則骰出區間內的字母
                if "," in self.input :
                    englist = self.input.split(",")
                    eng = english[rd.randint(int(englist[0])-1,int(englist[1])-1)]
                else:#*只輸入一個數字的話則為1~該數字隨機骰出一個字母
                    eng = english[rd.randint(1,int(self.input))]
            Lastnumber = eng
            outputline.setText(eng)
        except :
            outputline.setText("error")
            
    def RememberNumber(self,push):#*記憶功能
        global Lastnumber
        self.input = push.text()
        self.input += Lastnumber #*加左原本的句子上
        push.setText(self.input)
        
    
    def Basic (self,inputline,outputline):#*用作計算結果
        try:
            global Lastnumber
            self.input = inputline.text()
            while "log" in self.input:
                choose = re.compile(r"log[0-9]+\.?[0-9]*\,[0-9]+\.?[0-9]*|log[0-9]+\.?[0-9]*")#*找出log數的位置
                log_native = re.search(choose,self.input).group()#*帶有Log字串
                log_get = log_native[3:]#*獲取關建的數字(log的數字)
                log_ans = str(CalcLog(log_get)) #*獲取答案
                self.input = self.input.replace(log_native,log_ans)#*把答案取代輸入中的log,同時覆蓋原來的輸入端
                    
            ans = eval(self.input)#*計算結果
            outputline.setText(str(ans))#*在輸出端顯示結果
            Lastnumber = str(ans)
        except :
            outputline.setText("error")#*有問題時則報錯
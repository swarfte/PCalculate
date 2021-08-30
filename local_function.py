'''
Author: Swarfte
Date: 2021-08-09 21:36:18
LastEditors: Chau Lap Tou
LastEditTime: 2021-08-30 21:57:56
FilePath: \calculate\local_function.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
'''
import random as rd
import math
import re
import sympy as SP

Lastnumber = ""#*用作記憶功能,即紀錄結果
DecimalPlaces = 2 #*預設保留的小數位

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

def CalcTrigonometric(sentence,mode):#*計算三角函數
    get_num = sentence
    ans = 0
    if "," in get_num:
        get_num = get_num[:len(get_num)-1]
        num = float(get_num)
        if mode == "sin" :
            ans = SP.cos(math.radians(num))#*化為弧度制
        elif mode == "tan":
            ans = SP.cot(math.radians(num))
        elif mode == "sec":
            ans = SP.csc(math.radians(num))
    else:
        num = float(get_num)
        if mode == "sin" :
            ans = SP.sin(math.radians(num))
        elif mode == "tan":
            ans = SP.tan(math.radians(num))
        if mode == "sec" :
            ans = SP.sec(math.radians(num))
    return ans#*預設保留小數位後2位

def ReplaceExpression(sentence):
    ans = sentence
    if ".." in ans: #*在運算時改變式子保留的小數點,且只允許式子出現一次
        choose = re.compile(r"\.\.[0-9]+")
        num_native = re.search(choose,ans).group()#*帶有..
        num_get = num_native[2:]
        global DecimalPlaces
        DecimalPlaces = int(num_get)
        ans = ans.replace(num_native,"")#*用空白替換
        
    while "log" in ans:#*處理式子中全部Log數
        choose = re.compile(r"log[0-9]+\.?[0-9]*\,[0-9]+\.?[0-9]*|log[0-9]+\.?[0-9]*")#*找出log數的位置
        log_native = re.search(choose,ans).group()#*帶有Log字串
        log_get = log_native[3:]#*獲取關建的數字(log的數字)
        log_ans = str(CalcLog(log_get)) #*獲取答案
        ans = ans.replace(log_native,log_ans)#*把答案取代輸入中的log,同時覆蓋原來的輸入端
        
    while "sin" in ans:#*處理式子中全迎的sin/cos
        choose = re.compile(r"sin[0-9]+\.?[0-9]*\,?")#*找出sin的位置
        num_native = re.search(choose,ans).group()#*帶有sin
        num_get = num_native[3:]
        num_ans= str(CalcTrigonometric(num_get,"sin"))
        ans = ans.replace(num_native,num_ans)
        
    while "tan" in ans:#*處理式子中全迎的tan/cos
        choose = re.compile(r"tan[0-9]+\.?[0-9]*\,?")#*找出tan的位置
        num_native = re.search(choose,ans).group()#*帶有tan
        num_get = num_native[3:]
        num_ans= str(CalcTrigonometric(num_get,"tan"))
        ans = ans.replace(num_native,num_ans)
        
    while"sec" in ans:#*處理式子中全迎的sec/csc
        choose = re.compile(r"sec[0-9]+\.?[0-9]*\,?")#*找出sec的位置
        num_native = re.search(choose,ans).group()#*帶有sce
        num_get = num_native[3:]
        num_ans= str(CalcTrigonometric(num_get,"sec"))
        ans = ans.replace(num_native,num_ans)
        
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
            self.input = ReplaceExpression(self.input)#*處理log數
            
            global DecimalPlaces
            try :
                ans = round(eval(self.input),DecimalPlaces)#*計算結果
            except:
                ans = str(eval(self.input))
                ans += "it is a error"
            outputline.setText(str(ans))#*在輸出端顯示結果
            Lastnumber = str(ans)
        except :
            outputline.setText("error")#*有問題時則報錯
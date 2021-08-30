'''
Author: Swarfte
Date: 2021-08-09 21:36:18
LastEditors: Chau Lap Tou
LastEditTime: 2021-08-30 21:02:06
FilePath: \calculate\local_button.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
'''
import local_function as LF
class button_event(object):
    def __init__(self,gui):#*傳入main的GUI檔案
        super().__init__()
        self.buttons = gui#*實例化gui,用作處理button的內容
        self.func = LF.function(gui)
        self.input = ""#*初始的輸入欄
        
        
        #*進行按鍵綁定
        #!利用lambda函數讓輸入函數變成可調用
        #?1~9的部份
        self.buttons.zero.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"0"))#*按下按鈕0時輸出"0"
        self.buttons.one.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"1"))#*按下按鈕1時輸出"1"
        self.buttons.two.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"2"))#*按下按鈕2時輸出"2"
        self.buttons.three.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"3"))#*按下按鈕3時輸出"3"
        self.buttons.four.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"4"))#*按下按鈕4時輸出"4"
        self.buttons.five.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"5"))#*按下按鈕5時輸出"5"
        self.buttons.six.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"6"))#*按下按鈕6時輸出"6"
        self.buttons.seven.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"7"))#*按下按鈕7時輸出"7"
        self.buttons.eight.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"8"))#*按下按鈕8時輸出"8"
        self.buttons.nine.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"9"))#*按下按鈕9時輸出"9"
        
        #?運算符號的部份(除等號)
        self.buttons.addition.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"+"))#*按下按鈕+時輸出"+"
        self.buttons.subtraction.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"-"))#*按下按鈕-時輸出"-"
        self.buttons.multiplication.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"*"))#*按下按鈕*時輸出"*"
        self.buttons.division.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"/"))#*按下按鈕/時輸出"/"
        self.buttons.point.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"."))#*按下按鈕.時輸出"."
        self.buttons.comma.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,","))#*按下按鈕,.時輸出","
        self.buttons.index.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"**"))#*按下按鈕^時輸出"**"
        self.buttons.leftparenthesis.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"("))#*按下按鈕(時輸出"("
        self.buttons.closingparenthesis.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,")"))#*按下按鈕)時輸出")"
        self.buttons.remainder.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"%"))#*按下按鈕%時輸出"%"
        self.buttons.log.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"log"))#*按下按鈕log時輸出"log"
        self.buttons.sin.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"sin"))#*按下按鈕log時輸出"log"
        self.buttons.tan.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"tan"))#*按下按鈕log時輸出"log"
        self.buttons.sec.clicked.connect(lambda:self.func.Printf(self.buttons.InputLine,"sec"))#*按下按鈕log時輸出"log"
        
        #?功能類的部份
        self.buttons.clean.clicked.connect(lambda:self.func.Clean(self.buttons.InputLine,self.buttons.OutputLine))#&按下按鈕CLS時清空輸入欄
        self.buttons.equal.clicked.connect(lambda:self.func.Basic(self.buttons.InputLine,self.buttons.OutputLine))#&按下按鈕=時在輸出端輸出結果
        self.buttons.deletenum.clicked.connect(lambda:self.func.Delete(self.buttons.InputLine))#&按下按鈕<-時刪除前一個字符
        self.buttons.randommath.clicked.connect(lambda:self.func.RandomMath(self.buttons.InputLine,self.buttons.OutputLine))#&按下按鈕DICE時會根據輸入端輸出對應的結果
        self.buttons.randomenglish.clicked.connect(lambda:self.func.RandomEnglish(self.buttons.InputLine,self.buttons.OutputLine))#&按下按鈕ABC時會根據輸入端輸出對應的結果
        self.buttons.lastnumber.clicked.connect(lambda:self.func.RememberNumber(self.buttons.InputLine))#&記憶鍵功能
        
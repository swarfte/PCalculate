'''
Author: Swarfte
Date: 2021-08-10 22:58:00
LastEditors: Swarfte
LastEditTime: 2021-08-10 23:34:55
FilePath: \calculate\test.py
FileOutput: pyinstaller -F -w file_name.py -p C:/python/lib/site-packages 
GithubName: Swarfte
'''
import math
def CalcLog(sentence):#*計算對數
    num = sentence
    log_base = 10
    ans = 0
    if "," in num:#*輸入底數的情況
        number = num.split(",")
        log_base = int(number[0])#*用前面那個數為底
        logarithm = int(number[1])#*逗號後的為對數
    else:#*沒有輸入底數的情況
        logarithm = int(sentence)
    ans = math.log(logarithm,log_base)#*log() 函式接受兩個引數。第一個引數是數字，第二個引數是基值
    return ans

print(CalcLog("2,16"))
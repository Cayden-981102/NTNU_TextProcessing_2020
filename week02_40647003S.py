#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def myfunction(inputSTR):
    '''
    這支程式的主要函式(「函式」就是「功能」的意思！)
    '''
    #print("Hello {}, {}".format(inputSTR, "你好"))

    myNameSTR = inputSTR[0:3]
    myIDSTR = inputSTR[4:]
    print(" substring index 切出姓名和學號:")
    print("名字:{}".format(myNameSTR))
    print("學號:{}".format(myIDSTR))


    inputSTRLIST = inputSTR.split(" ")
    print("\n split() 切出姓名和學號:")
    print("名字：{}".format(inputSTRLIST[0]))
    print("學號：{}".format(inputSTRLIST[1]))
'''
    messageSTR = """
    「程式設計與基礎資料型態與中文構詞學」
    整堂課的資訊量爆炸，在知識的海洋裡衝浪
    超過癮的啊啊啊啊！
    """
    #print(messageSTR)
'''

#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR = "楊家明 40647003S"

    myfunction(nameSTR)
